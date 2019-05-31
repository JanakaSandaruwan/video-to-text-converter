from PyQt4 import QtGui
from PyQt4 import phonon
from PyQt4.QtCore import QThread, SIGNAL
import time
import json
import GUI
from text_recog_handler import TextGenerator as TextGenerator
from textviewer import TextViewer as TextViewer
from model_ocr import OCR as OCR


class VideoPlayerClass(GUI.Ui_MainWindow, QtGui.QMainWindow):
    """
     This class handles gui and basic gui operations
    """


    def __init__(self):
        super(VideoPlayerClass, self).__init__()
        self.setupUi(self)
        # button functions of video player
        self.btnPlay.clicked.connect(lambda :self.playVideo())
        self.btnPlaywithtext.clicked.connect(lambda:self.playwithtext() )
        self.btnPause.clicked.connect(lambda:self.pausewithtext())
        self.btnStop.clicked.connect(lambda: self.stopplayer())

        # hide progressbar and cancel button at the begining
        self.progressbar.hide()
        self.btnCancel.hide()

        #self.pushButton_4.clicked.connect(lambda:self.download())
        self.filepath=""
        self.tp= TextGenerator()
        self.tp.ispytesseract=True

        self.ocr=OCR()

        self.btnGeneratetext.clicked.connect(lambda: self.generateText())

        self.actionOpen.triggered.connect(self.select_video)
        self.actionChange_download_path.triggered.connect(self.select_path)
        self.actionExit.triggered.connect(self.close)

        # set font size
        self.action10.triggered.connect(lambda: self.setFont10())
        self.action12.triggered.connect(lambda :self.setFont12())
        self.action14.triggered.connect(lambda: self.setFont14())
        self.action16.triggered.connect(lambda: self.setFont16())
        self.action18.triggered.connect(lambda: self.setFont18())
        self.action20.triggered.connect(lambda: self.setFont20())
        self.action24.triggered.connect(lambda: self.setFont24())
        self.action28.triggered.connect(lambda: self.setFont28())


        self.textviewer= TextViewer()
        self.connect(self.textviewer,SIGNAL("Lable"),self.setLableVal)
        self.label.showFullScreen()
        self.connect(self.tp, SIGNAL("progress"), self.setProgress)
        self.connect(self.tp, SIGNAL("progress100"), self.setProgress100)

        # set accuracy and speed level
        self.actionLow.triggered.connect(lambda :self.setLowAccuracy())
        self.actionMedium.triggered.connect(lambda: self.setMediumAccuracy())
        self.actionHigh.triggered.connect(lambda: self.setHighAccuracy())

        self.btnCancel.clicked.connect(lambda :self.cancelTextGenerate())


        self.actionPytesseract.triggered.connect(lambda :self.usePytesseract())
        self.actionML.triggered.connect(lambda :self.useMyocr())

        self.isgenerate=False
        self.btnPlaywithtext.hide()

        self.btnGeneratetext.hide()


    def playVideo(self):
        # play video player
        self.videoPlayer.play()
        # hide play with button when play button is pressed
        self.btnPlaywithtext.hide()




    def usePytesseract(self):
        # select pytesseract module for text recognition
        self.tp.ispytesseract=True
        self.actionPytesseract.setText("-->Pytesseract")
        self.actionML.setText("ML")

    def useMyocr(self):
        # select machine learning model for text recognition
        self.tp.ispytesseract=False
        self.actionPytesseract.setText("Pytesseract")
        self.actionML.setText("-->ML")



    def cancelTextGenerate(self):
        # cancel text file generation task
        self.tp.terminate()
        # set progressbar attributes
        self.progressbar.hide()
        self.progressbar.setValue(0)
        self.btnCancel.hide()


    def setLowAccuracy(self):
        # set accuracy level low
        self.tp.threshold=0.3
        self.tp.scale_percent=25
        self.actionLow.setText("-->Low")
        self.actionMedium.setText("Medium")
        self.actionHigh.setText("High")

    def setMediumAccuracy(self):\
        # set accuracy level medium
        self.tp.threshold=0.5
        self.tp.scale_percent=50
        self.actionLow.setText("Low")
        self.actionMedium.setText("-->Medium")
        self.actionHigh.setText("High")

    def setHighAccuracy(self):
        # set accuracy level high
        self.tp.threshold=0.9
        self.tp.scale_percent=75
        self.actionLow.setText("Low")
        self.actionMedium.setText("Medium")
        self.actionHigh.setText("-->High")

    # set font sizes of text screen
    def setFont10(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(10) + 'pt ')
        self.action10.setText("-->10")
        self.action12.setText("14")
        self.action14.setText("16")
        self.action16.setText("20")
        self.action18.setText("24")
        self.action20.setText("28")
        self.action24.setText("36")
        self.action28.setText("48")

    def setFont12(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(14) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("-->14")
        self.action14.setText("16")
        self.action16.setText("20")
        self.action18.setText("24")
        self.action20.setText("28")
        self.action24.setText("36")
        self.action28.setText("48")


    def setFont14(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(16) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("14")
        self.action14.setText("-->16")
        self.action16.setText("20")
        self.action18.setText("24")
        self.action20.setText("28")
        self.action24.setText("36")
        self.action28.setText("48")


    def setFont16(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(20) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("14")
        self.action14.setText("16")
        self.action16.setText("-->20")
        self.action18.setText("24")
        self.action20.setText("28")
        self.action24.setText("36")
        self.action28.setText("48")


    def setFont18(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(24) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("14")
        self.action14.setText("16")
        self.action16.setText("20")
        self.action18.setText("-->24")
        self.action20.setText("28")
        self.action24.setText("36")
        self.action28.setText("48")


    def setFont20(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(28) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("14")
        self.action14.setText("16")
        self.action16.setText("20")
        self.action18.setText("24")
        self.action20.setText("-->28")
        self.action24.setText("36")
        self.action28.setText("48")


    def setFont24(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(36) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("14")
        self.action14.setText("16")
        self.action16.setText("20")
        self.action18.setText("24")
        self.action20.setText("28")
        self.action24.setText("-->36")
        self.action28.setText("48")


    def setFont28(self):
        self.label.setStyleSheet('background-color: black; color: white ; font-size:' + str(48) + 'pt ')
        self.action10.setText("10")
        self.action12.setText("14")
        self.action14.setText("16")
        self.action16.setText("20")
        self.action18.setText("24")
        self.action20.setText("28")
        self.action24.setText("36")
        self.action28.setText("-->48")


    # set profress bar value
    def setProgress(self,val):
        # print("val",val)
        self.progressbar.setValue(val)

    # set progressbar attributes after completing text generation
    def setProgress100(self,val):
        self.progressbar.setValue(val)
        self.progressbar.hide()
        self.btnCancel.hide()
        self.btnPlaywithtext.show()
        self.isgenerate=True

    # start text generating process
    def generateText(self):
        self.progressbar.show()
        self.btnCancel.show()

        self.tp.start()
        # path = "E:\\Semester Project\\ui\\test video\\Janaka.mp4"
        # self.ocr.generateSrt(path)
        # self.ocr.start()

    # play video with text
    def playwithtext(self):
        self.videoPlayer.play()
        self.textviewer.ispause= False
        self.textviewer.isstop=False
        self.textviewer.start()
        self.btnPlaywithtext.hide()
        self.seekSlider.hide()

    # display text on text screen
    def setLableVal(self,val):
        self.label.setText(val)
        QtGui.QApplication.processEvents()


    def pausewithtext(self):
        self.videoPlayer.pause()
        self.textviewer.ispause=True


    def stopplayer(self):
        self.videoPlayer.stop()
        self.textviewer.isstop=True
        self.label.setText("")
        self.textviewer.ispause= False
        self.textviewer.pausedtime=0
        if self.isgenerate:
            self.btnPlaywithtext.show()
            self.seekSlider.show()


    # select the path of video from folders
    def select_path(self):
        file = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        text_file = open("downloadpath", "w")
        text_file.write(file)
        text_file.close()
        #self.get_path()


    def select_video(self):
        self.btnPlaywithtext.hide()
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Select Video')
        self.filepath=filepath
        self.tp.setFilePath(self.filepath)
        # self.tp=TextGenerator(self.filepath)
        self.load_video(filepath)
        #print (self.filepath)
        self.isgenerate=False
        self.btnGeneratetext.show()
        # print(filepath)

    def load_video(self, filepath):
        media = phonon.Phonon.MediaSource(filepath)
        self.videoPlayer.load(media)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
        self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
        #self.videoPlayer.play()





if __name__ == '__main__':
    app = QtGui.QApplication([])
    vp = VideoPlayerClass()
    vp.show()
    app.exec_()