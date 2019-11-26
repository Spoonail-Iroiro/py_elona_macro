# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui',
# licensing of 'main_form.ui' applies.
#
# Created: Sat Nov 23 06:18:10 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(655, 412)
        self.mainView = CanvasGraphicsView(MainForm)
        self.mainView.setGeometry(QtCore.QRect(0, 0, 256, 192))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainView.sizePolicy().hasHeightForWidth())
        self.mainView.setSizePolicy(sizePolicy)
        self.mainView.setObjectName("mainView")

        self.retranslateUi(MainForm)
        QtCore.QObject.connect(self.mainView, QtCore.SIGNAL("capture_complete()"), MainForm.accept)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtWidgets.QApplication.translate("MainForm", "Dialog", None, -1))

from canvas_graphicsview import CanvasGraphicsView
