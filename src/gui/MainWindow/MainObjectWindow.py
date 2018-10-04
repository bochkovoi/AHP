#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
sys.path.append(path1)
sys.path.append(path2)
from Structure import *
from .MainCategoriesVision import *
from .MainAlternativesVision import *
from SubCriteriasVision import *
from .MainRadioButton import *
from .MainCriteriasVision import *

class MainObjectWindow( QtWidgets.QWidget ):
    """ Главное окно приложения """
    def __init__( self, main_object, parent=None ):
        
        super().__init__( parent )
        self.main_object = main_object
        
        self.initUI()
        
    def initUI( self ):
        """ Инициализируем окно """
        #Объявляем виджеты категорий, альтернатив, критерий и кнопки состояния
        self.categories = MainCategoriesVision( self.main_object, parent=self )
        self.alternatives = MainAlternativesVision( self.main_object, parent=self )
        self.is_simple_button = MainRadioButton( self.main_object, parent=self )
        self.criterias = MainCriteriasVision( self.main_object, parent=self )
        
        #Соединяем все сигналы с методом обновления окна
        self.alternatives.is_changed.connect( self.refresh)
        self.categories.is_changed.connect( self.refresh )
        self.is_simple_button.is_changed.connect( self.refresh )
        self.criterias.is_changed.connect( self.refresh )
        
        #Создаем форму и заполняем ее
        form1 = QtWidgets.QFormLayout()
        form1.addRow(  self.alternatives, self.criterias)
        form = QtWidgets.QFormLayout()
        form.addRow( self.categories,  form1)
        form.addRow( self.is_simple_button )
        self.setLayout( form )
        
    def refresh( self ):
        """ Обновляем все виджеты """
        for widget in [self.categories, self.alternatives, self.criterias]:
            widget.refresh()
        
        
