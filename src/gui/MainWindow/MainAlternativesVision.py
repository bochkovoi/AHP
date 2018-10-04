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

class MainAlternativesVision( QtWidgets.QWidget ):
    #Объявляем сигнал изменения окна
    is_changed = pyqtSignal()
    
    def __init__( self, main_object, parent=None ):
        
        self.__main = main_object
        super().__init__( parent=parent )
        self.initUI()
        
    def initUI( self ):
        ''' Инициализируем окно'''
        
        #Создаем заголовок
        label = QtWidgets.QLabel("Альтернативы")
        
        #Создаем список
        self.sub_objs = QtWidgets.QListWidget( )
        
        #Заполняем переменную альтернативами и их значениями, которые будем отображать в скобках
        
        self.refresh()
            
        #Добавляем кнопку добавления альтернативы
        
        add_button = QtWidgets.QPushButton("Добавить альтернативу")
        add_button.clicked.connect( self.add_alternative )
        
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
        """ При двойном щелчке на альтернативе показываем окно изменения альтернативы """
        
        #Создаем окно
        sub_window = ChangeAlternativeWindow( obj.sub_obj, self.__main,  parent=self )
        sub_window.setWindowTitle( "Редактирование альернативы: " + obj.sub_obj.name )
        #Если есть родительское окно, делаем его неактивным (или делаем неактивным этот виджет)
        if self.parent() is None:
            self.setEnabled( False )
        else:
            self.parent().setEnabled( False )
        #Включаем дочернее окно и устанавливаем на него флаги отсутствия кнопки закрытия и кнопки раскрытия на весь экран
        sub_window.setEnabled( True )
        sub_window.setWindowFlags( sub_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        #Показываем окно
        sub_window.show()
    
    def add_alternative( self ):
        """ Показывает окно добавления альтернативы """
        #Создаем окно добавления альтернативы
        sub_window = AddAlternativeWindow( self.__main, parent=self )
        sub_window.setWindowTitle( "Добавление  альернативы: " )
        #Если есть родительское окно, делаем его неактивным (или делаем неактивным этот виджет)
        if self.parent() is None:
            self.setEnabled( False )
        else:
            self.parent().setEnabled( False )
        #Включаем дочернее окно и устанавливаем на него флаги отсутствия кнопки закрытия и кнопки раскрытия на весь экран
        sub_window.setEnabled( True )
        sub_window.setWindowFlags( sub_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        #Показываем окно
        sub_window.show()
        
    def refresh( self ):
        """ При обновлении окна обновляем все значения всех альтернатив """
        
        #Очищаем окно
        self.sub_objs.clear()
        
        main_values = self.__main.main_values
        for obj in main_values:
            #Создаем ячейку
            a = QtWidgets.QListWidgetItem()
            #Добавляем в ячейку объект
            a.sub_obj = obj
            val = ((main_values[obj] * 10000 ) // 1) / 10000
            #Добавляем в ячейку строку имя строки + значение объекта
            a.setText( obj.name + ' ( ' + str(val) + ' ) ' )
            self.sub_objs.addItem( a )
        
