import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
import GUI
import Main
from PyQt4 import QtGui

app = QApplication(sys.argv)

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.form = Main.VideoPlayerClass()

    def test_defaults(self):
        # '''Test the GUI in its default state'''
        self.assertEqual(self.form.label.text(), "")
        self.assertEqual(self.form.progressbar.value(),0)
        self.assertEqual(self.form.action12.text(),"-->14")
        self.assertEqual(self.form.progressbar.isHidden(),True)
        self.assertEqual(self.form.btnPlaywithtext.isHidden(),True)
        self.assertEqual(self.form.actionPytesseract.text(),"-->Pytesseract")
        self.assertEqual(self.form.actionMedium.text(),"-->Medium")

    def test_btnplay(self):
        QTest.mouseClick(self.form.btnPlay,Qt.LeftButton)
        self.assertEqual(self.form.btnPlaywithtext.isHidden(),True)


    def test_btngeneratetext(self):
        QTest.mouseClick(self.form.btnGeneratetext,Qt.LeftButton)
        self.assertEqual(self.form.btnCancel.isHidden(),False)
        self.assertEqual(self.form.progressbar.isHidden(),False)

    def test_btncancel(self):
        QTest.mouseClick(self.form.btnCancel, Qt.LeftButton)
        self.assertEqual(self.form.btnCancel.isHidden(), True)
        self.assertEqual(self.form.progressbar.isHidden(),True)
        self.assertEqual(self.form.progressbar.value(),0)






if __name__ == '__main__':
    unittest.main()