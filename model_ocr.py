
import cv2

from model_char_recognize import CharRecognizer
from model_character_segmentation import  CharSegmentation
from model_textdetect import TextDetecter


class OCR:

    def __init__(self):
        # create objects of classes
        self.td=TextDetecter()
        self.charseg=CharSegmentation()
        self.charreg=CharRecognizer()


    def ocr(self,img):

        # detect text regions in image
        contours=self.td.detect_text(img)
        # contours = self.td.mserdetect(img)#detect text with mserdetect python module

        # get detected text regions orderly
        k=self.charseg.textOrder(contours)

        str=''
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        for t in k:
            if t=="space":
                str=str+" "
                continue

            if t=="enter":
                str=str+'\n'
                continue

            m, x, y, w, h = t
            ratio = w / h
            if ratio > 5:
                # if sample is too wide then it's probably a line across the page or something
                continue

            sample = img[y:y + h, x:x + w]  # take a text pertion out of the original image

            str=str+self.charreg.predictChar(sample)#predict character of sample


        return str



