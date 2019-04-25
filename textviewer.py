from PyQt4.QtCore import QThread, SIGNAL
import time
import json


class TextViewer(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.ispause= False
        self.isstop= False
        self.pausedtime=0

    def run(self):
        t = time.time()
        data = {}
        with open('data.json') as json_file:
            data = json.load(json_file)
            # data=json.loads(data)

        times = [float(i) for i in data.keys()]

        i = 0
        k = -1
        while i < len(times) and not self.isstop:
            if time.time() - t-self.pausedtime >= times[i]:
                if i != k:
                    val=data[str(times[i])]
                    #print(val)
                    #self.label.setText(data[str(times[i])])
                    #QtGui.QApplication.processEvents()
                    self.emit(SIGNAL("Lable"),val)
                    k = i
                    i = i + 1
            k=time.time()
            while self.ispause and not self.isstop:
                self.pausedtime=time.time()-k

        if self.isstop:
            self.emit(SIGNAL("Lable"), "")

        # print("End")
