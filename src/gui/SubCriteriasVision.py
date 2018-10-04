#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from MatrixAppend import *
from Criteria import *
from SubVision import *
from VisObject import *

class SubCriteriasVision( SubVision ):
    """ Окно просмотра критериев """
    def __init__( self, category, parent=None ):
        self.category = category
        super().__init__( self.category, parent=parent )
        
        #Объявляем кнопку
        criteriaRedButton = QtWidgets.QPushButton("Редактировать элемент")
        criteriaRedButton.clicked.connect(self.red_criteria)
        
        box = QtWidgets.QVBoxLayout()
        box.addWidget( criteriaRedButton )
        
        self.form.addRow(box)
    
    def isDoubleClicked( self, obj ):
        """ При двойном щелчке открывается окно редактирования критерия """
        sub_window = CriteriaWindow( obj.sub_obj, parent=self )
        sub_window.setWindowTitle( "Редактирование критерия: " + obj.sub_obj.name )
        
        #При наличии родительского окна, делаем его неактивным
        if self.parent() is None:
            self.setEnabled( False )
        else:
            self.parent().setEnabled( False )
        
        #Делаем активным дочернее окно и устанавливаем его флаги
        sub_window.setEnabled( True )
        
        sub_window.setWindowFlags( sub_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        sub_window.show()
        
        
    def red_criteria( self ):
        try:
            self.isDoubleClicked(self.sub_objs.currentItem())
        except AttributeError:
            pass
