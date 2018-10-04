#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Matrix import *

class Support( object ):
    """ Вспомогательный объект, производящий все вычисления с подчиненными объектами (у категории это критерии, у критериев это альтернативы"""
    def __init__( self, base_object, sub_objects_list=None, sub_objects_matrix=None ):
        
        #Задаем базовый объект
        self.__base_object = base_object
        #Из списка подчиненных объектов составляем словарь, значения которого изначально заполнены нулями
        #Проверяем переданный лист подчиненных объектов на наличие
        if sub_objects_list is None or sub_objects_list == []:
            sub_objects_list=[]
            self.__matrix = None
        #Проверяем введенную матрицу на соответствие количества элементов количеству подчиненных объектов или заполняем ее единицами
        self.__sub_objects = dict.fromkeys(sub_objects_list, 0)
        if sub_objects_matrix is None:
            self.set_ones_matrix()
        elif len(sub_objects_matrix.values) != len(sub_objects_list):
            raise ValueError( " Количество строк в таблице не соответствует количеству подчиненных объектов " )
        else:
            self.__matrix = sub_objects_matrix
            self.recalculate()
    ###########################
    
    @property
    def base_object( self ):
        return self.__base_object
    @base_object.setter
    def base_object( self, new_object ):
         self.__base_object = new_object
    
    @property
    def sub_objects( self ):
        return list(self.__sub_objects.keys())
    @sub_objects.setter
    def sub_objects( self, new_objects ):
        """ Если параметр является None, то объявляем список объектов в пустой, а матрицу делаем None """
        if new_objects is None or new_objects == []:
            self.__sub_objects = dict.fromkeys( [], 0)
            self.__matrix = None
        else:
            self.__sub_objects = dict.fromkeys( new_objects, 0)
            self.set_ones_matrix()
        
    @property
    def matrix( self ):
        return self.__matrix
    @matrix.setter
    def matrix( self, new_matrix ):
        #Проверяем матрицу
        if len(new_matrix.values) != len(self.sub_objects):
            raise ValueError( " Количество строк в таблице не соответствует количеству подчиненных объектов " )
        self.__matrix = new_matrix
        self.recalculate()
        
    @property
    def sub_objects_masses( self ):
        return self.__sub_objects
    
    @property
    def name( self ):
        return self.base_object.name
    @name.setter
    def name( self, new_name ):
        self.base_object.name = new_name
        
    @property
    def description( self ):
        return self.base_object.description
    @description.setter
    def description( self, new_descr ):
        self.base_object.description = new_descr
        
    ###########################
    
    def recalculate( self ):
        """ Пересчитывает значения подчиненных объектов """
        if self.__sub_objects == {}:
            pass
        else:
            vector = self.__matrix.mainVector
            self.__sub_objects = dict(zip(self.sub_objects, vector))

    def add_sub_object( self, new_object ):
        ''' Добавляет объект в список подчиненных '''
        self.sub_objects = dict.fromkeys(list(self.sub_objects) + [new_object], 0)
        self.set_ones_matrix()
        
    def set_ones_matrix( self ):
        """ Заполняет матрицу единицами """
        self.__matrix = Matrix( [[1 for x in self.__sub_objects] for y in self.__sub_objects]  )
        self.recalculate( )
        
