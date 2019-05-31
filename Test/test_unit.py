import unittest
from text_recog_handler import TextGenerator as TG
from model_char_recognize import CharRecognizer as CR
from model_character_segmentation import CharSegmentation as CS
import cv2

class TestCharRecognizer(unittest.TestCase):

    def test_select_best(self):
        char_recog=CR()
        input1=[[],[],[]]
        output1=''
        self.assertEqual(char_recog.select_best(input1),output1)

        input2=[[('a',1)],[('b',0.77)],[('c',0.56)],[]]
        output2='a'
        self.assertEqual(char_recog.select_best(input2),output2)

        input2 = [[('a', 1)], [('b', 1)], [('c', 1)], [('a',1)]]
        output2 = 'a'
        self.assertEqual(char_recog.select_best(input2), output2)

        input2 = [[('a', 1)], [('a', 1)], [('b', 1)], [('b',1)]]
        y=char_recog.select_best(input2)
        output2= (y == 'a') or (y =='b')
        self.assertTrue(output2)

        input1=[]
        output1=''
        self.assertEqual(char_recog.select_best(input1),output1)


class TestCharSegmentation(unittest.TestCase):
    def setUp(self):
        self.char_seg=CS()

    def test_arrange(self):
        input1=[]
        output1=[]
        self.assertEqual(self.char_seg.arrange(input1),output1)

        input1=[[615, 1057, 590, 23, 25], [614, 1033, 590, 22, 24], [615, 957, 590, 17, 25], [614, 933, 590, 22, 24]]
        output1= [[1, 933, 590, 22, 24], [1, 957, 590, 17, 25], [1, 1033, 590, 22, 24], [1, 1057, 590, 23, 25]]
        self.assertEqual(self.char_seg.arrange(input1),output1)

    def test_average_w_h(self):
        input1=[]
        output1=[0,0]
        self.assertEqual(self.char_seg.get_average_w_h(input1),output1)

        input1 = [[615, 1057, 590, 23, 25], [614, 1033, 590, 22, 24], [615, 957, 590, 17, 25], [614, 933, 590, 22, 24]]
        output1= [21.0, 24.5]
        self.assertEqual(self.char_seg.get_average_w_h(input1),output1)

    def test_decode(self):
        input1=[]
        output1=[]
        self.assertEqual(self.char_seg.decode(input1),output1)

        input1 = [[615, 1057, 590, 23, 25], [614, 1033, 590, 22, 24], [615, 957, 590, 17, 25], [614, 933, 590, 22, 24]]
        output1 = [[1, 933, 590, 22, 24], [1, 957, 590, 17, 25], 'space', [1, 1033, 590, 22, 24], [1, 1057, 590, 23, 25]]
        self.assertEqual(self.char_seg.decode(input1), output1)

        input1 = [[615, 1057, 590, 23, 25], [614, 1033, 590, 22, 24], [715, 957, 590, 17, 25], [715, 933, 590, 22, 24]]
        output1 =[[1, 1033, 590, 22, 24], [1, 1057, 590, 23, 25], 'enter', [2, 933, 590, 22, 24], [2, 957, 590, 17, 25]]
        self.assertEqual(self.char_seg.decode(input1), output1)


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
        completepath1="E:\\Semester Project\\ui\\Test\\expected_textfile.txt"
        result="Testing Testing"
        self.objTG.write_textfile(completepath1,result)

        fo=open(completepath1,'r')
        res=fo.read()
        fo.close()

        self.assertEqual(res,result)

    def test_generateSrt(self):
        video_path="E:\\Semester Project\\ui\\test video\\test1.mp4"
        self.objTG.generateSrt(video_path)

        fo = open("Test/expected_output.txt", 'r')
        res = fo.read()
        fo.close()

        fo = open("output.txt", 'r')
        result = fo.read()
        fo.close()

        self.assertEqual(res, result)


if __name__ == '__main__':
    unittest.main()