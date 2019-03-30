import cv2
import numpy as np
import os
import pytesseract
import os.path
import json
import time

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from PIL import Image

def get_path():
    f = open("downloadpath", "r")
    #print(f.read())
    s= f.read()
    if s=="":
        return ""
    else:
        return s+ "\\"



def generateSrt(sf,path):
    dict={}
    result = ''
    sf.progress.show()


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
    #print('Creating...' + name)
    cv2.imwrite(name, f)

    dict[0.0]=pytesseract.image_to_string(f)
    #cv2.imshow("video", f)
    currentFrame += 1

    while (ret):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if (not ret):
            break



        threshold = 0.5
        res = cv2.matchTemplate(frame, f, cv2.TM_CCOEFF_NORMED)
        if res < threshold:
            f = frame
            name = './data/frame' + str(currentFrame) + '.jpg'
            #print('Creating...' + name)
            dict[currentFrame/fps]=pytesseract.image_to_string(f)
            #cv2.imwrite(name, frame)
        currentFrame += 1
        completed=(currentFrame/one_present)
        sf.progress.setValue(completed)


    sf.progress.setValue(100)
    completepath=os.path.join(get_path()+"srt.txt")

    # dict = json.dumps(dict)
    # loaded_r = json.loads(dict)

    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile)





    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    #end = time.time()
    #print(end - start)
    sf.progress.hide()






















def generateText(sf,path):

    #start = time.time()
    result = ''
    sf.progress.show()


    if path=="":
        return
    cap = cv2.VideoCapture(path)


    #print("frames per second"+str(fps))

    # try:
    #     if not os.path.exists('data'):
    #         os.makedirs('data')
    # except OSError:
    #     print('Error: Creating directory of data')

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    one_present=length/100.0
    completed=0
    #print(length)
    #print(one_present)


    currentFrame = 0
    ret, f = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    #print('Creating...' + name)
    cv2.imwrite(name, f)
    result = result + pytesseract.image_to_string(f) + '\n'
    #cv2.imshow("video", f)
    currentFrame += 1

    while (ret):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if (not ret):
            break



        threshold = 0.5
        res = cv2.matchTemplate(frame, f, cv2.TM_CCOEFF_NORMED)
        if res < threshold:
            f = frame
            name = './data/frame' + str(currentFrame) + '.jpg'
            #print('Creating...' + name)
            result = result + pytesseract.image_to_string(
                f) + '\n--------------------------------------------------------------------------\n'
            #cv2.imwrite(name, frame)
        currentFrame += 1
        completed=(currentFrame/one_present)
        sf.progress.setValue(completed)
        #print(completed)
        #print(currentFrame)

    sf.progress.setValue(100)
    completepath=os.path.join(get_path()+"output.txt")
    print(completepath)

    text_file = open(completepath, "w")
    text_file.write(result)
    text_file.close()

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    #end = time.time()
    #print(end - start)
    sf.progress.hide()
