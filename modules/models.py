# -*- coding: utf-8 -*-

from PyQt5.QtCore import QAbstractTableModel, Qt

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
        
    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return
        if role == Qt.DisplayRole:
            val = self._data.iloc[index.row(), index.column()]
            val = f'{val:.1f}' if type(val) is float else val
            return str(val)
        if role == Qt.EditRole:
            try:
                return eval(self._data.iloc[index.row(), index.column()])
            except:
                return str(self._data.iloc[index.row(), index.column()])
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return None
    
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
    
