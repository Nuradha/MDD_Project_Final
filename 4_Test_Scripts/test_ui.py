import sys
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import main

from PyQt5 import QtGui

app = QApplication(sys.argv)

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.form = main.Main()

    def test_defaults(self):
        self.assertEqual(self.form.lineEdit.text(), "")
        self.assertEqual(self.form.lineEdit1.text(), "")
        self.assertEqual(self.form.radioButton.isChecked(), False)
        self.assertEqual(self.form.radioButton_2.isChecked(), False)

    def test_pushButton(self):
        self.form.lineEdit.setText("document_name")
        self.form.lineEdit1.setText("document_type")
        QTest.mouseClick(self.form.pushButton,Qt.LeftButton)
        self.assertEqual(self.form.lineEdit.text(),"document_name")     
    
    def test_lineEdit(self):
        self.form.lineEdit.setText("document_name")
        self.form.lineEdit1.setText("document_type")
        QTest.mouseClick(self.form.pushButton,Qt.LeftButton)
        self.assertEqual(self.form.lineEdit.text(),"document_name")

    def test_lineEdit1(self):
        self.form.lineEdit.setText("document_name")
        self.form.lineEdit1.setText("document_type")
        QTest.mouseClick(self.form.pushButton,Qt.LeftButton)
        self.assertEqual(self.form.lineEdit1.text(),"document_type")
    
    def test_radioButton(self):
        self.form.radioButton.click()
        self.assertEqual(self.form.radioButton.isChecked(), True)
    
    def test_radioButton_2(self):
        self.form.radioButton_2.click()
        self.assertEqual(self.form.radioButton_2.isChecked(), True)


if __name__ == '__main__':
    unittest.main()