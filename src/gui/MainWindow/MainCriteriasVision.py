#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..',  '..')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
sys.path.append(path1)
sys.path.append(path2)
from Categories import *
from VisObject import *

class MainCriteriasVision( QtWidgets.QWidget ):
    
    is_changed = pyqtSignal()
    
    def __init__( self, main_object, parent=None ):
        self.__main = main_object
        super().__init__( parent=parent )
        self.initUI()
        
    def initUI( self ):
        ''' '''
        label = QtWidgets.QLabel("Критерии")
        
        #Создаем список
        self.sub_objs = QtWidgets.QListWidget( )
        
        #Заполняем список критериями
        
        criterias = self.__main.criterias
        for obj in criterias:
            a = QtWidgets.QListWidgetItem()
            a.sub_obj = obj
            a.setText( obj.name )
            self.sub_objs.addItem( a )
            
        #Добавляем кнопку добавления критерия
        
        add_button = QtWidgets.QPushButton("Добавить критерий")
        add_button.clicked.connect( self.add_criteria )
        
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(add_button)
        #Объявляем и заполняем форму
        
        form = QtWidgets.QFormLayout()
        form.addRow( label )
        form.addRow(self.sub_objs)
        form.addRow(layout)
        
        #Располагаем форму в виджете
        
        self.setLayout(form)
        
        #Присоединяем двойной щелчок к функции isDoubleClicked
        
        self.sub_objs.itemDoubleClicked.connect( self.isDoubleClicked )
    
    def isDoubleClicked( self, obj ):
        sub_window = ChangeCriteriaWindow( obj.sub_obj, self.__main,  parent=self )
        sub_window.setWindowTitle( "Редактирование критерия: " + obj.sub_obj.name )
        if self.parent() is None:
            self.setEnabled( False )
        else:
            self.parent().setEnabled( False )
        sub_window.setEnabled( True )
        sub_window.setWindowFlags( sub_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        sub_window.show()
    
    def add_criteria( self ):
        sub_window = AddCriteriaWindow( self.__main, parent=self )
        sub_window.setWindowTitle( "Добавление  альернативы: " )
        if self.parent() is None:
            self.setEnabled( False )
        else:
            self.parent().setEnabled( False )
        sub_window.setEnabled( True )
        sub_window.setWindowFlags( sub_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        sub_window.show()
        
    def refresh( self ):
        self.sub_objs.clear()
        criterias = self.__main.criterias
        for obj in criterias:
            a = QtWidgets.QListWidgetItem()
            a.sub_obj = obj
            a.setText( obj.name )
            self.sub_objs.addItem( a )
        
