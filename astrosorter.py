# -*- coding: utf-8 -*-

# =============================================================================
# IMPORTS
# =============================================================================

import os
import sys
import ctypes

if getattr(sys, 'frozen', False):
    local_path = os.path.dirname(sys.executable)
elif __file__:
    local_path = os.path.dirname(__file__)
os.chdir(os.path.join(local_path, ''))

import exifread
import numpy as np
import pandas as pd
import pickle
import time
from datetime import datetime, date
import rawpy
import imageio
from PIL import Image
import shutil

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt, QThreadPool
import pyqt5ac

from modules import build, threading, models

# =============================================================================
# APP SETUP
# =============================================================================
pyqt5ac.main(config='resources/resources config.yml')
app_id = 'AstroSorter.AstroSorter.AstroSorter.AstroSorter'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
form_class = uic.loadUiType('gui/astrosorter.ui')[0]; print('\n')
app = QApplication(sys.argv)

# =============================================================================
# MAIN CLASS
# =============================================================================
class AstroSorter(QMainWindow, form_class):
    def __init__(self, parent=None):
        # Build the main GUI
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.show()
        self.app = app
        build.core(self)
        
        # Set up threading
        self.threadpool = QThreadPool()
        
        # Folder variables
        self.default_save_folder = os.path.abspath('test/')
        self.test_location = os.path.abspath('test/')
        
        # These local paths obviously will not work on your computer
        self.astro_folder = 'D:/ElliotYoung/Pictures/Astro/'
        self.test_pic = 'C:/Users/ElliotYoung/Google Drive/Code/Github/AstroSorter/test/Light/light (2).CR2'
        
        # Photo variables
        self.pic_exts = ('cr2', 'png', 'jpg', 'jpeg', 'tiff', 'bmp', 'fits')
        self.metadata_fields = {
            'Filename': str,
            'Image DateTime': str,
            'FrameType': str,
            'EXIF ExposureTime': str,
            'EXIF ISOSpeedRatings': int,
            'EXIF FocalLength': int,
            'EXIF FNumber': str,
            'Image ImageWidth': int,
            'Image ImageLength': int,
            'EXIF ColorSpace': str,
            'Image Make': str,
            'Image Model': str,
            'EXIF LensModel': str,
            'EXIF ExposureProgram': str,
            'EXIF SensitivityType': str,
            'EXIF Flash': str,
            'EXIF LensSpecification': list,
            'DestinationFolder': str,
            'DestinationPath': str,
            }
        self.reset_info()
        
    # =============================================================================
    # FINDING, LOADING, AND ANALYZING PHOTOS
    # =============================================================================
    def is_pic(self, filepath) -> bool:
        return filepath.lower().endswith(self.pic_exts)
        
    def get_pics(self, location: str) -> list:
        if type(location) is not str:
            return self.alert(f'Expected location as a string, got {type(location)}')
        if not os.path.exists(location):
            return self.alert(f'{location} does not exist!')
        pics = []
        for root, dirs, files in os.walk(location):
            [pics.append(os.path.join(root, f)) for f in files if self.is_pic(f)]
        return pics
        
    def analyze_pics(self, pics: list = None, location: str = None,
                     *args, **kwargs) -> pd.DataFrame:
        
        if pics is None and location is None:
            return self.alert('Unable to analyze pictures: requires list of images or a location')
        
        t0 = time.time()
        self.analyzePicsButton.setEnabled(False)
        self.analyzePicsButton.setText('Analyzing Pictures...')
        
        pics = pics if pics else self.get_pics(location)
        if pics is None:
            return self.alert('Found no pictures to analyze...')
        self.notice(f'Analyzing {len(pics)} pictures...')
        pic_dict = {path: self.get_metadata(path) for path in pics}
        df = pd.DataFrame.from_dict(pic_dict, orient='index')
        df.rename(columns=lambda c: c.split(' ')[-1], inplace=True)
        df.index.rename('Filepath', inplace=True)
        for filepath, info in df.iterrows():
            df.loc[filepath, 'Filename'] = os.path.basename(filepath)
        for field, func in self.metadata_fields.items():
            try:
                col = field.split(' ')[-1]
                df[col] = df[col].astype(func)
            except:
                self.alert(f'Could not convert {field} using {func}')
        df['DateTime'] = df['DateTime'].apply(self.reformat_date)
        df = df if self.pics_df is None else pd.concat([self.pics_df, df])
        df = df[~df.index.duplicated(keep='first')]
        self.pics_df = df.replace({np.nan: None, 'nan': None})
        
        self.notice(f'Analyzed {len(df)} pictures in {time.time()-t0:.2f} seconds')
        
        return df
    
    def get_metadata(self, filepath: str) -> dict:
        metadata = {}
        try:
            if self.is_pic(filepath):
                with open(filepath, 'rb') as f:
                    res = exifread.process_file(f, details=False)
                metadata = {k: str(v) for k, v in res.items() if k in self.metadata_fields}
                return metadata
            else:
                self.alert(f'{filepath} is not a valid picture file: skipping...')
            return metadata
        except Exception as ex:
            self.alert(f'Unable to get image metadata\n\t(Error: {ex})')
            return metadata
        
    def load_image(self, filepath: str):
        im = None
        if filepath.lower().endswith('.cr2'):
            with rawpy.imread(filepath) as raw:
                im = raw.postprocess(no_auto_bright=True)
        return im
    
    def load_thumbnail(self, filepath: str) -> np.ndarray:
        # Get the thumbnail
        thumb = None
        with rawpy.imread(filepath) as raw:
            try:
                thumb = raw.extract_thumb()
            except rawpy.LibRawNoThumbnailError:
                return self.alert(f'No thumbnail found for {filepath}')
            except rawpy.LibRawUnsupportedThumbnailError:
                return self.alert(f'Unsupported thumbnail from {filepath}')
            else:
                if thumb.format == rawpy.ThumbFormat.JPEG:
                    with open('thumb.jpg', 'wb') as f:
                        f.write(thumb.data)
                elif thumb.format == rawpy.ThumbFormat.BITMAP:
                    imageio.imsave('thumb.jpg', thumb.data)

        # Convert to numpy array and remove the temp file
        array = np.array(Image.open('thumb.jpg'))
        os.remove('thumb.jpg')
        return array
        
    def get_pct_dark(self, filepath: str, dark_thresh: int = 50, light_thresh = 150):
        if filepath.lower().endswith('.cr2'):
            im = self.load_thumbnail(filepath)
        else:
            im = self.load_image(filepath)
        if im is None:
            return self.alert(f'Could not load {filepath}')
        npix = im.shape[0]*im.shape[1]
        flat = self.condense_pixels(im)
        num_dark = np.count_nonzero(flat < dark_thresh)
        pct_dark = num_dark / npix
        return pct_dark
        
    # =============================================================================
    # SORTING PHOTOS   
    # =============================================================================
    def sort_pics(self, autodetect: bool = True, *args, **kwargs):
        t0 = time.time()
        num_pics = len(self.pics_df)
        self.notice(f'Sorting {num_pics} pictures...')
        self.sortPicsButton.setEnabled(False)
        self.sortPicsButton.setText('Sorting Pictures...')
        
        # Get list of unique conditions
        settings = ['ExposureTime', 'ExposureTimeFloat', 'ISOSpeedRatings', 'FNumber']
        df = self.pics_df.copy()
        df = df[~df.index.duplicated()]
        df['ExposureTimeFloat'] = df['ExposureTime'].apply(eval)
        
        # Sort out bias frames (min. exposure time) and other frames (unique settings)
        conditions = df.groupby(settings).size().reset_index().rename(columns={0: 'Count'})
        min_exp = df['ExposureTime'].apply(eval).min()
        for i, group in conditions.iterrows():
            mask = ((df['ExposureTime'] == group['ExposureTime']) &
                    (df['ISOSpeedRatings'] == group['ISOSpeedRatings']) &
                    (df['FNumber'] == group['FNumber']))
            if group['ExposureTimeFloat'] == min_exp:
                conditions.loc[i, 'FrameType'] = 'Bias'
                self.pics_df.loc[mask, 'FrameType'] = 'Bias'
            elif group['Count'] == 1:
                conditions.loc[i, 'FrameType'] = 'Other'
                self.pics_df.loc[mask, 'FrameType'] = 'Other'
            else:
                conditions.loc[i, 'FrameType'] = 'Unsorted'
                self.pics_df.loc[mask, 'FrameType'] = 'Unsorted'
                
        # Sort out dark or light and flat frames
        settings = ['ISOSpeedRatings', 'FNumber']
        isos = conditions[conditions['FrameType'] != 'Other']
        isos = isos.groupby(settings).size().reset_index().rename(columns={0: 'Groups'})
        group_num = 0
        for i, group in isos.iterrows():
            mask = ((df['ISOSpeedRatings'] == group['ISOSpeedRatings']) &
                    (df['FNumber'] == group['FNumber']) &
                    (self.pics_df['FrameType'] == 'Unsorted'))
            if group['Groups'] == 3:
                self.pics_df.loc[mask, 'ImageGroup'] = group_num
                times = sorted(df.loc[mask, 'ExposureTimeFloat'].tolist())
                t_min, t_max = float(times[0]), float(times[-1])
                flat_mask = mask & (self.pics_df['ExposureTime'].apply(eval) == t_min)
                other_mask = mask & (self.pics_df['ExposureTime'].apply(eval) == t_max)
                self.pics_df.loc[flat_mask, 'FrameType'] = 'Flat'
                self.pics_df.loc[other_mask, 'FrameType'] = 'Dark or Light'
                group_num += 1
            else:
                self.pics_df.loc[mask, 'FrameType'] = 'Other'
                
        # Distinguish dark and light frames
        for i, info in self.pics_df.iterrows():
            if not info['FrameType'] == 'Dark or Light':
                continue
            pct_dark = self.get_pct_dark(i)
            
            if pct_dark > 0.99:
                self.pics_df.loc[i, 'FrameType'] = 'Dark'
            else:
                self.pics_df.loc[i, 'FrameType'] = 'Light'
                
        # Catch anything else that might have been missed
        self.pics_df.loc[self.pics_df['FrameType'].isna(), 'FrameType'] = 'Unknown'
                
        self.notice(f'Sorted {num_pics} pictures in {time.time()-t0:.2f} seconds')
        
        return self.pics_df
    
    def move_pics(self, copy: bool = False, *args, **kwargs):
        t0 = time.time()
        num_pics = len(self.pics_df)
        num_left = num_pics
        self.notice(f'Moving {num_pics} pictures...')
        self.sortPicsButton.setEnabled(False)
        self.sortPicsButton.setText('Sorting Pictures...')
        
        folder = self.outputFolderEdit.text()
        if not folder or not os.path.exists(folder):
            folder = self.default_save_folder
            
        # Each group of ISO shots with at least 2 shutter speeds is a group
        
        for name in self.pics_df['FrameType'].unique():
            subfolder = os.path.join(folder, name).replace('\\', '/')
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
            mask = (self.pics_df['FrameType'] == name)
            self.pics_df.loc[mask, 'DestinationFolder'] = subfolder
            for filepath, info in self.pics_df[mask].iterrows():
                filename = info['Filename']
                dest_path = os.path.join(subfolder, filename).replace('\\', '/')
                self.pics_df.loc[filepath, 'DestinationPath'] = dest_path
                if copy:
                    shutil.copy(filepath, dest_path)
                else:
                    os.rename(filepath, dest_path)
                num_left -= 1
                self.notice(f'Moving pictures: {num_left}/{num_pics} remaining')
                    
        self.notice(f'Moved {num_pics} pictures in {time.time()-t0:.2f} seconds')
    
    # =============================================================================
    # SAVING AND LOADING DATA
    # =============================================================================
    def save_data(self, data) -> None:
        save_path = os.path.join(self.test_location, 'photo info.pkl')
        with open(save_path, 'wb') as f:
            pickle.dump(data, f)
        self.notice(f'Saved data to {save_path}')
        
    def load_data(self, filepath: str):
        if not os.path.exists(filepath):
            self.alert(f'Unable to load data: {filepath} not found')
            return None
        try:
            with open(filepath, 'rb') as f:
                info = pickle.load(f)
            self.notice(f'Successfully loaded info from {filepath}')
            return info
        except Exception as ex:
            self.alert(f'Unable to load info from {filepath}\n\t(Error {ex})')
    
    # =============================================================================
    # GUI FUNCTIONS
    # =============================================================================
    def show_pic_info(self, dataframe: pd.DataFrame) -> None:
        if type(dataframe) is not pd.DataFrame:
            return self.alert(f'Expected DataFrame, got {type(self.pics_df)}')
        pandas_model = models.PandasModel(dataframe)
        proxy_model = QtCore.QSortFilterProxyModel()
        proxy_model.setSortRole(Qt.EditRole)
        proxy_model.setSourceModel(pandas_model)
        self.fileTable.reset()
        self.fileTable.setModel(proxy_model)
        
    def select_folder(self, window_title: str = 'Select Folder') -> str:
        folder = str(QFileDialog.getExistingDirectory(self, window_title))
        return f'{folder}/' if folder else folder
    
    def select_input_folder(self):
        folder = self.select_folder('Select Input Folder')
        if not folder:
            return
        self.inputFolderEdit.setText(folder)
    
    def select_output_folder(self):
        folder = self.select_folder('Select Output Folder')
        if not folder:
            return
        self.outputFolderEdit.setText(folder)
        
    def sync_output_folder(self, checked: bool):
        if checked:
            self.outputFolderEdit.setText(self.inputFolderEdit.text())
        
    def notice(self, text: str) -> None:
        print(text)
        self.update_left_status(text)
        
    def alert(self, text: str) -> None:
        print(text)
        self.update_right_status(text)
        
    def update_left_status(self, text: str) -> None:
        self.left_status.setText(str(text))
        
    def update_right_status(self, text: str) -> None:
        self.right_status.setText(str(text))

    # =============================================================================
    # HELPER FUNCTIONS
    # =============================================================================
    def reset_info(self):
        columns = [name.split(' ')[-1] for name in self.metadata_fields.keys()]
        self.pics_df = pd.DataFrame(columns = columns)
    
    def reformat_date(self, date_string: str):
        time_obj = datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S')
        return date.strftime(time_obj, '%m/%d/%Y %H:%M:%S')
    
    def condense_pixels(self, frame: np.ndarray) -> np.ndarray:
        if frame.ndim == 3:
            flat = frame.sum(axis=2).ravel()
        else:
            flat = frame.ravel()
        return flat
    
    def analyze_pics_finished(self):
        self.sortPicsButton.setEnabled(len(self.pics_df) > 0)
        self.show_pic_info(self.pics_df)
        self.update_right_status('Finished analyzing pictures')
        self.analyzePicsButton.setEnabled(True)
        self.analyzePicsButton.setText('Analyze Pictures')
    
    def sort_pics_finished(self):
        self.move_pics_thread(copy = False)
        self.show_pic_info(self.pics_df)
        self.update_right_status('Finished sorting pictures')
        self.sortPicsButton.setEnabled(True)
        self.sortPicsButton.setText('Sort Pictures')
        
    def move_pics_finished(self):
        self.show_pic_info(self.pics_df)
        self.update_right_status('Finished moving pictures')
        self.sortPicsButton.setEnabled(True)
        self.sortPicsButton.setText('Sort Pictures')
    
    # =============================================================================
    # EVENTS
    # =============================================================================
    def closeEvent(self, event):
        self.close()
        self.app.quit()
        
    # =============================================================================
    # THREADS
    # =============================================================================
    def analyze_pics_thread(self):
        location = self.inputFolderEdit.text()
        location = location if location else self.test_location
        worker = threading.Worker(self.analyze_pics, location=location)
        worker.signals.finished.connect(self.analyze_pics_finished)
        self.threadpool.start(worker)
        
    def sort_pics_thread(self, autodetect: bool = True):
        worker = threading.Worker(self.sort_pics, autodetect)
        worker.signals.finished.connect(self.sort_pics_finished)
        worker.signals.message.connect(self.update_left_status)
        self.threadpool.start(worker)
        
    def move_pics_thread(self, copy: bool = False):
        worker = threading.Worker(self.move_pics, copy)
        worker.signals.finished.connect(self.move_pics_finished)
        worker.signals.message.connect(self.update_left_status)
        self.threadpool.start(worker)
        
    # =============================================================================
    # TESTING
    # =============================================================================
    def test(self):
        self.load_thumbnail(self.test_pic)
        # pics = self.get_pics(self.test_location)
        # df = self.analyze_pics(pics)
        # self.sort_pics_thread(autodetect = True)
        
# =============================================================================
# RUNNING
# =============================================================================
if __name__ == '__main__':
    sorter = AstroSorter(None)
    app.exec_()
        