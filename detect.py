import cv2
import numpy as np
from ocr import *
#Create MSER object
mser = cv2.MSER_create()

#Your image path i-e receipt path
img = cv2.imread("E:\\Semester Project\\ui\\ui\\images.jpg")

#Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# gray = preprocess_image(gray)
    # cv2.imshow("Thresh",thresh)

vis = img.copy()

#detect regions in gray scale image
regions, _ = mser.detectRegions(gray)
im=np.array(regions[0])
# print(_[0])
#cv2.imshow('dd',im)

hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
px,py,pw,ph=-10000,-100000,-100000,-1000
k = []
for obj in hulls:

    area = cv2.contourArea(obj)
    # if area < 10:
    #     # if sample is too small, probably just artifact
    #     continue
    x, y, w, h = cv2.boundingRect(obj)
    x=x-5
    y=y-5
    w=w+10
    h=h+10
    if px-2<=x<=px+2 and py-2<=y<=py+2:
        continue

    k.append((y + h, x, y, w, h))
    cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # print(x,y,w,h)
    px,py,pw,ph=x,y,w,h
    # sample = img[y:y + h, x:x + w]  # take a sample out of the original image
    # cv2.imshow("vv",sample)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



k.sort()

# cv2.polylines(vis, hulls, 1, (0, 255, 0))

# cv2.imshow('img', vis)

cv2.waitKey(0)

for t in k:
    m, x, y, w, h = t
    # print(m,y,x)
    ratio = w / h
    if ratio > 5:
        # if sample is too wide then it's probably a line across the page or something
        continue

    sample = img[y:y + h, x:x + w]  # take a sample out of the original image
    # cv2.imshow("vv",sample)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    sample = pad_scale_sample(sample)  # scale to 32px high and pad sides for scanning
    cv2.imshow("vv", sample)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    predictions = scan_image(sample)
    # predictions = scan(sample)
    pp(predictions)

# mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)

# for contour in hulls:

#     cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

# #this is used to find only text regions, remaining are ignored
# text_only = cv2.bitwise_and(img, img, mask=mask)
#
# cv2.imshow("text only", text_only)
#
# cv2.waitKey(0)