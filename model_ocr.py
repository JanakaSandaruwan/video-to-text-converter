
import cv2

from model_char_recognize import CharRecognizer
from model_character_segmentation import  CharSegmentation
from model_textdetect import TextDetecter

# class OCR(QThread):
#     def __init__(self):
#         QThread.__init__(self)
#         self.img_size = 32
#         self.charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#         # self.model = keras.models.load_model('model/keras_alphanumeric.mod')
#         self.model = keras.models.load_model('E:\\Semester Project\\ui\\model\\keras_alphanumeric.mod')
#         self.model._make_predict_function()
#         self.graph = tf.get_default_graph()
#
#
#     def show_contours(self,image, contours):
#         cp = copy.copy(image)
#         cv2.drawContours(cp, contours, -1, (255, 0, 0), 1)
#         cv2.imshow('contours', cp)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#
#     def preprocess_image(self,image):
#         gray_blur = cv2.GaussianBlur(image, (15, 15), 0)
#         # cv2.imshow("IMAGE",gray_blur)
#         thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
#         return thresh
#
#
#     def pad_scale_sample(self,image):
#         scale_factor = self.img_size / image.shape[0]
#         new_x = round(image.shape[1] * scale_factor)
#         image = cv2.resize(image, dsize=(new_x, self.img_size), fx=scale_factor, fy=scale_factor)
#         border = cv2.copyMakeBorder(image, top=0, bottom=0, left=16, right=16, borderType=cv2.BORDER_CONSTANT, value=255)
#         return border
#
#
#     def single_inferance(self,img):
#         img = np.expand_dims(img, axis=2)
#         img = np.expand_dims(img, axis=0)
#
#         # model = keras.models.load_model('E:\\Semester Project\\ui\\model\\keras_alphanumeric.mod')
#         # preds, = self.model.predict(img)
#         with self.graph.as_default():
#             preds,   = self.model.predict(img)
#
#         lst = list(preds)
#         # print("jjj",lst)
#         result = []
#         for i in range(len(lst)):
#             crtnty = float(lst[i])
#             if crtnty < 0.5:
#                 continue
#             ltr = self.charset[i]
#             if ltr == 'Q':
#                 continue
#             result.append((ltr, crtnty))
#         # print(result)
#         return result
#
#
#     def scan_image(self,image):
#         results = []
#         idx = 0
#         while True:
#             try:
#                 sample = image[0:self.img_size, idx:idx + self.img_size]
#                 idx += 8
#                 # print("rrr")
#                 inferance = self.single_inferance(sample)
#                 # print("ee")
#                 results.append(inferance)
#                 # pp(inferance)
#
#             except Exception as e:
#                 # print('Failed to upload to ftp: ' + str(e))
#                 return results
#
#     def arrange(self,k):
#         k.sort()
#         if len(k)==0:
#             return k
#         # print(k)
#         ltr_width = 0
#         ltr_height = 0
#         for ltr in k:
#             m, x, y, w, h = ltr
#             ltr_width += w
#             ltr_height += h
#         ltr_width = ltr_width / len(k)
#         ltr_height = ltr_height / len(k)
#         j=1
#         pm, px, py, pw, ph = k[0]
#         k[0][0]=j
#         for i in range(1,len(k)):
#             m, x, y, w, h = k[i]
#             if pm-h/2.0 <= m <= pm+h/2.0:
#                 k[i][0]=j
#
#             else:
#                 pm, px, py, pw, ph = k[i]
#                 j=j+1
#                 k[i][0]=j
#
#         k.sort()
#         # print(k)
#         return k
#
#
#     def decode(self,pre):
#         # pre.sort()
#         # print(pre)
#         if len(pre)==0:
#             return pre
#         pre=self.arrange(pre)
#         ltr_width=0
#         ltr_height=0
#         for ltr in pre:
#             m, x, y, w, h = ltr
#             ltr_width +=w
#             ltr_height+=h
#         ltr_width=ltr_width/len(pre)
#         ltr_height=ltr_height/len(pre)
#
#         new=[]
#         new.append(pre[0])
#         x0=pre[0][1]
#         y0=pre[0][0]
#         for i in range(1,len(pre)):
#
#             if (y0<pre[i][0]):
#                 new.append("enter")
#             elif x0+ltr_width+5<pre[i][1] :
#                 new.append("space")
#             x0=pre[i][1]
#             y0=pre[i][0]
#             # ltr_width=pre[i][3]
#             new.append(pre[i])
#
#
#         return new
#
#
#
#
#     def scan(self,image):
#         idx = 0
#         sample = image[0:self.img_size, idx:idx + self.img_size]
#         # cv2.imshow('scaled and padded sample', sample)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#         inferance = self.single_inferance(sample)
#         pp(inferance)
#         return inferance
#
#     # def select_char(prediction):
#     #     for ltr in prediction:
#     #
#     def select_best(self,prediction):
#
#         maxx=0
#         n=[]
#
#         for i in prediction:
#             if len(i)!=0:
#                 n.append(i)
#
#         prediction=n
#         random.shuffle(prediction)
#         if len(prediction)==0:
#             return ''
#         for i in range(len(prediction)):
#
#             if maxx<prediction[i][0][1]:
#                 maxx=prediction[i][0][1]
#
#         new=list(tuple(prediction))
#
#         for i in range(len(prediction)):
#             if prediction[i][0][1]<maxx:
#                 new.remove(prediction[i])
#
#         prediction=new
#         if len(prediction)==0:
#             return ''
#
#         counter=[]
#         for i in range(len(prediction)):
#             counter.append(prediction.count(prediction[i]))
#
#         mm=max(counter)
#         max_c=counter.index(mm)
#         #print(prediction[max_c][0][0])
#         return prediction[max_c][0][0]
#
#
#
#
#     def ocr(self,img):
#         # clear_session()
#         img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#         img1 = copy.copy(img)
#         thresh = self.preprocess_image(img)
#         # cv2.imshow("Thresh",thresh)
#
#
#         contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
#
#         # print('num contours found', len(contours))
#         # show_contours(thresh, contours)
#
#         k = []
#         for obj in contours:
#
#             area = cv2.contourArea(obj)
#             if area < 50:
#                 # if sample is too small, probably just artifact
#                 continue
#             x, y, w, h = cv2.boundingRect(obj)
#             k.append([y + h, x, y, w, h])
#             cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#         k=self.decode(k)
#         # cv2.imshow("vv", img1)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#         str=''
#         for t in k:
#             if t=="space":
#                 # print("space")
#                 str=str+" "
#                 continue
#
#             if t=="enter":
#                 # print("enter")
#                 str=str+'\n'
#                 continue
#
#             m, x, y, w, h = t
#             # print(m,y,x)
#             ratio = w / h
#             if ratio > 5:
#                 # if sample is too wide then it's probably a line across the page or something
#                 continue
#
#             sample = img[y:y + h, x:x + w]  # take a sample out of the original image
#             # cv2.imshow("vv",sample)
#             # cv2.waitKey(0)
#             # cv2.destroyAllWindows()
#             sample = self.pad_scale_sample(sample)  # scale to 32px high and pad sides for scanning
#             # cv2.imshow("vv", sample)
#             # cv2.waitKey(0)
#             # cv2.destroyAllWindows()
#             predictions = self.scan_image(sample)
#             # predictions = self.scan(sample)
#             # print(predictions)
#
#             if len(predictions)>1:
#                 s=self.select_best(predictions)
#                 str=str+s
#                 # print(s)
#             else:
#                 if len(predictions)!=0:
#                     str+=predictions[0][0][0]
#                 # print(predictions[0][0][0])
#         print ("THiS IS The Answer",str)
#         return str



class OCR:

    def __init__(self):
        self.td=TextDetecter()
        self.charseg=CharSegmentation()
        self.charreg=CharRecognizer()


    def ocr(self,img):

        contours=self.td.detect_text(img)

        # contours = self.td.mserdetect(img)
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

            sample = img[y:y + h, x:x + w]  # take a sample out of the original image

            str=str+self.charreg.predictChar(sample)

        # print ("THiS IS The Answer",str)
        return str



