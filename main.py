#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import cv2
import tensorflow as tf
import tensorflow_hub as hub
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 531, 581))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")

        self.individual_tab = QtWidgets.QWidget()
        self.individual_tab.setObjectName("individual_tab")

        self.step1_i = QtWidgets.QLabel(self.individual_tab)
        self.step1_i.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.step1_i.setFont(font)
        self.step1_i.setObjectName("step1_i")

        self.step2_i = QtWidgets.QLabel(self.individual_tab)
        self.step2_i.setGeometry(QtCore.QRect(10, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.step2_i.setFont(font)
        self.step2_i.setObjectName("step2_i")

        self.contentButton_i = QtWidgets.QPushButton(self.individual_tab)
        self.contentButton_i.setGeometry(QtCore.QRect(10, 40, 121, 41))
        self.contentButton_i.setObjectName("contentButton_i")
        self.contentButton_i.clicked.connect(self.get_content)

        self.contentPreview_i = QtWidgets.QLabel(self.individual_tab)
        self.contentPreview_i.setGeometry(QtCore.QRect(10, 90, 251, 221))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.contentPreview_i.setFont(font)
        self.contentPreview_i.setAutoFillBackground(True)
        self.contentPreview_i.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.contentPreview_i.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentPreview_i.setText("")
        self.contentPreview_i.setScaledContents(True)
        self.contentPreview_i.setAlignment(QtCore.Qt.AlignCenter)
        self.contentPreview_i.setObjectName("contentPreview_i")
        self.content_image = None

        self.styleButton_i = QtWidgets.QPushButton(self.individual_tab)
        self.styleButton_i.setGeometry(QtCore.QRect(270, 40, 111, 41))
        self.styleButton_i.setObjectName("styleButton_i")
        self.styleButton_i.clicked.connect(self.get_style)

        self.stylePreview_i = QtWidgets.QLabel(self.individual_tab)
        self.stylePreview_i.setGeometry(QtCore.QRect(270, 90, 251, 221))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stylePreview_i.setFont(font)
        self.stylePreview_i.setAutoFillBackground(True)
        self.stylePreview_i.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stylePreview_i.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stylePreview_i.setText("")
        self.stylePreview_i.setScaledContents(True)
        self.stylePreview_i.setAlignment(QtCore.Qt.AlignCenter)
        self.stylePreview_i.setObjectName("stylePreview_i")
        self.style_image = None

        self.createButton_i = QtWidgets.QPushButton(self.individual_tab)
        self.createButton_i.setGeometry(QtCore.QRect(50, 370, 161, 41))
        self.createButton_i.setObjectName("createButton_i")
        self.createButton_i.clicked.connect(self.create_stylized)

        self.saveButton_i = QtWidgets.QPushButton(self.individual_tab)
        self.saveButton_i.setGeometry(QtCore.QRect(50, 490, 161, 41))
        self.saveButton_i.setObjectName("saveButton_i")

        self.stylizedPreview_i = QtWidgets.QLabel(self.individual_tab)
        self.stylizedPreview_i.setGeometry(QtCore.QRect(270, 330, 251, 221))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stylizedPreview_i.setFont(font)
        self.stylizedPreview_i.setAutoFillBackground(True)
        self.stylizedPreview_i.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stylizedPreview_i.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stylizedPreview_i.setScaledContents(True)
        self.stylizedPreview_i.setAlignment(QtCore.Qt.AlignCenter)
        self.stylizedPreview_i.setObjectName("stylizedPreview_i")
        self.stylized_image = None

        self.infoLabel_i = QtWidgets.QLabel(self.individual_tab)
        self.infoLabel_i.setGeometry(QtCore.QRect(400, 40, 111, 41))
        self.infoLabel_i.setAutoFillBackground(True)
        self.infoLabel_i.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoLabel_i.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel_i.setWordWrap(True)
        self.infoLabel_i.setObjectName("infoLabel_i")

        self.progressBar_i = QtWidgets.QProgressBar(self.individual_tab)
        self.progressBar_i.setGeometry(QtCore.QRect(60, 440, 181, 23))
        self.progressBar_i.setProperty("value", 24)
        self.progressBar_i.setObjectName("progressBar_i")

        self.tabWidget.addTab(self.individual_tab, "")

        self.batch_tab = QtWidgets.QWidget()
        self.batch_tab.setObjectName("batch_tab")

        self.progressBar_b = QtWidgets.QProgressBar(self.batch_tab)
        self.progressBar_b.setGeometry(QtCore.QRect(210, 220, 181, 23))
        self.progressBar_b.setProperty("value", 24)
        self.progressBar_b.setObjectName("progressBar_b")

        self.contentButton_b = QtWidgets.QPushButton(self.batch_tab)
        self.contentButton_b.setGeometry(QtCore.QRect(10, 50, 171, 41))
        self.contentButton_b.setObjectName("contentButton_b")

        self.step2_b = QtWidgets.QLabel(self.batch_tab)
        self.step2_b.setGeometry(QtCore.QRect(10, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.step2_b.setFont(font)
        self.step2_b.setObjectName("step2_b")

        self.infLable_b = QtWidgets.QLabel(self.batch_tab)
        self.infLable_b.setGeometry(QtCore.QRect(400, 60, 111, 81))
        self.infLable_b.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infLable_b.setAlignment(QtCore.Qt.AlignCenter)
        self.infLable_b.setWordWrap(True)
        self.infLable_b.setObjectName("infLable_b")

        self.styleButton_b = QtWidgets.QPushButton(self.batch_tab)
        self.styleButton_b.setGeometry(QtCore.QRect(210, 50, 171, 41))
        self.styleButton_b.setObjectName("styleButton_b")

        self.createButton_b = QtWidgets.QPushButton(self.batch_tab)
        self.createButton_b.setGeometry(QtCore.QRect(20, 210, 171, 41))
        self.createButton_b.setObjectName("createButton_b")

        self.styleFloderLabel = QtWidgets.QLabel(self.batch_tab)
        self.styleFloderLabel.setGeometry(QtCore.QRect(210, 100, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.styleFloderLabel.setFont(font)
        self.styleFloderLabel.setAutoFillBackground(True)
        self.styleFloderLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.styleFloderLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.styleFloderLabel.setScaledContents(False)
        self.styleFloderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.styleFloderLabel.setWordWrap(True)
        self.styleFloderLabel.setObjectName("styleFloderLabel")

        self.contetFloderLabel = QtWidgets.QLabel(self.batch_tab)
        self.contetFloderLabel.setGeometry(QtCore.QRect(10, 100, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contetFloderLabel.setFont(font)
        self.contetFloderLabel.setAutoFillBackground(True)
        self.contetFloderLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.contetFloderLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contetFloderLabel.setScaledContents(False)
        self.contetFloderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.contetFloderLabel.setWordWrap(True)
        self.contetFloderLabel.setObjectName("contetFloderLabel")

        self.step1_b = QtWidgets.QLabel(self.batch_tab)
        self.step1_b.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.step1_b.setFont(font)
        self.step1_b.setObjectName("step1_b")

        self.infoLabel2_b = QtWidgets.QLabel(self.batch_tab)
        self.infoLabel2_b.setGeometry(QtCore.QRect(20, 270, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infoLabel2_b.setFont(font)
        self.infoLabel2_b.setAutoFillBackground(True)
        self.infoLabel2_b.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel2_b.setWordWrap(True)
        self.infoLabel2_b.setObjectName("infoLabel2_b")

        self.tabWidget.addTab(self.batch_tab, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.step1_i.setText(_translate("MainWindow", "Step 1:"))
        self.step2_i.setText(_translate("MainWindow", "Step 2:"))
        self.contentButton_i.setText(_translate("MainWindow", "Select Base Image"))
        self.styleButton_i.setText(_translate("MainWindow", "Select Style Image"))
        self.createButton_i.setText(_translate("MainWindow", "Create Styleized Image"))
        self.saveButton_i.setText(_translate("MainWindow", "Save Styleized image"))
        self.stylizedPreview_i.setText(_translate("MainWindow", "TextLabel"))
        self.infoLabel_i.setText(_translate("MainWindow", "Smaller images work better, 256 x 256 pixels is ideal."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.individual_tab), _translate("MainWindow", "Individal"))
        self.contentButton_b.setText(_translate("MainWindow", "Select Base Images Folder"))
        self.step2_b.setText(_translate("MainWindow", "Step 2:"))
        self.infLable_b.setText(_translate("MainWindow", "Smaller style images work better, 256 x 256 pixels is ideal."))
        self.styleButton_b.setText(_translate("MainWindow", "Select Style Image Folder"))
        self.createButton_b.setText(_translate("MainWindow", "Create Styleized Images"))
        self.styleFloderLabel.setText(_translate("MainWindow", "Style Images Folder Name"))
        self.contetFloderLabel.setText(_translate("MainWindow", "Base Images Folder Name"))
        self.step1_b.setText(_translate("MainWindow", "Step 1:"))
        self.infoLabel2_b.setText(_translate("MainWindow", "This mode will save all the images created automaticly."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.batch_tab), _translate("MainWindow", "Batch"))

    def get_content(self):
        self.content_image, _ = QtWidgets.QFileDialog.getOpenFileName(parent=None,
            caption="Open Image", directory="./content", filter="Image Files (*.png *.jpg *.bmp)")
        self.contentPreview_i.setPixmap(QtGui.QPixmap(self.content_image))

    def get_style(self):
        self.style_image, _ = QtWidgets.QFileDialog.getOpenFileName(parent=None,
            caption="Open Image", directory="./styles", filter="Image Files (*.png *.jpg *.bmp)")
        self.stylePreview_i.setPixmap(QtGui.QPixmap(self.style_image))
    
    def load_image(self, img_path):
        img = tf.io.read_file(img_path)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = img[tf.newaxis, :]
        return img

    def create_stylized(self):
        print("Button pressed - create")
        if self.content_image and self.style_image:
            content = self.load_image(self.content_image)
            style = self.load_image(self.style_image)
            model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
            self.stylized_image = model(tf.constant(content), tf.constant(style))[0]
            self.stylizedPreview_i.setPixmap(QtGui.QPixmap(self.stylized_image))
    
    def save_stylized(self):
        pass
        # cv2.imwrite('/content/gdrive/MyDrive/style_transfer/ben_styled_waves.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
