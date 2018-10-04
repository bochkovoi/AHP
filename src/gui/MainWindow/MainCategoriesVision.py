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

class MainCategoriesVision( QtWidgets.QWidget ):
        #Объявляем сигнал изменения окна
    is_changed = pyqtSignal()
    
    def __init__( self, main_object, parent=None ):
        self.__main = main_object
        super().__init__( parent=parent )
        self.initUI()
    
    def initUI( self ):
        ''' Инициализируем окно'''
        
        #Создаем заголовок
        
        label = QtWidgets.QLabel("Категории:")

        #Создаем список
        self.sub_objs = QtWidgets.QListWidget( )

        self.refresh()
            
        #Создаем форму и заполняем ее
        form = QtWidgets.QFormLayout()
        form.addRow( label )
        form.addRow(self.sub_objs)
        
        self.setLayout(form)
        #Присоединяем сигнал двойного щелчка к методу
        self.sub_objs.itemDoubleClicked.connect( self.isDoubleClicked )
        
    
    def isDoubleClicked( self, obj ):
        """ Вызывает окно редактирования категории при наличии альтернатив и критериев """
        if self.__main.criterias == [] or self.__main.criterias == []:
            window = QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сравниваемые критерии и альтернативы", defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            #Создает окно
            sub_window = CategoryWindow( obj.sub_obj, parent=self )
            sub_window.setWindowTitle( "Просмотр категории: " + obj.sub_obj.name )
            #Делаем главное окно неактивным
            if self.parent() is None:
                self.setEnabled( False )
            else:
                self.parent().setEnabled( False )
        #Делаем активным дочернее окно, ставим на нем флаги и отображаем
            sub_window.setEnabled( True )
            sub_window.setWindowFlags( sub_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
            sub_window.show()
        
    def refresh( self ):
        """ Обновляет лист категорий """
        #Очищаем подчиненный объект
        self.sub_objs.clear()
        #Если режим главного объекта простой, то отображаем только категории затрат и выгод, а если нет - все четыре
        if self.__main.is_simple:
            work_set = [self.__main.costs, self.__main.profit]
        else:
            work_set = [self.__main.risk, self.__main.possibility, self.__main.costs, self.__main.profit]
        #Заполняем список
        for obj in work_set:
            a = QtWidgets.QListWidgetItem()
            a.sub_obj = obj
            a.setText( obj.name )
            self.sub_objs.addItem( a )
            
        
