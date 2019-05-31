import keras
import numpy as np
import copy
import cv2
import random
import tensorflow as tf


class CharRecognizer:
    def __init__(self):
        self.img_size = 32
        self.char_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        # self.model = keras.models.load_model('model/ocr_model.mod')
        self.model = keras.models.load_model('E:\\Semester Project\\ui\\model\\ocr_model.mod')
        self.model._make_predict_function()
        self.graph = tf.get_default_graph()

    def resize_image(self, image):
        # scale to 32px high and pad sides for searching predictions
        scale_factor = self.img_size / image.shape[0] #calculte scale of real image
        new_x = round(image.shape[1] * scale_factor)
        image = cv2.resize(image, dsize=(new_x, self.img_size), fx=scale_factor, fy=scale_factor)#resize image
        border = cv2.copyMakeBorder(image, top=0, bottom=0, left=16, right=16, borderType=cv2.BORDER_CONSTANT, value=255)
        return border


    def get_predicted_letter_list(self, img):
        #change dimension of image
        img = np.expand_dims(img, axis=2)
        img = np.expand_dims(img, axis=0)

        #predict letter using saved model
        with self.graph.as_default():
            preds,   = self.model.predict(img)

        lst = list(preds)#get prediction probability list

        result = []
        for i in range(len(lst)):
            probability = float(lst[i])
            if probability < 0.5:
                #if probality of being a letter is less than 0.5,ignore it
                continue

            ltr = self.char_str[i] #get letter from char_str

            result.append((ltr, probability)) #append tuple to result list

        return result


    def search_prediction(self, img):
        letters = []
        x = 0
        while True:
            try:
                #iterate x value by 8 and select sample image for prediction
                sample = img[0:self.img_size, x:x + self.img_size]
                x += 8

                inferance = self.get_predicted_letter_list(sample)

                letters.append(inferance)#add predicted (letter,probability) tuples to letters list


            except Exception as e:

                return letters

    def select_best(self,prediction):
        #select best predicted letter from prediction list
        maxx=0
        n=[]

        # remove [] from prediction
        for i in prediction:
            if len(i)!=0:
                n.append(i)

        prediction=n
        random.shuffle(prediction)

        # return empty symbol if prediction is empty
        if len(prediction)==0:
            return ''
        # get maximum accuracy of prediction as maxx
        for i in range(len(prediction)):

            if maxx<prediction[i][0][1]:
                maxx=prediction[i][0][1]

        new=list(tuple(prediction))

        #remove all predictions which has less accuracy than maxx in list
        for i in range(len(prediction)):
            if prediction[i][0][1]<maxx:
                new.remove(prediction[i])


        prediction=new
        if len(prediction)==0:
            return ''

        #get number of occurences of each counted letter
        counter=[]
        for i in range(len(prediction)):
            counter.append(prediction.count(prediction[i]))

        mm=max(counter) #get maximum count
        max_c=counter.index(mm) #get max count index
        #print(prediction[max_c][0][0])
        return prediction[max_c][0][0]

    def predictChar(self,img):
        sample = self.resize_image(img)  # scale to 32px high and pad sides for scanning

        predictions = self.search_prediction(sample)#get prediction list

        if len(predictions) > 1:

            s = self.select_best(predictions)
            #select best prediction from pediction list

        else:
            if len(predictions) != 0:
                s= predictions[0][0][0]
        return s


