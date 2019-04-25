import cv2
import numpy as np
import os
import pytesseract
import os.path
import json
import time
from PyQt4.QtCore import QThread, SIGNAL
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from PIL import Image
from ocr import OCR as OCR


class TextGenerator(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.filepath=''
        self.scale_percent=50
        self.threshold=0.5
        self.ispytesseract=True
        self.myocr=OCR()

    def setFilePath(self,path):
        self.filepath=path

    def run(self):
        self.generateSrt(self.filepath)

    def get_path(self):
        f = open("downloadpath", "r")
        s= f.read()
        if s=="":
            return ""
        else:
            return s+ "\\"

    def compareFrames(self,img,f):
        scale_percent = self.scale_percent # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized_frame = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        # percent of original size
        width = int(f.shape[1] * scale_percent / 100)
        height = int(f.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized_f = cv2.resize(f, dim, interpolation=cv2.INTER_AREA)


        res = cv2.matchTemplate(resized_frame, resized_f, cv2.TM_CCOEFF_NORMED)
        return res

    def generateSrt(self,path):
        dict={}
        result = ''

        print("Start Generate Text")

        if path=="":
            return
        cap = cv2.VideoCapture(path)


        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        one_present=length/100.0
        completed=0

        currentFrame = 0
        ret, f = cap.read()

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'

        cv2.imwrite(name, f)

        if self.ispytesseract:
            dict[0.0]=pytesseract.image_to_string(f)
            result = result + pytesseract.image_to_string(f) + '\n'
        else:
            dict[0.0] = self.myocr.ocr(f)
            result = result + self.myocr.ocr(f) + '\n'

        currentFrame += 1

        while (ret):
            # Capture frame-by-frame
            ret, frame = cap.read()

            if (not ret):
                break



            threshold = self.threshold
            # print(threshold)

            # res = cv2.matchTemplate(frame, f, cv2.TM_CCOEFF_NORMED)
            res= self.compareFrames(frame,f)
            if res < threshold:
                f = frame

                name = 'frame' + str(currentFrame) + '.jpg'
                # cv2.imwrite(name,f)
                if self.ispytesseract:
                    dict[currentFrame/fps]=pytesseract.image_to_string(f)
                    result = result + pytesseract.image_to_string(f) + '\n--------------------------------------------------------------------------\n'
                else:
                    dict[currentFrame / fps] = self.myocr.ocr(f)
                    result = result + self.myocr.ocr(
                        f) + '\n--------------------------------------------------------------------------\n'


            currentFrame += 1
            completed=(currentFrame/one_present)

            self.emit(SIGNAL("progress"),completed)


        self.emit(SIGNAL("progress100"),100)

        completepath = os.path.join(self.get_path() + "output.txt")

        text_file = open(completepath, "w")
        text_file.write(result)
        text_file.close()


        with open('data.json', 'w') as outfile:
            json.dump(dict, outfile)


        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        print("End Generate Text")






