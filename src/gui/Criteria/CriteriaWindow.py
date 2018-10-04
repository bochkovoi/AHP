#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
sys.path.append(path1)
sys.path.append(path2)
from SubVision import *
from VisObject import *
from MatrixAppend import *

class CriteriaWindow( QtWidgets.QWidget ):
    """ Окно критерия """
    def __init__( self, criteria, parent=None ):
        
        super().__init__( parent, QtCore.Qt.Window )
        
        self.__criteria = criteria
        self.initUI()
    
    def initUI( self ):
        """ Инициализируем окно """
        self.matrix = MatrixAppend(self.__criteria, parent=self)
        self.alternatives = SubVision(self.__criteria, is_change=False, parent=self)
        # Объявляем кнопки
        moreButton = QtWidgets.QPushButton("Подробнее...")
        moreButton.clicked.connect( self.more )
        exitButton = QtWidgets.QPushButton("Назад")
        exitButton.clicked.connect( self.exit )
        
        #Объявляем метку и форму
        alternatives_label = QtWidgets.QLabel("Сравниваемые альтернативы")
        
        alternatives = QtWidgets.QVBoxLayout()
        alternatives.addWidget(alternatives_label)
        alternatives.addWidget(self.alternatives)
        
        form = QtWidgets.QFormLayout()
        form.addRow( self.matrix, alternatives )
        form.addRow(moreButton)
        form.addRow(exitButton)
        self.setLayout( form )
    
    def more( self ):
        """ """
        more_win = SimpleVisObject( self.__criteria, parent=self )
        more_win.setWindowTitle("О критерии")
        more_win.show()
        
    def exit( self ):
        """ """
        try:
            try:
                self.parent().parent().setEnabled(True)
            except AttributeError:
                self.parent().setEnabled(True)
        except AttributeError:
            QtWidgets.qApp.quit()
        self.destroy()
        
