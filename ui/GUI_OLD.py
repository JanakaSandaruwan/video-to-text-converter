# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
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
        MainWindow.resize(1688, 853)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(20, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(530, 580, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 580, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 580, 93, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.frame)
        self.seekSlider.setGeometry(QtCore.QRect(40, 550, 941, 22))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.frame)
        self.volumeSlider.setGeometry(QtCore.QRect(870, 580, 113, 26))
        self.volumeSlider.setMinimumSize(QtCore.QSize(20, 0))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 580, 271, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(640, 170, 291, 221))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.frame)
        self.videoPlayer.setGeometry(QtCore.QRect(10, 10, 1001, 531))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.label = QtGui.QLabel(self.frame)
        #self.label.setGeometry(QtCore.QRect(30, 629, 971, 461))
        self.label.setGeometry(QtCore.QRect(1030, 10, 600, 531))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        a=20
        self.label.setStyleSheet('background-color: black; color: white ; font-size:'+str(a)+'pt ')
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionChange_download_path = QtGui.QAction(MainWindow)
        self.actionChange_download_path.setObjectName(_fromUtf8("actionChange_download_path"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionChange_download_path)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(80, 700, 900, 20)
        self.progress.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Video To Text Annotator", None))
        self.pushButton.setText(_translate("MainWindow", "Play", None))
        self.pushButton_2.setText(_translate("MainWindow", "Pause", None))
        self.pushButton_3.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_4.setText(_translate("MainWindow", "Generate Text", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionChange_download_path.setText(_translate("MainWindow", "Change download path", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from PyQt4 import phonon
