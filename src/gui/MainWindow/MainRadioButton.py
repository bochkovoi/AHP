#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
sys.path.append(path1)
sys.path.append(path2)
from Structure import *
from .MainCategoriesVision import *
from .MainAlternativesVision import *
from SubCriteriasVision import *

class MainRadioButton( QtWidgets.QWidget ):
    ''' Окно режима объекта'''
    
    is_changed = pyqtSignal()
    def __init__( self, main_obj, parent=None ):
        
        super().__init__( parent=parent )
        
        self.main_obj = main_obj
        
        #Делаем надпись и две радиокнопки
        label = QtWidgets.QLabel("Сложность модели")
        
        setTrueButton = QtWidgets.QRadioButton("Две категории")
        setFalseButton = QtWidgets.QRadioButton("Четыре категории")
        
        #Соединяем одну из кнопок с методов и ставим указатель на ней
        setTrueButton.toggled.connect( self.setTrue )
        setTrueButton.setChecked(True)
        
        box = QtWidgets.QHBoxLayout()
        box.addWidget(setTrueButton)
        box.addWidget(setFalseButton)
        
        form = QtWidgets.QFormLayout()
        form.addRow(label)
        form.addRow(box)
        
        self.setLayout( form )
        
    def setTrue( self, is_right ):
        if is_right:
            self.main_obj.is_simple = True
        else:
            self.main_obj.is_simple = False
        self.is_changed.emit()
