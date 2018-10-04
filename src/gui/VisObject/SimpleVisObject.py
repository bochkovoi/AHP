#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from .VisObject import *

class SimpleVisObject( VisObject ):
    """ Простое отображение объекта (без возможности изменения)"""
    def __init__( self, obj, parent=None ):
        super().__init__( obj, parent=parent)
        #Добавляем кнопку и соединяем ее с выходом
        exitButton = QtWidgets.QPushButton("Назад")
        exitButton.clicked.connect( self.exit )
        self.form.addRow(exitButton)
        self.setLayout( self.form )
        
    def exit( self ):
        """ Выходим, делая активными родительские окна """
        try:
            try:
                self.parent().parent().setEnabled(True)
            except AttributeError:
                self.parent().setEnabled(True)
                
        except AttributeError:
            QtWidgets.qApp.quit()
        self.destroy()
        
