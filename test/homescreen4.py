# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T:\Prafull\homescreen4.ui'
#
# Created: Fri Apr 21 15:56:07 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMinimumSize(QtCore.QSize(1000, 600))
        self.gridLayout_3 = QtGui.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_24 = QtGui.QLabel(self.frame_2)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_10.addWidget(self.label_24)
        self.label_25 = QtGui.QLabel(self.frame_2)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_10.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(self.frame_2)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        spacerItem = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_27 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_17.addWidget(self.label_27)
        self.comboBox_17 = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_17.sizePolicy().hasHeightForWidth())
        self.comboBox_17.setSizePolicy(sizePolicy)
        self.comboBox_17.setObjectName("comboBox_17")
        self.verticalLayout_17.addWidget(self.comboBox_17)
        self.horizontalLayout_11.addLayout(self.verticalLayout_17)
        spacerItem1 = QtGui.QSpacerItem(228, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_28 = QtGui.QLabel(self.frame_2)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_18.addWidget(self.label_28)
        self.comboBox_14 = QtGui.QComboBox(self.frame_2)
        self.comboBox_14.setObjectName("comboBox_14")
        self.verticalLayout_18.addWidget(self.comboBox_14)
        self.horizontalLayout_12.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_29 = QtGui.QLabel(self.frame_2)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_19.addWidget(self.label_29)
        self.comboBox_15 = QtGui.QComboBox(self.frame_2)
        self.comboBox_15.setObjectName("comboBox_15")
        self.verticalLayout_19.addWidget(self.comboBox_15)
        self.horizontalLayout_12.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_30 = QtGui.QLabel(self.frame_2)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_20.addWidget(self.label_30)
        self.comboBox_16 = QtGui.QComboBox(self.frame_2)
        self.comboBox_16.setObjectName("comboBox_16")
        self.verticalLayout_20.addWidget(self.comboBox_16)
        self.horizontalLayout_12.addLayout(self.verticalLayout_20)
        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_31 = QtGui.QLabel(self.frame_2)
        self.label_31.setMinimumSize(QtCore.QSize(161, 0))
        self.label_31.setObjectName("label_31")
        self.verticalLayout_22.addWidget(self.label_31)
        self.listWidget_3 = QtGui.QListWidget(self.frame_2)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_22.addWidget(self.listWidget_3)
        self.gridLayout_4.addLayout(self.verticalLayout_22, 0, 0, 1, 1)
        self.verticalLayout_23 = QtGui.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_32 = QtGui.QLabel(self.frame_2)
        self.label_32.setMinimumSize(QtCore.QSize(151, 0))
        self.label_32.setObjectName("label_32")
        self.verticalLayout_23.addWidget(self.label_32)
        self.listWidget_4 = QtGui.QListWidget(self.frame_2)
        self.listWidget_4.setObjectName("listWidget_4")
        self.verticalLayout_23.addWidget(self.listWidget_4)
        self.gridLayout_4.addLayout(self.verticalLayout_23, 0, 1, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_5 = QtGui.QPushButton(self.frame_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_14.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.frame_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_14.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.frame_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_14.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.frame_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_14.addWidget(self.pushButton_8)
        self.gridLayout_4.addLayout(self.horizontalLayout_14, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.splitter)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textEdit = QtGui.QTextEdit(self.frame_4)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_5.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Form", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Form", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("Form", "Select Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Form", "Select Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Form", "Select Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("Form", "Select Dept.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("Form", "Server Path Versions :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("Form", "Local Path Versions :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Start session", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "SFA", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "SFC", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "End Session", None, QtGui.QApplication.UnicodeUTF8))

