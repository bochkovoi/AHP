#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import  os.path as pth
path = pth.abspath(pth.normpath(pth.join(pth.dirname(__file__), 'Structure')))
sys.path.append(path)
path = pth.abspath(pth.normpath(pth.join(pth.dirname(__file__))))
from PyQt5 import QtWidgets
from .MainWindow import *
from Structure import *

class Application(QtWidgets.QApplication):
    def __init__( self, argv ):
        super().__init__( argv )
        self.main_object = MainObject()
        self.main_window = MainObjectWindow(self.main_object)
        self.main_window.setWindowTitle( 'Основное окно' )
        self.main_window.setWindowFlags( self.main_window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.main_window.show()
