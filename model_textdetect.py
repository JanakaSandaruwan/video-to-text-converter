
import copy
import cv2


class TextDetecter:
    def preprocess_image(self,image):
        gray_blur = cv2.GaussianBlur(image, (15, 15), 0)
        # cv2.imshow("IMAGE",gray_blur)
        thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
        return thresh

    # def show_contours(self,image, contours):
    #     cp = copy.copy(image)
    #     cv2.drawContours(cp, contours, -1, (255, 0, 0), 1)
    #     cv2.imshow('contours', cp)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    def detect_text(self,img):
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        thresh = self.preprocess_image(img)
        contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def mserdetect(self,img):
        mser = cv2.MSER_create()
        # Convert to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()
        regions, _ = mser.detectRegions(gray)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
        # return hulls
        px, py, pw, ph = -10000, -100000, -100000, -1000
        k = []
        for obj in hulls:
            # print(obj)
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
