#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore

def sizeTable( qTableObject ):
    ''' Возвращает объект QSize с габаритами таблицы '''
    #В качестве изначальных размеров задаем высоту горизонтальных заголовков+2 и ширину вертикальных заголовков+2
    h = qTableObject.horizontalHeader().height()+5
    w = qTableObject.verticalHeader().width()+5
    print(w)
    #
    for i in range(qTableObject.rowCount()):
        h += qTableObject.rowHeight(i)+10
    for i in range(qTableObject.columnCount()):
        w += (qTableObject.columnWidth(i)+15)
    #
    return QtCore.QSize(w, h)
    
    
