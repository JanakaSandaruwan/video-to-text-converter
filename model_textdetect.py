
import copy
import cv2


class TextDetecter:
    def preprocess_image(self,image):
        blur_image = cv2.GaussianBlur(image, (15, 15), 0)
        th = cv2.adaptiveThreshold(blur_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
        return th


    def detect_text(self,img):
        # return contours(regions with same color ) of the image
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        th = self.preprocess_image(img)
        contours, hierarchy = cv2.findContours(image=th, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def mserdetect(self,img):
        #use mser to detect text
        mser = cv2.MSER_create()
        # Convert to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()
        regions, _ = mser.detectRegions(gray)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
        # return hulls
        px, py, pw, ph = -10000, -100000, -100000, -1000
        k = []
        # remove same letters detected several times
        for obj in hulls:

            area = cv2.contourArea(obj)
            # if area < 10:
            #     # if sample is too small, probably just artifact
            #     continue
            x, y, w, h = cv2.boundingRect(obj)
            x = x - 5
            y = y - 5
            w = w + 10
            h = h + 10
            if px - 2 <= x <= px + 2 and py - 2 <= y <= py + 2:
                continue

            k.append(obj)

        return k
