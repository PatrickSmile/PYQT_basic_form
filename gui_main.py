# -*- coding: utf-8 -*-
"""
@author: patrick.park@epitone.ai
"""

import sys
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(BASE_DIR + r"\gui.ui")[0]
# main gui window class

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Image Generator")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()