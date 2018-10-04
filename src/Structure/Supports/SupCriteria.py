#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Matrix import *
from .Support import *
from Elements import *

class SupCriteria( Support ):
    """ Рассчетный вспомогательный критерий, определяющий веса альтернатив """
    def __init__( self, criteria, alternatives=None, matrix=None):
        #Проверяем критерий на тип
        if type(criteria) is not Criteria:
            raise ValueError( " Переданный параметр не является критерием " )
        super().__init__(criteria, alternatives, matrix)
    
    ############################
    
    @property
    def sub_objects( self ):
        return super().sub_objects
    @sub_objects.setter
    def sub_objects( self, new_alternatives ):
        for alternative in new_alternatives:
            if type(alternative) is not Alternative:
                raise ValueError( " Один или несколько переданных параметров в списке не являются альтернативами  " )
        Support.sub_objects.__set__(self, new_alternatives)
        
    @property
    def base_object( self ):
        return super().base_object
    @base_object.setter
    def base_object( self, new_criteria ):
        if type(new_criteria) is not Criteria:
            raise ValueError( " Переданный параметр не является критерием " )
        Support.base_object.__set__( self, new_criteria )

    ############################

    def add_sub_object( self, new_object ):
        ''' Добавляет объект в список подчиненных '''
        self.sub_objects = dict.fromkeys(list(self.sub_objects) + [new_object], 0)
        self.set_ones_matrix()
