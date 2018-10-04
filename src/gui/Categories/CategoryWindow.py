#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', '..')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
sys.path.append(path1)
sys.path.append(path2)
from SubCriteriasVision import *
from MatrixAppend import *
from .MainValuesWindow import *

class CategoryWindow( QtWidgets.QWidget ):
    """ Окно категории """
    def __init__( self, category, parent=None ):
        
        super().__init__( parent, QtCore.Qt.Window )
        
        self.__category = category
        self.initUI()
    
    def initUI( self ):
        """ Инициализируем окно """
        
        #Объявляем матрицу и список критериев
        self.matrix = MatrixAppend(self.__category, parent=self)
        self.criterias = SubCriteriasVision(self.__category,  parent=self)
        
        #Добавляем кнопки описания категории, вектора значений и возврата на главное окно
        moreButton = QtWidgets.QPushButton("Подробнее о категории")
        moreButton.clicked.connect( self.more )
        mainVectorButton = QtWidgets.QPushButton("Вектор значений альтернатив")
        mainVectorButton.clicked.connect( self.mainVector )
        exitButton = QtWidgets.QPushButton("Назад")
        exitButton.clicked.connect( self.exit )
        
        #Добавляем заголовки
        criterias_label = QtWidgets.QLabel("Сравниваемые критерии")
        criterias = QtWidgets.QVBoxLayout()
        criterias.addWidget(criterias_label)
        criterias.addWidget(self.criterias)
        
        #Объявляем форму и располагаем ее в окне
        form = QtWidgets.QFormLayout()
        form.addRow( self.matrix, criterias )
        form.addRow(mainVectorButton)
        form.addRow(moreButton)
        form.addRow(exitButton)
        self.setLayout( form )
        
    def red_criteria( self ):
        ''' Вызывает метод показа окна редактирования критерия из списка критериев'''
        self.criterias.isDoubleClicked(self.criterias.sub_objs.currentItem())
    
    def more( self ):
        """ Создает окно просмотра категории без возможности его изменения """
        more_win = SimpleVisObject( self.__category, parent=self )
        more_win.setWindowTitle("О категории")
        more_win.show()
    
    def mainVector( self ):
        """ Создает окно, отображающее вектор значений категории """
        vector_window = MainValuesWindow( self.__category, parent=self )
        vector_window.setWindowTitle("Значения альтернатив для данной категории")
        vector_window.setWindowFlags( vector_window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        vector_window.show()
        self.setEnabled(False)
        vector_window.setEnabled( True )
    
    def exit( self ):
        """ Делает все окна активными и обновляет основное окно """
        try:
            self.parent().parent().setEnabled(True)
            self.parent().is_changed.emit()
                
        except AttributeError:
            QtWidgets.qApp.quit()
        self.destroy()
        
