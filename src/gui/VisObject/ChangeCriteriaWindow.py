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

class ChangeCriteriaWindow( ChangeVisObject ):
    """ Окно изменения критерия """
    def __init__( self , obj, main_object, parent=None ):
        super().__init__( obj, supObj=main_object, parent=parent)
        
    def is_good_name( self ):
        """ Проверяем, подходящим ли является имя """
        if self.name.text().strip(' ') in [criteria.name for criteria in self.main_obj.criterias if criteria is not self.elem]:
            #Если имя состоит из пробелов или не задано, или критерий с таким именем уже существует, выкидываем ошибку.
            window = QtWidgets.QMessageBox.critical(self, "Ошибка имени", "Критерий с таким именем уже существует", defaultButton=QtWidgets.QMessageBox.Ok)
            self.name.setText(self.elem.name)
            return False
        else:
            return super().is_good_name() and True
        
    def save( self ):
        """ Сохраняем элемент """
        if self.is_good_name():
            super().save()
            self.exit()
            self.main_obj.vis()
        else:
            pass
