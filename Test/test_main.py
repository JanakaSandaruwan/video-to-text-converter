import unittest
from text_recog_handler import TextGenerator as TG
import cv2

class TestTextRecognition(unittest.TestCase):
    def setUp(self):
        self.objTG=TG()

    def test_compareFrames(self):
        image1=cv2.imread("E:\\Semester Project\\ui\\ui\\frame61.jpg")
        image2=cv2.imread("E:\\Semester Project\\ui\\ui\\frame122.jpg")
        image3 = cv2.imread("E:\\Semester Project\\ui\\ui\\frame183.jpg")
        self.assertEqual(self.objTG.compareFrames(image2,image2)>=self.objTG.threshold,True)
        self.assertEqual(self.objTG.compareFrames(image3, image3)>=self.objTG.threshold, True)
        self.assertEqual(self.objTG.compareFrames(image2, image3)>=self.objTG.threshold, False)
        self.assertEqual(self.objTG.compareFrames(image2, image1)>=self.objTG.threshold, False)


    def test_get_path(self):
        testpath1_output='E:\\Semester Project\\ui\\ui\\'
        testpath2_output=""
        self.assertEqual(self.objTG.get_path('E:\\Semester Project\\ui\\Test\\testpath1'),testpath1_output)
        self.assertEqual(self.objTG.get_path('E:\\Semester Project\\ui\\Test\\testpath2'), testpath2_output)

    def test_write_textfile(self):
        completepath1="expected_output.txt"
        result="Testing Testing"
        self.objTG.write_textfile(completepath1,result)

        fo=open(completepath1,'r')
        res=fo.read()
        fo.close()

        self.assertEqual(res,result)

    def test_generateSrt(self):
        video_path="E:\\Semester Project\\ui\\test video\\test1.mp4"
        self.objTG.generateSrt(video_path)

        fo = open("expected_output.txt", 'r')
        res = fo.read()
        fo.close()

        fo = open("output.txt", 'r')
        result = fo.read()
        fo.close()

        self.assertEqual(res, result)




if __name__ == '__main__':
    unittest.main()