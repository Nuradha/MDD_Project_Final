import sys
from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess, os, platform
from main_ui import Ui_MainWindow
from main_ui import Ui_MainWindow_Output
from main_ui import Ui_MainWindow_Work
import real_full

class Main(QMainWindow, Ui_MainWindow, Ui_MainWindow_Output,Ui_MainWindow_Work):
    filename=""
    output_type=""
    output_name=""
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
    def browse(self):
        global filename
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '.')[0]
        self.textEdit=QtWidgets.QTextEdit()
        str(self.textEdit.setText(self.filename))
        self.lineEdit.setText(self.filename)

    def pastwork(self):
	    window_work=self.setupUi_Work(self)

    
    def gotohome(self):
        self.filename=""
        self.output_type=""
        self.output_name=""
        window_home=self.setupUi(self)

    def openfile(self):
        if self.output_type=="PDF":
            ind=self.filename.rfind('/')
            file_location=self.filename[:ind]+'/'
            filepath=file_location+"%s.PDF" % self.output_name
            filepath=filepath.replace("/","\\")
        elif self.output_type=="WORD":
            filepath=os.getcwd()+"\\Outputs\\Docs\\"+"%s.docx" % self.output_name
        if platform.system() == 'Darwin':
                subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':
                os.startfile(filepath)
        else:
                subprocess.call(('xdg-open', filepath))
            
    def start(self):
        if self.filename!="" and self.output_type!="":
            try:
                self.output_name= self.lineEdit1.text()
                window_output=self.setupUi_Output(self)
                self.lineEdit.setText(self.output_type)
                self.lineEdit_2.setText(self.output_name)
                real_full.create_doc(str(self.filename),str(self.output_type),str(self.output_name))
            except Exception as e:
                self.magjava=QtWidgets.QMessageBox()
                self.magjava.setText(str(e))
                self.magjava.exec_()

    def radioOnClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.output_type=radioButton.type
    def radioOnClicked_1(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.process=radioButton.process

if __name__ == "__main__":
    if not os.path.exists('Outputs/Docs'):
        os.makedirs('Outputs/Docs')
    if not os.path.exists('Outputs/Contoured'):
        os.makedirs('Outputs/Contoured')
    if not os.path.exists('Outputs/Canny_Images'):
        os.makedirs('Outputs/Canny_Images')
    appctxt = ApplicationContext() 
    window = Main()
    window.show()
    sys.exit(appctxt.app.exec_())