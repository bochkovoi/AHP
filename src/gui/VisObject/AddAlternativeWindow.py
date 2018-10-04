#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..', 'Structure')
path2 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
sys.path.append(path1)
sys.path.append(path2)
from Structure import *
from .ChangeVisObject import *

class AddAlternativeWindow( ChangeVisObject ):
    """ Окнр добавления альтернативы """
    def __init__( self, main, parent=None ):
        #Передаем в качестве параметров основной объект и пустую альтернативу
        super().__init__( Alternative(''), supObj=main, parent=parent )

    def is_good_name( self ):
        """ Проверяем, подходящим ли является имя """
        if self.name.text().strip(' ') in [alternative.name for alternative in self.main_obj.alternatives]:
            #Если имя состоит из пробелов или не задано, или альтернатива с таким именем уже существует, выкидываем ошибку.
            window = QtWidgets.QMessageBox.critical(self, "Ошибка имени", "Альтернатива с таким именем уже существует", defaultButton=QtWidgets.QMessageBox.Ok)
            self.name.setText("")
            return False
        else:
            return super().is_good_name() and True
        
    def save( self ):
        """ Сохраняем элемент, если он подходящий """
        super().save()
        if self.is_good_name():
            self.main_obj.add_alternative( self.elem )
            self.exit()
        else:
            pass
