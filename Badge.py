# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'badge.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(685, 564)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 661, 491))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_UART = QtGui.QWidget()
        self.tab_UART.setObjectName(_fromUtf8("tab_UART"))
        self.comboBox_Port = QtGui.QComboBox(self.tab_UART)
        self.comboBox_Port.setGeometry(QtCore.QRect(10, 20, 191, 27))
        self.comboBox_Port.setObjectName(_fromUtf8("comboBox_Port"))
        self.comboBox_BaudRate = QtGui.QComboBox(self.tab_UART)
        self.comboBox_BaudRate.setGeometry(QtCore.QRect(210, 20, 171, 27))
        self.comboBox_BaudRate.setObjectName(_fromUtf8("comboBox_BaudRate"))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.comboBox_BaudRate.addItem(_fromUtf8(""))
        self.pushButton_AutoDetect = QtGui.QPushButton(self.tab_UART)
        self.pushButton_AutoDetect.setGeometry(QtCore.QRect(390, 20, 131, 27))
        self.pushButton_AutoDetect.setObjectName(_fromUtf8("pushButton_AutoDetect"))
        self.pushButton_Connect = QtGui.QPushButton(self.tab_UART)
        self.pushButton_Connect.setGeometry(QtCore.QRect(530, 20, 111, 27))
        self.pushButton_Connect.setObjectName(_fromUtf8("pushButton_Connect"))
        self.line = QtGui.QFrame(self.tab_UART)
        self.line.setGeometry(QtCore.QRect(10, 60, 641, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit_UartInput = QtGui.QLineEdit(self.tab_UART)
        self.lineEdit_UartInput.setGeometry(QtCore.QRect(10, 420, 491, 27))
        self.lineEdit_UartInput.setObjectName(_fromUtf8("lineEdit_UartInput"))
        self.comboBox_Ender = QtGui.QComboBox(self.tab_UART)
        self.comboBox_Ender.setGeometry(QtCore.QRect(510, 420, 131, 27))
        self.comboBox_Ender.setObjectName(_fromUtf8("comboBox_Ender"))
        self.comboBox_Ender.addItem(_fromUtf8(""))
        self.comboBox_Ender.addItem(_fromUtf8(""))
        self.comboBox_Ender.addItem(_fromUtf8(""))
        self.comboBox_Ender.addItem(_fromUtf8(""))
        self.textEdit_UartConsole = QtGui.QTextEdit(self.tab_UART)
        self.textEdit_UartConsole.setGeometry(QtCore.QRect(10, 80, 631, 331))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.textEdit_UartConsole.setPalette(palette)
        self.textEdit_UartConsole.setReadOnly(True)
        self.textEdit_UartConsole.setObjectName(_fromUtf8("textEdit_UartConsole"))
        self.tabWidget.addTab(self.tab_UART, _fromUtf8(""))
        self.tab_I2C = QtGui.QWidget()
        self.tab_I2C.setObjectName(_fromUtf8("tab_I2C"))
        self.tabWidget.addTab(self.tab_I2C, _fromUtf8(""))
        self.tab_SPI = QtGui.QWidget()
        self.tab_SPI.setObjectName(_fromUtf8("tab_SPI"))
        self.tabWidget.addTab(self.tab_SPI, _fromUtf8(""))
        self.tab_GPIO = QtGui.QWidget()
        self.tab_GPIO.setObjectName(_fromUtf8("tab_GPIO"))
        self.checkBox_d0 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d0.setGeometry(QtCore.QRect(30, 81, 71, 31))
        self.checkBox_d0.setObjectName(_fromUtf8("checkBox_d0"))
        self.comboBox_d0 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d0.setGeometry(QtCore.QRect(110, 80, 131, 27))
        self.comboBox_d0.setObjectName(_fromUtf8("comboBox_d0"))
        self.comboBox_d0.addItem(_fromUtf8(""))
        self.comboBox_d0.addItem(_fromUtf8(""))
        self.checkBox_d1 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d1.setGeometry(QtCore.QRect(30, 171, 71, 31))
        self.checkBox_d1.setObjectName(_fromUtf8("checkBox_d1"))
        self.comboBox_d1 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d1.setGeometry(QtCore.QRect(110, 170, 131, 27))
        self.comboBox_d1.setObjectName(_fromUtf8("comboBox_d1"))
        self.comboBox_d1.addItem(_fromUtf8(""))
        self.comboBox_d1.addItem(_fromUtf8(""))
        self.checkBox_d2 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d2.setGeometry(QtCore.QRect(30, 261, 71, 31))
        self.checkBox_d2.setObjectName(_fromUtf8("checkBox_d2"))
        self.comboBox_d2 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d2.setGeometry(QtCore.QRect(110, 260, 131, 27))
        self.comboBox_d2.setObjectName(_fromUtf8("comboBox_d2"))
        self.comboBox_d2.addItem(_fromUtf8(""))
        self.comboBox_d2.addItem(_fromUtf8(""))
        self.comboBox_d3 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d3.setGeometry(QtCore.QRect(110, 350, 131, 27))
        self.comboBox_d3.setObjectName(_fromUtf8("comboBox_d3"))
        self.comboBox_d3.addItem(_fromUtf8(""))
        self.comboBox_d3.addItem(_fromUtf8(""))
        self.checkBox_d3 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d3.setGeometry(QtCore.QRect(30, 350, 71, 31))
        self.checkBox_d3.setObjectName(_fromUtf8("checkBox_d3"))
        self.comboBox_d5 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d5.setGeometry(QtCore.QRect(470, 170, 131, 27))
        self.comboBox_d5.setObjectName(_fromUtf8("comboBox_d5"))
        self.comboBox_d5.addItem(_fromUtf8(""))
        self.comboBox_d5.addItem(_fromUtf8(""))
        self.comboBox_d7 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d7.setGeometry(QtCore.QRect(470, 350, 131, 27))
        self.comboBox_d7.setObjectName(_fromUtf8("comboBox_d7"))
        self.comboBox_d7.addItem(_fromUtf8(""))
        self.comboBox_d7.addItem(_fromUtf8(""))
        self.checkBox_d4 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d4.setGeometry(QtCore.QRect(390, 81, 71, 31))
        self.checkBox_d4.setObjectName(_fromUtf8("checkBox_d4"))
        self.checkBox_d6 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d6.setGeometry(QtCore.QRect(390, 261, 71, 31))
        self.checkBox_d6.setObjectName(_fromUtf8("checkBox_d6"))
        self.comboBox_d4 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d4.setGeometry(QtCore.QRect(470, 80, 131, 27))
        self.comboBox_d4.setObjectName(_fromUtf8("comboBox_d4"))
        self.comboBox_d4.addItem(_fromUtf8(""))
        self.comboBox_d4.addItem(_fromUtf8(""))
        self.checkBox_d5 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d5.setGeometry(QtCore.QRect(390, 171, 71, 31))
        self.checkBox_d5.setObjectName(_fromUtf8("checkBox_d5"))
        self.checkBox_d7 = QtGui.QCheckBox(self.tab_GPIO)
        self.checkBox_d7.setGeometry(QtCore.QRect(390, 350, 71, 31))
        self.checkBox_d7.setObjectName(_fromUtf8("checkBox_d7"))
        self.comboBox_d6 = QtGui.QComboBox(self.tab_GPIO)
        self.comboBox_d6.setGeometry(QtCore.QRect(470, 260, 131, 27))
        self.comboBox_d6.setObjectName(_fromUtf8("comboBox_d6"))
        self.comboBox_d6.addItem(_fromUtf8(""))
        self.comboBox_d6.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_GPIO, _fromUtf8(""))
        self.tab_JTAG = QtGui.QWidget()
        self.tab_JTAG.setObjectName(_fromUtf8("tab_JTAG"))
        self.tabWidget.addTab(self.tab_JTAG, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuInterfaces = QtGui.QMenu(self.menubar)
        self.menuInterfaces.setObjectName(_fromUtf8("menuInterfaces"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionUART = QtGui.QAction(MainWindow)
        self.actionUART.setObjectName(_fromUtf8("actionUART"))
        self.actionI2C = QtGui.QAction(MainWindow)
        self.actionI2C.setObjectName(_fromUtf8("actionI2C"))
        self.actionSPI = QtGui.QAction(MainWindow)
        self.actionSPI.setObjectName(_fromUtf8("actionSPI"))
        self.actionGPIO = QtGui.QAction(MainWindow)
        self.actionGPIO.setObjectName(_fromUtf8("actionGPIO"))
        self.actionJTAG = QtGui.QAction(MainWindow)
        self.actionJTAG.setObjectName(_fromUtf8("actionJTAG"))
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menuInterfaces.addAction(self.actionUART)
        self.menuInterfaces.addAction(self.actionI2C)
        self.menuInterfaces.addAction(self.actionSPI)
        self.menuInterfaces.addAction(self.actionGPIO)
        self.menuInterfaces.addAction(self.actionJTAG)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInterfaces.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Attify Badge Tool", None))
        self.comboBox_BaudRate.setItemText(0, _translate("MainWindow", "Select Baud Rate", None))
        self.comboBox_BaudRate.setItemText(1, _translate("MainWindow", "600", None))
        self.comboBox_BaudRate.setItemText(2, _translate("MainWindow", "1200", None))
        self.comboBox_BaudRate.setItemText(3, _translate("MainWindow", "2400", None))
        self.comboBox_BaudRate.setItemText(4, _translate("MainWindow", "4800", None))
        self.comboBox_BaudRate.setItemText(5, _translate("MainWindow", "9600", None))
        self.comboBox_BaudRate.setItemText(6, _translate("MainWindow", "14400", None))
        self.comboBox_BaudRate.setItemText(7, _translate("MainWindow", "19200", None))
        self.comboBox_BaudRate.setItemText(8, _translate("MainWindow", "38400", None))
        self.comboBox_BaudRate.setItemText(9, _translate("MainWindow", "57600", None))
        self.comboBox_BaudRate.setItemText(10, _translate("MainWindow", "115200", None))
        self.comboBox_BaudRate.setItemText(11, _translate("MainWindow", "128000", None))
        self.comboBox_BaudRate.setItemText(12, _translate("MainWindow", "256000", None))
        self.pushButton_AutoDetect.setText(_translate("MainWindow", "Detect BaudRate", None))
        self.pushButton_Connect.setText(_translate("MainWindow", "Connect", None))
        self.comboBox_Ender.setItemText(0, _translate("MainWindow", "No line ending", None))
        self.comboBox_Ender.setItemText(1, _translate("MainWindow", "Carriage Return", None))
        self.comboBox_Ender.setItemText(2, _translate("MainWindow", "New Line", None))
        self.comboBox_Ender.setItemText(3, _translate("MainWindow", "Both CR + NL", None))
        self.textEdit_UartConsole.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff5500;\">                                                             Attify Badge Tool V1.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[*] Detecting USB ports</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_UART), _translate("MainWindow", "   UART   ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_I2C), _translate("MainWindow", "     I2C     ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SPI), _translate("MainWindow", "     SPI     ", None))
        self.checkBox_d0.setText(_translate("MainWindow", "Pin D0", None))
        self.comboBox_d0.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d0.setItemText(1, _translate("MainWindow", "    Output", None))
        self.checkBox_d1.setText(_translate("MainWindow", "Pin D1", None))
        self.comboBox_d1.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d1.setItemText(1, _translate("MainWindow", "    Output", None))
        self.checkBox_d2.setText(_translate("MainWindow", "Pin D2", None))
        self.comboBox_d2.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d2.setItemText(1, _translate("MainWindow", "    Output", None))
        self.comboBox_d3.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d3.setItemText(1, _translate("MainWindow", "    Output", None))
        self.checkBox_d3.setText(_translate("MainWindow", "Pin D3", None))
        self.comboBox_d5.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d5.setItemText(1, _translate("MainWindow", "    Output", None))
        self.comboBox_d7.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d7.setItemText(1, _translate("MainWindow", "    Output", None))
        self.checkBox_d4.setText(_translate("MainWindow", "Pin D4", None))
        self.checkBox_d6.setText(_translate("MainWindow", "Pin D6", None))
        self.comboBox_d4.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d4.setItemText(1, _translate("MainWindow", "    Output", None))
        self.checkBox_d5.setText(_translate("MainWindow", "Pin D5", None))
        self.checkBox_d7.setText(_translate("MainWindow", "Pin D7", None))
        self.comboBox_d6.setItemText(0, _translate("MainWindow", "    Input", None))
        self.comboBox_d6.setItemText(1, _translate("MainWindow", "    Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_GPIO), _translate("MainWindow", "  GPIO  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_JTAG), _translate("MainWindow", " JTAG ", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuInterfaces.setTitle(_translate("MainWindow", "Interfaces", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionUART.setText(_translate("MainWindow", "UART", None))
        self.actionI2C.setText(_translate("MainWindow", "I2C", None))
        self.actionSPI.setText(_translate("MainWindow", "SPI", None))
        self.actionGPIO.setText(_translate("MainWindow", "GPIO", None))
        self.actionJTAG.setText(_translate("MainWindow", "JTAG", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

