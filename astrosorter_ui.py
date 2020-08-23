# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ElliotYoung\Google Drive\Code\Github\AstroSorter\gui\astrosorter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(1156, 892)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        mainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 35, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        mainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(True)
        mainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("/*                                                                All Items                                                                                */    \n"
"* {\n"
"    font: 11pt \"Bahnschrift SemiLight\";\n"
"    color: white;\n"
"    background-color: rgb(25, 35, 45);\n"
"}\n"
"/*                                                                QPushbutton                                                                        */    \n"
"#mainLayout > QPushButton {\n"
"    font: 11pt \"Bahnschrift SemiBold\";\n"
"    background: none;\n"
"    border: 2px solid rgba(80, 95, 105, 150);\n"
"     border-radius: 2px;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"#mainLayout > #rectButton:hover:!disabled {\n"
"    padding-bottom: 7px;\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"}\n"
"#directoryButton, #userButton, #sampleButton {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"#directoryButton:hover:!disabled, #userButton:hover:!disabled, #sampleButton:hover:!disabled {\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    padding-bottom: 7px;\n"
"} \n"
"QPushButton {\n"
"    font: 11pt \"Bahnschrift SemiBold\";\n"
"    background-color: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgb(68, 86, 100), \n"
"        stop: 0.0 rgb(44, 55, 64));\n"
"    border: 1px solid rgba(80, 95, 105, 255);\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton:hover:!disabled {\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgb(68, 86, 100), \n"
"        stop: 0.0 rgb(44, 55, 64));\n"
"    padding-bottom: 7px;\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"}\n"
"#mainLayout > QPushButton:hover:!disabled {\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    padding: 5px 5px 7px 5px;\n"
"}\n"
"QPushButton::disabled {\n"
"    color: rgb(68, 86, 100);\n"
"    background-color: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgb(34, 43, 53), \n"
"        stop: 0.0 rgb(44, 55, 64));\n"
"}\n"
"#startstopwatchButton {\n"
"    color: rgb(155, 229, 100);\n"
"}\n"
"#resetstopwatchButton::enabled {\n"
"    color: rgb(228, 88, 101);\n"
"}\n"
"#starttimerButton::enabled {\n"
"    color: rgb(155, 229, 100);\n"
"}\n"
"#starttimerButton::disabled:checked {\n"
"    color: rgb(228, 88, 101);\n"
"}\n"
"#resettimerButton::enabled {\n"
"    color: rgb(228, 88, 101);\n"
"}\n"
"/*                                                                QLabel                                                                                    */    \n"
"#drawCanvas {\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"#gammaValue_Label, #blacklevelValue_Label, #gainValue_Label {\n"
"    color: rgb(155, 229, 100);\n"
"}\n"
"#mainLayout > #zoomvalueLabel {\n"
"    padding-left: 0px;\n"
"    color: rgb(155, 229, 100);\n"
"}\n"
"#mainLayout > #zoomtextLabel {\n"
"    padding-right: 0px;\n"
"}\n"
"#mainLayout > QLabel {\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"}\n"
"#sampleLabel, #userLabel {\n"
"    margin-right: 0px;\n"
"    margin-left: -6px;\n"
"    padding-right: 0px;\n"
"    padding-left: 0px;\n"
"}\n"
"QLabel:disabled {\n"
"    color: rgb(68, 86, 100);\n"
"}\n"
"/*                                                                QFrame                                                                                */    \n"
"QFrame[frameShape=\"4\"] { /* horizontal line */\n"
"    color: rgb(62, 152, 193);\n"
"}\n"
"QFrame[frameShape=\"5\"] { /* vertical line */\n"
"    color: rgb(62, 152, 193);\n"
"}\n"
"/*                                                                QTabBar                                                                                */    \n"
"QTabBar::tab {\n"
"    font: 11pt \"Bahnschrift SemiBold\";\n"
"    color: white;\n"
"    border: 1px solid rgb(68, 86, 100);\n"
"    border-bottom-width: 0px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    padding: 2px 10px 5px 10px;\n"
"    margin-right: 3px;\n"
"    background: qlineargradient(spread:pad, \n"
"        x1:1, y1:1, \n"
"        x2:1, y2:0.585227, \n"
"        stop:0 rgba(44, 55, 64, 255), \n"
"        stop:1 rgba(80, 95, 105, 255));\n"
"}\n"
"QTabBar::tab:hover {\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    background: qlineargradient(x1: 0.5, y1: 0.86,\n"
"        x2: 0.5, y2: 1.0,\n"
"         stop: 0.0 rgb(50, 65, 75),\n"
"        stop: 1.0  rgb(0, 167, 209));\n"
"    background: qlineargradient(spread:pad, x1:1, y1:0.977273, x2:1, y2:0, stop:0 rgba(0, 167, 209, 156), stop:0.198864 rgba(80, 95, 105, 255));\n"
"    padding: 2px 10px 6px 10px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    border: none;\n"
"    background: rgb(68, 86, 100);\n"
"    border-bottom: 1px solid rgb(0, 167, 209);\n"
"    border-top: 1px solid rgb(68, 86, 100);\n"
"    padding: 2px 11px 5px 11px;\n"
"    background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.83, stop:0 rgba(0, 167, 209, 255), stop:1 rgba(80, 95, 105, 255));\n"
"}\n"
"QTabBar::tab:selected:hover {\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.779, stop:0 rgba(0, 167, 209, 255), stop:1 rgba(80, 95, 105, 255));\n"
"    padding: 2px 10px 7px 10px;\n"
"}\n"
"QTabBar::scroller {\n"
"    width: 16px;\n"
"}\n"
"QTabBar QToolButton {\n"
"    background-color: rgba(25, 35, 45, 220);\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"}\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(:/icons/icons/left button.png);\n"
"}\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"    image: url(:/icons/icons/left button hover.png);\n"
"}\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"    image: url(:/icons/icons/left button gray.png)\n"
"}\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(:/icons/icons/right button.png);\n"
"}\n"
"QTabBar QToolButton::right-arrow:hover {\n"
"    image: url(:/icons/icons/right button hover.png);\n"
"}\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"    image: url(:/icons/icons/right button gray.png)\n"
"}\n"
"QTabBar::close-button {\n"
"    image: url(:/icons/icons/close tab icon.png);\n"
"    subcontrol-position: right;\n"
"}\n"
"QTabBar::close-button:hover {\n"
"    image: url(:/icons/icons/close tab hover icon.png);\n"
"}\n"
"/*                                                                QTabWidget                                                                        */    \n"
"QTabWidget::pane {\n"
"    border: 1px solid rgb(80, 95, 105);\n"
"    border-radius: 3px;\n"
"    border-top-left-radius: 0px;\n"
"}\n"
"QTabWidget::pane:hover {\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"}\n"
"/*                                                                QStatusBar                                                                            */    \n"
"QStatusBar::item {\n"
"    border: 0px solid black;\n"
"}\n"
"/*                                                                QScrollBar                                                                            */\n"
"QScrollBar {\n"
"    background: transparent;\n"
"    border: 1px solid rgba(111, 124, 132, 150);\n"
"    border-radius: 5px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: 3px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    margin-top: 13px;\n"
"    margin-bottom: 13px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    margin-left: 13px;\n"
"    margin-right: 13px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top;\n"
"    background: none;\n"
"    border-radius: 3px;\n"
"    height: 13px;\n"
"    top: -13px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom;\n"
"    background: none;\n"
"    border-radius: 3px;\n"
"    height: 13px;\n"
"    bottom: -13px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: left;\n"
"    background: none;\n"
"    border-radius: 3px;\n"
"    width: 13px;\n"
"    left: -13px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: right;\n"
"    background: none;\n"
"    border-radius: 3px;\n"
"    width: 13px;\n"
"    right: -13px;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top;\n"
"    image: url(:/icons/icons/up button gray.png);\n"
"    width: 12px;\n"
"}\n"
"QScrollBar::up-arrow:vertical:hover {\n"
"    image: url(:/icons/icons/up button hover.png);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom;\n"
"    image: url(:/icons/icons/down button gray.png);\n"
"    width: 12px;\n"
"}\n"
"QScrollBar::down-arrow:vertical:hover {\n"
"    image: url(:/icons/icons/down button hover.png);\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: left;\n"
"    image: url(:/icons/icons/left button gray.png);\n"
"    height: 12px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:hover {\n"
"    image: url(:/icons/icons/left button hover.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: right;\n"
"    image: url(:/icons/icons/right button gray.png);\n"
"    height: 12px;\n"
"}\n"
"QScrollBar::right-arrow:horizontal:hover {\n"
"    image: url(:/icons/icons/right button hover.png);\n"
"}\n"
"QScrollBar::handle {\n"
"    background-color: rgba(80, 95, 105, 150);\n"
"    border: 1px solid rgb(111, 124, 132);\n"
"    border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:hover {\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    background-color: rgb(0, 167, 209);\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"/*                                                                QSlider                                                                                    */    \n"
"QSlider::groove {\n"
"    height: 6px;\n"
"    border: 0px solid rgb(25, 35, 45);\n"
"    background: rgb(175, 182, 186);\n"
"    border-radius: 2px;\n"
"}\n"
"QSlider::handle {\n"
"    width: 12px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(155, 229, 100);\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"}\n"
"QSlider::handle:hover {\n"
"    background: rgb(0, 167, 209);\n"
"}\n"
"QSlider::handle:disabled {\n"
"    background: rgb(175, 182, 186);\n"
"    border: 1px solid rgb(111, 124, 132);\n"
"}\n"
"/*                                                                QCheckBox                                                                            */\n"
"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: 1px solid white;\n"
"    border-radius: 2px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background: rgb(228, 88, 101);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: rgb(155, 229, 100);\n"
"}\n"
"QCheckBox::disabled {\n"
"    color: rgb(68, 86, 100);\n"
"}\n"
"QCheckBox::indicator:disabled {\n"
"    background: rgb(68, 86, 100);\n"
"    border: 1px solid rgb(144, 149, 153);\n"
"}\n"
"/*                                                                QMenuBar                                                                            */    \n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"}\n"
"QMenuBar::item:selected {\n"
"    background-color: rgb(80, 95, 105);\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"/*                                                                QTextEdit                                                                            */    \n"
"QTextEdit {\n"
"    background: rgb(44, 55, 64);\n"
"    border: 1px solid rgb(62, 152, 193);\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"}\n"
"/*                                                                QLineEdit                                                                                */    \n"
"QLineEdit {\n"
"    color: rgb(155, 229, 100);\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgba(68, 86, 100, 235), \n"
"        stop: 0.0 rgb(44, 55, 64));\n"
"    padding: 4px 6px 4px 6px;\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    border-radius: 3px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgb(68, 86, 100), \n"
"        stop: 0.2 rgb(44, 55, 64));\n"
"}\n"
"/*                                                                QSpinBox                                                                                */\n"
"QSpinBox {\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgba(68, 86, 100, 235), \n"
"        stop: 0.0 rgb(44, 55, 64));\n"
"    color: rgb(155, 229, 100);\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    border-radius: 3px;\n"
"    padding: 4px 6px 4px 6px;\n"
"}\n"
"QSpinBox::hover {\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgb(68, 86, 100), \n"
"        stop: 0.2 rgb(44, 55, 64));\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    top: 4px;\n"
"    right: 3px;\n"
"    width: 16px;\n"
"    height: 10px;\n"
"    border-image: url(:/icons/icons/up button.png);\n"
"    border-width: 1px;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    bottom: 4px;\n"
"    right: 3px;\n"
"    width: 16px;\n"
"    height: 10px;\n"
"    border-image: url(:/icons/icons/down button.png);\n"
"    border-width: 1px;\n"
"}\n"
"QSpinBox::down-button:hover {\n"
"    border-image: url(:/icons/icons/down button hover.png)\n"
"}\n"
"QSpinBox::up-button:hover {\n"
"    border-image: url(:/icons/icons/up button hover.png)\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"    background: rgb(44, 55, 64);\n"
"    border-radius: 3px;\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"    background: rgb(44, 55, 64);\n"
"    border-radius: 3px;\n"
"}\n"
"/*                                                                QDoubleSpinBox                                                                    */\n"
"QDoubleSpinBox {\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgba(68, 86, 100, 235), \n"
"        stop: 0.0 rgb(44, 55, 64));\n"
"    color: rgb(155, 229, 100);\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    border-radius: 3px;\n"
"    padding: 4px 6px 4px 6px;\n"
"}\n"
"QDoubleSpinBox::hover {\n"
"    background: qlineargradient(x1: 0.5, y1: 1.0, \n"
"        x2: 0.5, y2: 0.0,\n"
"        stop: 1.0 rgb(68, 86, 100), \n"
"        stop: 0.2 rgb(44, 55, 64));\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    top: 4px;\n"
"    right: 3px;\n"
"    width: 16px;\n"
"    height: 10px;\n"
"    border-image: url(:/icons/icons/up button.png);\n"
"    border-width: 1px;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    bottom: 4px;\n"
"    right: 3px;\n"
"    width: 16px;\n"
"    height: 10px;\n"
"    border-image: url(:/icons/icons/down button.png);\n"
"    border-width: 1px;\n"
"}\n"
"QDoubleSpinBox::down-button:hover {\n"
"    border-image: url(:/icons/icons/down button hover.png)\n"
"}\n"
"QDoubleSpinBox::up-button:hover {\n"
"    border-image: url(:/icons/icons/up button hover.png)\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background: rgb(44, 55, 64);\n"
"    border-radius: 3px;\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background: rgb(44, 55, 64);\n"
"    border-radius: 3px;\n"
"}\n"
"QDoubleSpinBox::disabled {\n"
"    color: rgb(68, 86, 100);\n"
"}\n"
"QDoubleSpinBox::up-button:disabled {\n"
"    border-image: url(:/icons/icons/up button gray.png);\n"
"}\n"
"QDoubleSpinBox::down-button:disabled {\n"
"    border-image: url(:/icons/icons/down button gray.png);\n"
"}\n"
"/*                                                                QMenuBar                                                                            */\n"
"QMenuBar {\n"
"    background: rgb(68, 86, 100);\n"
"    border-radius: 0px;\n"
"}\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 12px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QMenuBar::item:selected {\n"
"     background: rgb(0, 167, 209);\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"/*                                                                QMenu                                                                                    */\n"
"QMenuBar > QMenu {\n"
"    background: rgb(68, 86, 100);\n"
"}\n"
"QMenuBar > QMenu::item {\n"
"    border: 1px solid transparent;\n"
"    margin-top: 0px;\n"
"    margin-bottom: 0px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    padding-top: 4px;\n"
"    padding-bottom: 4px;\n"
"}\n"
"QMenuBar > QMenu::item:selected {\n"
"     background: rgb(0, 167, 209);\n"
"}\n"
"QMenuBar > QMenu::separator {\n"
"    background: rgb(0, 167, 209);\n"
"    height: 1px;\n"
"}\n"
"/*                                                                QLCDNumber, QGroupbox                                                    */    \n"
"QLCDNumber, QGroupBox {\n"
"    border: 1px solid rgb(80, 95, 105);\n"
"    border-radius: 3px;\n"
"}\n"
"QGroupBox {\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"    border: none;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    margin: 0px;\n"
"    padding: 15px;\n"
"    top: -15px;\n"
"}\n"
"#timerScreen:disabled {\n"
"    color: rgb(228, 88, 101);\n"
"}\n"
"/*                                                                QToolTip                                                                                */    \n"
"QToolTip {\n"
"    background: rgb(111, 124, 132);\n"
"    text: white;\n"
"    border: 1px solid rgb(80, 95, 105);\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    opacity: 200;\n"
"}\n"
"/*                                                                PlotItems                                                                                */    \n"
"plotItem {\n"
"    color: red;\n"
"}\n"
"/*                                                               QStatusBar                                                                             */\n"
"QStatusBar {\n"
"    border-top: 1px solid rgb(80, 95, 105);\n"
"}\n"
"/*                                                                QSizeGrip                                                                                */    \n"
"QSizeGrip {\n"
"    image: url(:/icons/icons/sizegrip.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"/*                                                                QTableView                                                                            */\n"
"QHeaderView::section {\n"
"    background:  rgba(80, 95, 105, 150);\n"
"    border: none;\n"
"}\n"
"QHeaderView::down-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center top;\n"
"    image: url(:/icons/icons/down button hover.png);\n"
"    height: 16px;\n"
"    width: 16px;\n"
"    top: -4px;\n"
"}\n"
"QHeaderView::up-arrow {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center top;\n"
"    image: url(:/icons/icons/up button hover.png);\n"
"    height: 16px;\n"
"    width: 16px;\n"
"    top: -4px;\n"
"}\n"
"QTableView {\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    gridline-color: rgb(111, 124, 132);\n"
"    selection-background-color: rgb(0, 167, 209);\n"
"}\n"
"/*                                                                QGroupBox                                                                            */\n"
"QGroupBox {\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(0, 167, 209);\n"
"    font-size: 18px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left top;\n"
"    left: 3px;\n"
"}")
        mainWindow.setIconSize(QtCore.QSize(24, 24))
        mainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        mainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        mainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.mainLayout = QtWidgets.QWidget(mainWindow)
        self.mainLayout.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mainLayout.setFont(font)
        self.mainLayout.setMouseTracking(True)
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout = QtWidgets.QGridLayout(self.mainLayout)
        self.gridLayout.setContentsMargins(2, 2, 2, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.fileDisplayWidget = QtWidgets.QWidget(self.mainLayout)
        self.fileDisplayWidget.setObjectName("fileDisplayWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.fileDisplayWidget)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addWidget(self.fileDisplayWidget, 1, 0, 1, 2)
        self.loadWidget = QtWidgets.QWidget(self.mainLayout)
        self.loadWidget.setObjectName("loadWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.loadWidget)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 0)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.selectFoldersGroupBox = QtWidgets.QGroupBox(self.loadWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selectFoldersGroupBox.setFont(font)
        self.selectFoldersGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.selectFoldersGroupBox.setObjectName("selectFoldersGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.selectFoldersGroupBox)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.outputFolderEdit = QtWidgets.QLineEdit(self.selectFoldersGroupBox)
        self.outputFolderEdit.setFrame(True)
        self.outputFolderEdit.setReadOnly(False)
        self.outputFolderEdit.setObjectName("outputFolderEdit")
        self.gridLayout_4.addWidget(self.outputFolderEdit, 1, 2, 1, 1)
        self.selectOutputFolderButton = QtWidgets.QPushButton(self.selectFoldersGroupBox)
        self.selectOutputFolderButton.setObjectName("selectOutputFolderButton")
        self.gridLayout_4.addWidget(self.selectOutputFolderButton, 1, 0, 1, 1)
        self.useInputFolderCheckbox = QtWidgets.QCheckBox(self.selectFoldersGroupBox)
        self.useInputFolderCheckbox.setEnabled(True)
        self.useInputFolderCheckbox.setChecked(True)
        self.useInputFolderCheckbox.setObjectName("useInputFolderCheckbox")
        self.gridLayout_4.addWidget(self.useInputFolderCheckbox, 1, 1, 1, 1)
        self.inputFolderEdit = QtWidgets.QLineEdit(self.selectFoldersGroupBox)
        self.inputFolderEdit.setFrame(True)
        self.inputFolderEdit.setReadOnly(False)
        self.inputFolderEdit.setObjectName("inputFolderEdit")
        self.gridLayout_4.addWidget(self.inputFolderEdit, 0, 2, 1, 1)
        self.selectInputFolderButton = QtWidgets.QPushButton(self.selectFoldersGroupBox)
        self.selectInputFolderButton.setObjectName("selectInputFolderButton")
        self.gridLayout_4.addWidget(self.selectInputFolderButton, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.selectFoldersGroupBox, 0, 0, 1, 2)
        self.processPicsGroupBox = QtWidgets.QGroupBox(self.loadWidget)
        self.processPicsGroupBox.setObjectName("processPicsGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.processPicsGroupBox)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.analyzePicsButton = QtWidgets.QPushButton(self.processPicsGroupBox)
        self.analyzePicsButton.setObjectName("analyzePicsButton")
        self.gridLayout_5.addWidget(self.analyzePicsButton, 0, 0, 1, 1)
        self.sortPicsButton = QtWidgets.QPushButton(self.processPicsGroupBox)
        self.sortPicsButton.setEnabled(False)
        self.sortPicsButton.setObjectName("sortPicsButton")
        self.gridLayout_5.addWidget(self.sortPicsButton, 0, 1, 1, 1)
        self.movePicsButton = QtWidgets.QPushButton(self.processPicsGroupBox)
        self.movePicsButton.setEnabled(False)
        self.movePicsButton.setObjectName("movePicsButton")
        self.gridLayout_5.addWidget(self.movePicsButton, 0, 2, 1, 1)
        self.fileTable = QtWidgets.QTableView(self.processPicsGroupBox)
        self.fileTable.setStyleSheet("border: none;")
        self.fileTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fileTable.setProperty("showDropIndicator", False)
        self.fileTable.setAlternatingRowColors(False)
        self.fileTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.fileTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fileTable.setSortingEnabled(True)
        self.fileTable.setCornerButtonEnabled(False)
        self.fileTable.setObjectName("fileTable")
        self.fileTable.horizontalHeader().setHighlightSections(False)
        self.fileTable.horizontalHeader().setStretchLastSection(True)
        self.fileTable.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.fileTable, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.processPicsGroupBox, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.loadWidget, 0, 0, 1, 2)
        mainWindow.setCentralWidget(self.mainLayout)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1156, 29))
        self.menubar.setMaximumSize(QtCore.QSize(16777215, 1111111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(68, 86, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menubar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.menuExit = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.menuExit.setFont(font)
        self.menuExit.setObjectName("menuExit")
        self.action_Capture = QtWidgets.QAction(mainWindow)
        self.action_Capture.setObjectName("action_Capture")
        self.menuColormap = QtWidgets.QAction(mainWindow)
        self.menuColormap.setObjectName("menuColormap")
        self.menuOpen = QtWidgets.QAction(mainWindow)
        self.menuOpen.setObjectName("menuOpen")
        self.action_Record = QtWidgets.QAction(mainWindow)
        self.action_Record.setObjectName("action_Record")
        self.action_FFT = QtWidgets.QAction(mainWindow)
        self.action_FFT.setObjectName("action_FFT")
        self.action_Replot = QtWidgets.QAction(mainWindow)
        self.action_Replot.setObjectName("action_Replot")
        self.action_Add_rectangle = QtWidgets.QAction(mainWindow)
        self.action_Add_rectangle.setObjectName("action_Add_rectangle")
        self.action_Colormap_2 = QtWidgets.QAction(mainWindow)
        self.action_Colormap_2.setObjectName("action_Colormap_2")
        self.menuExposure = QtWidgets.QAction(mainWindow)
        self.menuExposure.setObjectName("menuExposure")
        self.menuSave = QtWidgets.QAction(mainWindow)
        self.menuSave.setObjectName("menuSave")
        self.action_50_shades_of_gray = QtWidgets.QAction(mainWindow)
        self.action_50_shades_of_gray.setObjectName("action_50_shades_of_gray")
        self.action_Connect = QtWidgets.QAction(mainWindow)
        self.action_Connect.setObjectName("action_Connect")
        self.menuConnect = QtWidgets.QAction(mainWindow)
        self.menuConnect.setObjectName("menuConnect")
        self.menuDefault = QtWidgets.QAction(mainWindow)
        self.menuDefault.setObjectName("menuDefault")
        self.connectButton = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(11)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.changesourceButton = QtWidgets.QAction(mainWindow)
        self.changesourceButton.setObjectName("changesourceButton")
        self.menuChangeDirectory = QtWidgets.QAction(mainWindow)
        self.menuChangeDirectory.setObjectName("menuChangeDirectory")
        self.actionSimulate_RHEED = QtWidgets.QAction(mainWindow)
        self.actionSimulate_RHEED.setObjectName("actionSimulate_RHEED")
        self.menuFile.addAction(self.menuExit)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.selectInputFolderButton, self.inputFolderEdit)
        mainWindow.setTabOrder(self.inputFolderEdit, self.selectOutputFolderButton)
        mainWindow.setTabOrder(self.selectOutputFolderButton, self.useInputFolderCheckbox)
        mainWindow.setTabOrder(self.useInputFolderCheckbox, self.outputFolderEdit)
        mainWindow.setTabOrder(self.outputFolderEdit, self.analyzePicsButton)
        mainWindow.setTabOrder(self.analyzePicsButton, self.sortPicsButton)
        mainWindow.setTabOrder(self.sortPicsButton, self.fileTable)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "AstroSorter"))
        self.selectFoldersGroupBox.setTitle(_translate("mainWindow", "Select Folders"))
        self.selectOutputFolderButton.setText(_translate("mainWindow", "Select Output Folder"))
        self.useInputFolderCheckbox.setText(_translate("mainWindow", "Use input folder"))
        self.selectInputFolderButton.setText(_translate("mainWindow", "Select Input Folder"))
        self.processPicsGroupBox.setTitle(_translate("mainWindow", "Process Pictures"))
        self.analyzePicsButton.setText(_translate("mainWindow", "Analyze Pictures"))
        self.sortPicsButton.setText(_translate("mainWindow", "Sort Pictures"))
        self.movePicsButton.setText(_translate("mainWindow", "Move Pictures"))
        self.menuFile.setTitle(_translate("mainWindow", "&File"))
        self.menuExit.setText(_translate("mainWindow", "&Exit"))
        self.action_Capture.setText(_translate("mainWindow", "&Capture"))
        self.menuColormap.setText(_translate("mainWindow", "&Zoom"))
        self.menuOpen.setText(_translate("mainWindow", "Open"))
        self.action_Record.setText(_translate("mainWindow", "&Record"))
        self.action_FFT.setText(_translate("mainWindow", "&FFT"))
        self.action_Replot.setText(_translate("mainWindow", "&Replot"))
        self.action_Add_rectangle.setText(_translate("mainWindow", "&Add rectangle"))
        self.action_Colormap_2.setText(_translate("mainWindow", "&Colormap"))
        self.menuExposure.setText(_translate("mainWindow", "&Colormap"))
        self.menuSave.setText(_translate("mainWindow", "&Save"))
        self.action_50_shades_of_gray.setText(_translate("mainWindow", "&50 shades of gray"))
        self.action_Connect.setText(_translate("mainWindow", "&Connect"))
        self.menuConnect.setText(_translate("mainWindow", "&Connect"))
        self.menuDefault.setText(_translate("mainWindow", "&Default"))
        self.connectButton.setText(_translate("mainWindow", "&Connect"))
        self.changesourceButton.setText(_translate("mainWindow", "&Change Source"))
        self.changesourceButton.setShortcut(_translate("mainWindow", "Ctrl+Shift+S"))
        self.menuChangeDirectory.setText(_translate("mainWindow", "Change Base Directory"))
        self.actionSimulate_RHEED.setText(_translate("mainWindow", "Simulate RHEED"))

from . import resources_rc
