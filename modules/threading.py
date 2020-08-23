# -*- coding: utf-8 -*-

import time
import traceback, sys
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSlot, pyqtSignal

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    send = pyqtSignal(object)
    message = pyqtSignal(str)
    result = pyqtSignal(object)
    progress = pyqtSignal(float)
  
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
        self.kwargs['message'] = self.signals.message
        self.kwargs['progress_callback'] = self.signals.progress
        
    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()