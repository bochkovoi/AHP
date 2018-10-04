#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets,QtCore
import sys, os.path as op
path1 = op.join( op.abspath(op.dirname(__file__)), '..', 'Structure')
path2 = op.join( op.abspath(op.dirname(__file__)), '..')
sys.path.append(path1)
sys.path.append(path2)
from Structure import *
from SubCriteriasVision import *
from MatrixAppend import *

class MainValuesWindow( QtWidgets.QWidget ):
    """ """
    def __init__( self, category, parent=None ):
        self.__obj = category
        super().__init__( parent, QtCore.Qt.Window )
        self.initUI()
        
    def initUI( self ):
        
        self.objects_list = QtWidgets.QListWidget()
        self.exitButton = QtWidgets.QPushButton("Назад")
        self.exitButton.clicked.connect( self.exit )
        
        alternatives = self.__obj.alternatives
        for criteria in alternatives:
            value = (alternatives[criteria] *10000 //1) / 10000
            item = QtWidgets.QListWidgetItem()
            item.setText(criteria.name + ': ' + str(value))
            self.objects_list.addItem(item)
        
        form = QtWidgets.QFormLayout()
        form.addRow(self.objects_list)
        form.addRow(self.exitButton)
        self.setLayout( form )
        
    def exit( self ):
        try:
            self.parent().setEnabled(True)
                
        except AttributeError:
            QtWidgets.qApp.quit()
        self.destroy()
        
            
        
