import keras
import numpy as np
import copy
import cv2
import random
import tensorflow as tf


class CharRecognizer:
    def __init__(self):
        self.img_size = 32
        self.charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        # self.model = keras.models.load_model('model/keras_alphanumeric.mod')
        self.model = keras.models.load_model('E:\\Semester Project\\ui\\model\\keras_alphanumeric.mod')
        self.model._make_predict_function()
        self.graph = tf.get_default_graph()

    def pad_scale_sample(self,image):
        scale_factor = self.img_size / image.shape[0]
        new_x = round(image.shape[1] * scale_factor)
        image = cv2.resize(image, dsize=(new_x, self.img_size), fx=scale_factor, fy=scale_factor)
        border = cv2.copyMakeBorder(image, top=0, bottom=0, left=16, right=16, borderType=cv2.BORDER_CONSTANT, value=255)
        return border


    def single_inferance(self,img):
        img = np.expand_dims(img, axis=2)
        img = np.expand_dims(img, axis=0)

        # model = keras.models.load_model('E:\\Semester Project\\ui\\model\\keras_alphanumeric.mod')
        # preds, = self.model.predict(img)
        with self.graph.as_default():
            preds,   = self.model.predict(img)

        lst = list(preds)
        # print("jjj",lst)
        result = []
        for i in range(len(lst)):
            crtnty = float(lst[i])
            if crtnty < 0.5:
                continue
            ltr = self.charset[i]
            if ltr == 'Q':
                continue
            result.append((ltr, crtnty))
        # print(result)
        return result


    def scan_image(self,image):
        results = []
        idx = 0
        while True:
            try:
                sample = image[0:self.img_size, idx:idx + self.img_size]
                idx += 8
                # print("rrr")
                inferance = self.single_inferance(sample)
                # print("ee")
                results.append(inferance)
                # pp(inferance)

            except Exception as e:

                return results

    def select_best(self,prediction):

        maxx=0
        n=[]

        for i in prediction:
            if len(i)!=0:
                n.append(i)

        prediction=n
        random.shuffle(prediction)
        if len(prediction)==0:
            return ''
        for i in range(len(prediction)):

            if maxx<prediction[i][0][1]:
                maxx=prediction[i][0][1]

        new=list(tuple(prediction))

        for i in range(len(prediction)):
            if prediction[i][0][1]<maxx:
                new.remove(prediction[i])

        prediction=new
        if len(prediction)==0:
            return ''

        counter=[]
        for i in range(len(prediction)):
            counter.append(prediction.count(prediction[i]))

        mm=max(counter)
        max_c=counter.index(mm)
        #print(prediction[max_c][0][0])
        return prediction[max_c][0][0]

    def predictChar(self,sample):
        sample = self.pad_scale_sample(sample)  # scale to 32px high and pad sides for scanning

        predictions = self.scan_image(sample)

        if len(predictions) > 1:
            s = self.select_best(predictions)


        else:
            if len(predictions) != 0:
                s= predictions[0][0][0]
        return s


