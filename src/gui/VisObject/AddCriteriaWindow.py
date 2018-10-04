#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from .ChangeVisObject import *
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..', 'Structure')
path2 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
sys.path.append(path1)
sys.path.append(path2)
from Structure import *

class AddCriteriaWindow( ChangeVisObject ):
    """ Окнр добавления критерия """
    def __init__( self, main, parent=None ):
        #Передаем в качестве параметров основной объект и пустой критерий
        super().__init__( Criteria(''), supObj=main, parent=parent )

    def is_good_name( self ):
        """ Проверяем, подходящим ли является имя? """
        if self.name.text().strip(' ') in [criteria.name for criteria in self.main_obj.criterias]:
            #Если имя состоит из пробелов или не задано, или критерий с таким именем уже существует, выкидываем ошибку.
            window = QtWidgets.QMessageBox.critical(self, "Ошибка имени", "Критерий с таким именем уже существует", defaultButton=QtWidgets.QMessageBox.Ok)
            self.name.setText("")
            return False
        else:
            return super().is_good_name() and True
        
    def save( self ):
        """ Сохраняем элемент, если он подходящий """
        if self.is_good_name():
            super().save()
            self.main_obj.add_criteria( self.elem )
            self.exit()
        else:
            pass
