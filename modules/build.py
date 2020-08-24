# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QHeaderView, QLabel, QSizePolicy
from PyQt5.QtCore import Qt

from . import models

def menu(self):
    self.menuExit.triggered.connect(self.closeEvent)

def buttons(self):
    self.analyzePicsButton.clicked.connect(self.analyze_pics_thread)
    self.sortPicsButton.clicked.connect(self.sort_pics_thread)
    
    self.openInputFolderButton.clicked.connect(self.open_input_folder)
    self.openOutputFolderButton.clicked.connect(self.open_output_folder)
    
    self.selectInputFolderButton.clicked.connect(self.select_input_folder)
    self.selectOutputFolderButton.clicked.connect(self.select_output_folder)

def tables(self):
    fill = QHeaderView.ResizeToContents
    self.fileTable.horizontalHeader().setSectionResizeMode(fill)
    self.fileTable.horizontalHeader().setMinimumHeight(32)
    
def checkboxes(self):
    self.useInputFolderCheckbox.stateChanged.connect(self.sync_output_folder)
    
def line_edits(self):
    self.inputFolderEdit.textChanged.connect(self.sync_output_folder)
    self.inputFolderEdit.textChanged.connect(self.toggle_folder_buttons)
    self.outputFolderEdit.textChanged.connect(self.toggle_folder_buttons)
    
def statusbar(self):
    self.left_status = QLabel()
    self.right_status = QLabel()
    
    for s in [self.left_status, self.right_status]:
        s.setStyleSheet('''
            font: 11pt "Bahnschrift SemiLight"; 
            margin-bottom: 3px;
            margin-top: 3px;
            margin-left: 0px; 
            margin-right: 0px;
            ''')
        s.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        s.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        
    bar = self.statusBar()
    bar.addWidget(self.left_status)
    bar.addPermanentWidget(self.right_status)

def core(self):
    menu(self)
    buttons(self)  
    tables(self)
    checkboxes(self)
    line_edits(self)
    statusbar(self)