#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..', 'Structure')
path2 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
sys.path.append(path1)
sys.path.append(path2)
from Structure import *
from copy import copy

class VisObject( QtWidgets.QWidget ):
    ''' Отображает объект '''
    def __init__( self, element, parent=None ):
        # Объявляем как окно и запрещаем разворачивать и закрывать 
        super().__init__( parent, QtCore.Qt.Window )
        self.setWindowFlags( self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        #Присваиваем элемент
        self.elem = element
        self.initUI()
    def initUI( self ):
        
        name_label = QtWidgets.QLabel("Наименование")
        text_label = QtWidgets.QLabel("Описание")
        
        self.name = QtWidgets.QLineEdit()
        self.name.setText(self.elem.name)
        self.text = QtWidgets.QTextEdit()
        self.text.setText(self.elem.description)
        
        self.form = QtWidgets.QFormLayout()
        self.form.addRow( name_label, self.name )
        self.form.addRow( text_label, self.text )
        
        self.setLayout( self.form )
        
