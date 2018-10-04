#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from .VisObject import *

class ChangeVisObject( VisObject ):
    """ Окно изменения объекта """
    def __init__( self, obj, supObj=None, parent=None ):
        super().__init__( obj, parent=parent )
        
        #Задаем объект, базовый к изменяемому
        self.main_obj = supObj
        
        #Добавляем две кнопки: для сохранения и отмены изменений
        saveButton = QtWidgets.QPushButton( "Сохранить" )
        saveButton.clicked.connect( self.save )
        retButton = QtWidgets.QPushButton( "Отмена" )
        retButton.clicked.connect( self.exit )
        
        #Добавляем надписи
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(saveButton)
        layout.addWidget(retButton)
        self.form.addRow(layout)
        self.setLayout( self.form )
        
    def is_good_name( self ):
        """ Проверяем имя на адекватность """
        if self.name.text().strip(' ') == '':
            #Если имя состоит из пробелов или пустое, выводим ошибку
            window = QtWidgets.QMessageBox.critical(self, "Ошибка имени", "Поле ввода не должно быть пустым", defaultButton=QtWidgets.QMessageBox.Ok)
            self.name.setText(self.elem.name)
            return False
        else:
            return True
            
    def save( self ):
        ''' Заменяем старые имя и описание на новые '''
        new_name = self.name.text().strip(' ')
        self.elem.name = new_name
        new_description = self.text.toPlainText()
        self.elem.description = new_description
        
    def rollback( self ):
        ''' Заменяем текст в окнах на имя и описание элемента '''
        self.name.setText( self.elem.name )
        self.text.setText( self.elem.description )
    
    def exit( self ):
        """ Выходим, делая активными родительские окна """
        try:
            self.parent().is_changed.emit()
            try:
                self.parent().parent().setEnabled(True)
            except AttributeError:
                self.parent().setEnabled(True)
                
        except AttributeError:
            QtWidgets.qApp.quit()
        self.destroy()

