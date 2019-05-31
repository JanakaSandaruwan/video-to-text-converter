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
from model_ocr import OCR as OCR


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

    def get_path(self,downloadpath):
        """
        :param downloadpath:
        :return: constructed download path where text file is generated
        """
        f = open(downloadpath, "r")
        s= f.read()
        f.close()
        if s=="":
            return ""
        else:
            return s+ "\\"

    def write_textfile(self,completepath,result):
        """
        write generated text into a file
        :param completepath:
        :param result:
        :return:
        """
        text_file = open(completepath, "w", encoding='utf-8')
        # encoding='utf-8'
        text_file.write(result)
        text_file.close()

    def compareFrames(self,img,f):
        """
        compare two frames
        :param img:
        :param f:
        :return: similarity percentage between two frames
        """
        scale_percent = self.scale_percent # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized_frame = cv2.resize(img.copy(), dim, interpolation=cv2.INTER_AREA)

        # percent of original size
        width = int(f.shape[1] * scale_percent / 100)
        height = int(f.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized_f = cv2.resize(f.copy(), dim, interpolation=cv2.INTER_AREA)


        res = cv2.matchTemplate(resized_frame, resized_f, cv2.TM_CCOEFF_NORMED)
        return res

    def generateSrt(self,path):
        dict={}
        result = ''

        if path=="":
            # return None if path to video is empty
            return
        cap = cv2.VideoCapture(path)#capture video


        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))#no of frames in the video
        fps = cap.get(cv2.CAP_PROP_FPS)#frame rate per second

        one_present=length/100.0


        currentFrame = 0
        ret, f = cap.read()


        # generate text of first frame
        if self.ispytesseract:
            # use pytesseract module to generate text
            dict[0.0]=pytesseract.image_to_string(f)
            result = result + pytesseract.image_to_string(f) + '\n'
        else:
            # use machine learning trained model to predict text
            dict[0.0] = self.myocr.ocr(f)
            result = result + self.myocr.ocr(f) + '\n'

        currentFrame += 1

        while (ret):
            # Capture frame-by-frame
            ret, frame = cap.read()

            if (not ret):
                break



            threshold = self.threshold#set threshol acording to accuracy level


            res= self.compareFrames(frame,f) #compare frame and f for similarity
            if res < threshold:#if similarity percentage is lower than threshold
                f = frame

                if self.ispytesseract:
                    dict[currentFrame/fps]=pytesseract.image_to_string(f)#set generated text to dictionary with its frame time
                    result = result + pytesseract.image_to_string(f) + '\n--------------------------------------------------------------------------\n'
                else:
                    dict[currentFrame / fps] = self.myocr.ocr(f)
                    result = result + self.myocr.ocr(
                        f) + '\n--------------------------------------------------------------------------\n'


            currentFrame += 1
            completed=(currentFrame/one_present)#calculate text generation percentage of video

            self.emit(SIGNAL("progress"),completed)#set progress bar value


        self.emit(SIGNAL("progress100"),100)

        completepath = os.path.join(self.get_path('downloadpath') + "output.txt")

        self.write_textfile(completepath,result)#write result text to text file


        # write dictionary to json
        with open('data.json', 'w',encoding='utf-8') as outfile:
            json.dump(dict, outfile)


        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()





