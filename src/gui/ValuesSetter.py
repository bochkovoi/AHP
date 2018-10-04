#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from SizeFunctions import sizeTable
import sys, os
a=os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'Structure', 'Supports')
print(os.path.normpath(a))
sys.path.append(a)
from Matrix import Matrix

class ValuesSetter( QtWidgets.QWidget ):
    """ Окно редактирования матрицы """
    def __init__( self, obj_names=None, parent=None ):
        #
        super().__init__( parent )
        #
        obj_count = len(obj_names)
        #
        self.first_table = QtWidgets.QTableWidget(obj_count, obj_count)
        self.second_table = QtWidgets.QTableWidget(obj_count, 1)
        #
        self.first_table.setVerticalHeaderLabels(obj_names)
        self.first_table.setHorizontalHeaderLabels(obj_names)
        #
        self.second_table.setVerticalHeaderLabels( obj_names )
        self.second_table.setHorizontalHeaderLabels( ['Значения'] )
        #
        for i in range(self.first_table.columnCount()):
            for j in range(self.first_table.rowCount()):
                if i == j:
                    #
                    a=QtWidgets.QTableWidgetItem()
                    a.setText(str(1))
                    self.first_table.setItem(i,j,a)
                    
                    self.first_table.item(i,j).setFlags(QtCore.Qt.ItemIsEnabled)
                else:
                    #
                    a=QtWidgets.QTableWidgetItem()
                    a.setText('')
                    self.first_table.setItem(i,j,a)
        
        #
        self.first_table.setMinimumSize(sizeTable( self.first_table ))
        self.second_table.setMinimumSize(sizeTable( self.second_table ))
        #
        self.first_table.setMaximumSize(sizeTable( self.first_table ))
        self.second_table.setMaximumSize(sizeTable( self.second_table ))
        #
        self.first_table.cellChanged.connect(self.is_changed)
        #
        calculate_button = QtWidgets.QPushButton('Рассчитать')
        calculate_button.clicked.connect(self.calculate)
        exit_button = QtWidgets.QPushButton('Отмена')
        
        buttons = QtWidgets.QHBoxLayout()
        
        buttons.addWidget(calculate_button)
        buttons.addWidget(exit_button)
        
        box=QtWidgets.QFormLayout()
        box.addRow(self.first_table, self.second_table)
        box.addRow(buttons)
        self.setLayout(box)
    def is_changed(self, row, col):
        try:
            reading = float(self.first_table.item(row, col).data(2))
            alter_item = QtWidgets.QTableWidgetItem()
            alter_item.setText(str(1/reading))
            self.first_table.setItem(col, row, alter_item)
        except ValueError:
            a = self.first_table.item(col, row).data(2)
            if a == '':
                a = 1.0
            a=1/float(a)
            a = QtWidgets.QTableWidgetItem(str(a))
            self.first_table.setItem(row, col, a)
        except ZeroDivisionError:
            err = QtWidgets.QTableWidgetItem()
            err.setText('1')
            self.first_table.setItem(row, col, err)
    def calculate( self ):
        pass
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = ValuesSetter( obj_names = [str(x) for x in range(10)] )
    
    window.show()
    
    #print(window.first_table.columnCount())
    #print(window.second_table.columnCount())
    
    #print(window.first_table.rowCount())
    #print(window.second_table.rowCount())
    
    #print(window.first_table.size())
    #print(window.second_table.size())
    
    for i in range(window.first_table.columnCount()):
        print(window.first_table.columnWidth(i))
    for i in range(window.first_table.rowCount()):
        print(window.first_table.rowHeight(i))
    sys.exit(app.exec_())
        
