from PyQt4 import QtGui
from PyQt4 import phonon
from PyQt4.QtCore import QThread, SIGNAL
import time
import json
import gui
import main1
from textrecognition import generateText
from textrecognition import generateSrt

class textgenerateThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        generateSrt(vp,vp.filepath)

class TextViewer(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        t = time.time()
        data = {}
        with open('data.json') as json_file:
            data = json.load(json_file)
            # data=json.loads(data)

        times = [float(i) for i in data.keys()]

        i = 0
        k = -1
        while i < len(times):
            if time.time() - t >= times[i]:
                if i != k:
                    val=data[str(times[i])]
                    print(val)
                    #self.label.setText(data[str(times[i])])
                    #QtGui.QApplication.processEvents()
                    self.emit(SIGNAL("Lable"),val)
                    k = i
                    i = i + 1




class VideoPlayerClass(main1.Ui_MainWindow, QtGui.QMainWindow):

    filepath=""
    ispause=False



    def __init__(self):
        super(VideoPlayerClass, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda:self.playwithtext() )
        self.pushButton_2.clicked.connect(lambda:self.pausewithtext())
        self.pushButton_3.clicked.connect(lambda: self.videoPlayer.stop())

        #self.pushButton_4.clicked.connect(lambda:self.download())
        tp=textgenerateThread()
        self.ispause= False
        self.pushButton_4.clicked.connect(lambda: tp.start())
        self.actionOpen.triggered.connect(self.select_video)
        self.actionChange_download_path.triggered.connect(self.select_path)
        self.actionExit.triggered.connect(self.close)
        self.textviewer= TextViewer()
        self.connect(self.textviewer,SIGNAL("Lable"),self.setLableVal)
        self.label.showFullScreen()



    def playwithtext(self):
        self.videoPlayer.play()
        self.textviewer.start()


    def setLableVal(self,val):
        self.label.setText(val)
        QtGui.QApplication.processEvents()



    def pausewithtext(self):
        self.videoPlayer.pause()




    def select_path(self):
        file = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        text_file = open("downloadpath", "w")
        text_file.write(file)
        text_file.close()
        #self.get_path()


    def select_video(self):
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Select Video')
        self.filepath=filepath
        self.load_video(filepath)
        #print (self.filepath)
        print(filepath)

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