#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from copy import copy
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', 'Structure')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
path3 = op.join( op.abspath(op.dirname(__file__)), '..', 'Structure', 'Supports')
sys.path.append(path1)
sys.path.append(path2)
sys.path.append(path3)
from Structure import *

class MatrixAppend( QtWidgets.QWidget ):
    ''' Окно редактирования матрицы '''
    def __init__( self, support_object, parent=None ):
        super().__init__(parent)
        self.__obj = support_object
        self.objmatrix = copy(self.__obj.matrix)
        self.initUI()
    
    def initUI( self ):
        #Объявляем надписи матрицы и главного вектора
        self.setLabels()
        #Объявляем кнопки
        self.setButtons()
        #Создаем матрицу и вектор
        count = len(self.__obj.matrix.values)
        self.matrix = QtWidgets.QTableWidget(count, count)
        self.vector = QtWidgets.QTableWidget(count, 1)
        #Заполняем матрицу
        self.setMatrix()
        #Объявляем заголовки
        self.setHeaders()
        #Устанавливаем размеры матрицы
        self.setSize()
        #Подключаем изменение в матрице к функции is_changed
        self.matrix.cellChanged.connect(self.is_changed)
        
        buttons = QtWidgets.QHBoxLayout()
        form = QtWidgets.QFormLayout()
        
        buttons.addWidget( self.saveButton )
        buttons.addWidget( self.clearButton )
        
        form.addRow(self.matrix_label, self.vector_label )
        form.addRow( self.matrix, self.vector )
        form.addRow( buttons )
        
        self.setLayout( form )
    def setLabels( self ):
        """Объявляем надписи матрицы и главного вектора"""
        self.matrix_label = QtWidgets.QLabel('Значения матрицы')
        self.vector_label = QtWidgets.QLabel('Значения векторa')
    def setButtons( self ):
        ''' Объявляем кнопки '''
        #Кнопка сброса
        self.clearButton = QtWidgets.QPushButton("Отмена")
        self.clearButton.clicked.connect(self.clear)
        self.clearButton.setEnabled( False )
        #Кнопка сохранения значения
        self.saveButton = QtWidgets.QPushButton("Сохранить")
        self.saveButton.clicked.connect(self.save)
        self.saveButton.setEnabled( False )
    def setMatrix( self ):
        ''' Заполняем матрицу'''
        count = len(self.__obj.matrix.values)
        for i in range(count):
            for j in range(count):
                value = self.objmatrix.values[i][j]
                item=QtWidgets.QTableWidgetItem()
                item.setText(str(value))
                if i == j:
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.matrix.setItem(i, j, item)
            value = self.objmatrix.mainVector[i]
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(value))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.vector.setItem(i, 0, item)
    def setHeaders( self ):
        """ Объявляет заголовки """
        headers = [obj.name for obj in self.__obj.sub_objects]
        #Устанавливаем заголовки в матрице
        self.matrix.setHorizontalHeaderLabels(headers)
        self.matrix.setVerticalHeaderLabels(headers)
        #Устанавливаем заголовки в векторе
        self.vector.setVerticalHeaderLabels(headers)
        self.vector.setHorizontalHeaderLabels([" "])
    def setSize( self ):
        """ Задает размеры матрицы и вектора"""

        self.matrix.setFixedWidth(600)
        
        self.vector.setFixedWidth(300)
        
        self.vector.horizontalHeader().setStretchLastSection( True )
        
    
    def clear( self ):
        """ Отменяет изменения в матрице, возвращая все значения исходной """
        self.matrix.cellChanged.disconnect()
        self.objmatrix = copy(self.__obj.matrix)
        self.setMatrix()
        self.matrix.cellChanged.connect(self.is_changed)
        self.changeButtonsMode( False )
    def changeButtonsMode( self, mode ):
        """ Меняет доступность кнопок """
        self.clearButton.setEnabled( mode )
        self.saveButton.setEnabled( mode )
    def save( self ):
        """ Сохраняет матрицу """
        self.__obj.matrix = self.objmatrix
        self.changeButtonsMode( False )
    
    def is_changed( self, row, col ):
        """ Обновляет матрицу при изменении ее элемента """
        #Отделяем сигнал изменения от функции
        self.matrix.cellChanged.disconnect()
        
        try:
            #Считываем значение из измененной ячейки
            value = float(self.matrix.item( row, col ).data(2))
            #В противоположную ячейку вставляем обратное значение
            diagonal_value = QtWidgets.QTableWidgetItem()
            diagonal_value.setText(str(1/value))
            #вставляем значение в матрицу
            self.matrix.setItem(col, row, diagonal_value)
        except TypeError:
            #Если был введен текст, ставим вместо него единицу
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(1.0))
            self.matrix.setItem( row, col, item )
        except ZeroDivisionError:
            #Если был введен 0, тоже ставим единицу
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(1.0))
            self.matrix.setItem( row, col, item )
        
        #Пересчитываем значения матрицы и вектора
        self.recalculate()
        #Присоединяем к сигналу функцию
        self.matrix.cellChanged.connect(self.is_changed)
        #Изменяем режим кнопок на активные (делаем возможными сохранение и отмену)
        self.changeButtonsMode( True )
        
    def recalculate( self ):
        """ Считывает все значения таблицы и обновляет матрицу  """
        count = self.matrix.rowCount()
        # В массив значений вставляем значения со всех линий
        values = []
        for i in range(count):
            line = []
            for j in range(count):
                line += [str( self.matrix.item(i, j).data(2))]
            values.append(line)
        #Переносим значения в матрицу
        self.objmatrix=Matrix(values)
        
        #Обновляем вектор значений
        for i in range(count):
            item=QtWidgets.QTableWidgetItem()
            item.setText(str(self.objmatrix.mainVector[i]))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.vector.setItem(i, 0, item)
        
