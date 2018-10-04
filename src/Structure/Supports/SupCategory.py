#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from .Matrix import *
from .Support import *
from .SupCriteria import *
from copy import copy

class SupCategory( Support ):
    """ Рассчетная вспомогательная категория """
    def __init__( self, category, criterias=None, matrix=None ):
        #Если первый аргумент не является категорией, выкидываем ошибку
        if type(category) is not Category:
            raise ValueError( " Передана не категория " )
        #Инициализируем базовый класс, передавая  категорию, критерии и матрицу
        super().__init__(category, criterias, matrix)
        
        
    #######################################################################
    
    @property
    def sub_objects( self ):
        return super().sub_objects
    @sub_objects.setter
    def sub_objects( self, new_criterias ):
        if new_criterias is not None:
            #Проверяем переданные критерии на тип
            for criteria in new_criterias:
                if type(criteria) is not SupCriteria:
                    raise ValueError( " Один или несколько переданных элементов не является вспомогательным критерием " )
                    
        Support.sub_objects.__set__(self, new_criterias)
        
    @property
    def base_object( self ):
        return super().base_object
    @base_object.setter
    def base_object( self, new_category ):
        #Проверяем базовый объект на тип
        if type(category) is not Category:
            raise ValueError( " Передана не категория " )
        Support.base_object.__set__( self, new_category )
    
    @property
    def alternatives( self ):
        #Объявляем словарь
        result = {}
        #Проходим по каждой альтернативе каждой критерии
        for criteria in self.sub_objects:
            for alternative in criteria.sub_objects:
                #Если альтернатива содержится в словаре, добавляем к элементу произведение веса критерия и веса альтернативы
                if alternative in result:
                    result[ alternative ] += self.sub_objects_masses[ criteria ] * criteria.sub_objects_masses[ alternative ]
                #Или добавляем это произведение как значение альтернативы.
                else:
                    result.update({alternative:self.sub_objects_masses[criteria ] * criteria.sub_objects_masses[ alternative ]})
        return result
    
    ########################################################################
    
    def add_sub_object( self, new_criteria ):
        #Проверяем тип критерия и добавляет его в список
        temple = new_criteria
        if type(new_criteria) is Criteria:
            temple = SupCriteria(new_criteria)
        elif type(new_criteria) is not SupCriteria:
            raise ValueError( " Один или несколько переданных элементов не является вспомогательным критерием " )
        super().add_sub_object(temple)
        
    def clear( self ):
        self.sub_objects = None
            
