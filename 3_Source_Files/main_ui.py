from os import listdir
from PyQt5 import QtCore, QtGui, QtWidgets
import doc_resource

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(824, 506)
        MainWindow.setStyleSheet(_fromUtf8("#frame{background-image: url(background10.jpeg);opacity:0.5;}\n"
"#frame_2{background-color: rgb(218, 218, 218);border-radius: 15px; }\n"
""))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(90, 110, 541, 281))
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(23, 61, 89, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(118, 61, 129, 27))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(391, 230, 121, 27))
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(391, 22, 124, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(253, 61, 85, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(14, 110, 301, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(150, 12, 141, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 40, 132, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(9, 11, 132, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(15, 180, 301, 41))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(26, 195, 55, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(195, 195, 155, 100))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 20, 491, 91))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit1 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit1.setGeometry(QtCore.QRect(118, 190, 129, 27))
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Document Digitizer", None))
        self.label_3.setText(_translate("MainWindow", "Select Image:", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create a New Document</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "View Past Work", None))
        self.pushButton_3.setText(_translate("MainWindow", "Browse", None))
        self.radioButton.setText(_translate("MainWindow", "Word Document", None))
        self.radioButton_2.setText(_translate("MainWindow", "PDF Document", None))
        self.label_4.setText(_translate("MainWindow", "Choose File Format:", None))
        self.label_6.setText(_translate("MainWindow", "Save As:", None))
	#self.label_7.setText(_translate("MainWindow", "Please Wait...", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">DIGITAL DOCUMENT DIGITIZER</span></p></body></html>", None))
        self.pushButton_3.clicked.connect(self.browse)
        self.radioButton.type = "WORD"
        self.radioButton.toggled.connect(self.radioOnClicked)
        self.radioButton_2.type = "PDF"
        self.radioButton_2.toggled.connect(self.radioOnClicked)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.pastwork)


class Ui_MainWindow_Output(object):
    def setupUi_Output(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(824, 506)
        MainWindow.setStyleSheet(_fromUtf8("#frame{background-image: url(background10.jpeg);opacity:0.5;}\n"
"#frame_2{background-color: rgb(218, 218, 218);border-radius: 15px; }\n"
""))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 806, 466))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(90, 110, 541, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tibetan Machine Uni"))
        font.setItalic(True)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(391, 22, 124, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(391, 230, 124, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(31, 150, 80, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 132, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(31, 100, 55, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 150, 70, 60))
        self.pushButton_3.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("button.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(150, 200))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(190, 64, 130, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 95, 130, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 20, 491, 91))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi_Output(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi_Output(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Document Digitizer", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">The Output Document</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "View Past Work", None))
        self.pushButton_4.setText(_translate("MainWindow", "Home", None))
        self.label_3.setText(_translate("MainWindow", "Output File:", None))
        self.label_4.setText(_translate("MainWindow", "Output File Format:", None))
        self.label_5.setText(_translate("MainWindow", "File Name:", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">DIGITAL DOCUMENT DIGITIZER</span></p></body></html>", None))
        self.pushButton_2.clicked.connect(self.pastwork)
        self.pushButton_3.clicked.connect(self.openfile)
        self.pushButton_4.clicked.connect(self.gotohome)




class Ui_MainWindow_Work(object):
    def setupUi_Work(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(824, 506)
        MainWindow.setStyleSheet(_fromUtf8("#frame{background-image: url(background10.jpeg);}\n"
"#frame_2{background-color: rgb(218, 218, 218);border-radius: 15px; }\n"
""))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 806, 466))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(90, 110, 541, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tibetan Machine Uni"))
        font.setItalic(True)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(391, 230, 124, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 132, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listView = QtWidgets.QListView(self.frame_2)
        self.listView.setGeometry(QtCore.QRect(180, 60, 301, 141))
        self.listView.setStyleSheet(_fromUtf8(""))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 20, 491, 91))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        model = QtGui.QStandardItemModel(self.listView)
        files = listdir("Outputs/Docs/")
        for f in files:
                item = QtGui.QStandardItem(f)
                model.appendRow(item)
        self.listView.setModel(model)
        self.listView.show()
        self.retranslateUi_Work(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        self.retranslateUi_Work(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi_Work(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Document Digitizer", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Past Work</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "Home", None))
        self.label_4.setText(_translate("MainWindow", "List of Past Work:", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">DIGITAL DOCUMENT DIGITIZER</span></p></body></html>", None))
        self.pushButton_2.clicked.connect(self.gotohome)







if __name__ == "__main__":
    import sys
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

