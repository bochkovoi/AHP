#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Elements import *
from Supports import *
from copy import copy

class MainObject( object ):
    ''' Основной объект иерархии '''
    def __init__(self, criterias=None, alternatives=None, is_simple=True):
        #Проверяем правильность переданных параметров
        if criterias is None:
            criterias = []
        else:
            for criteria in criterias:
                if type(criteria) is not Criteria:
                    raise TypeError( " Один или несколько элементов в списке не является критерием " )
        if alternatives is None:
            alternatives = []
        else:
            for alternative in alternatives:
                if type(alternative) is not Alternative:
                    raise TypeError( " Один или несколько элементов в списке не является альтернативой " )
        #Объявляем данные
        self.__criterias = criterias
        self.__alternatives = alternatives
        self.__is_simple = is_simple
        
        #Объявляем данные категорий: риска, возможностей, издержек и выгод
        
        risk = Category("Риск", "Категория, учитывающая возможные риски при выборе той или иной альтернативы. При сравнении элементов в плане рисков следует спросить, чем одна категория рискованнее другой в плане рассматриваемого критерия")
        possibility = Category("Возможность", "Категория, учиывающая возможности при выборе альтернативы. При сравнении альтернатив в этой категории следует отвечать на вопрос, во сколько раз первая альтернатива предоставляет больше возможностей, чем другая по заданному критерию")
        costs = Category("Издержки", "Категория, учитывающая издержки при выборе альтернативы. При сравнении двух альтернатив по критерию из этой категории следует спросить, во сколько раз первая альтернатива более затратна, чем вторая")
        profit = Category("Выгоды", "Категория, учитывающая выгоды при выборе альтернативы. При сравнении двух альтернатив по критерию из этой категории следует спросить, во сколько раз первая альтернатива более выгдна по данному критерию, чем вторая")
        
        
        self.__risk = SupCategory( risk )
        self.__possibility = SupCategory( possibility )
        self.__costs = SupCategory( costs )
        self.__profit = SupCategory( profit )
        
        self.update()
        
    ###########################
    
    @property
    def criterias( self ):
        return self.__criterias
    @criterias.setter
    def criterias( self, new_list ):
        self.__criterias = new_list
        self.update()
    
    @property
    def alternatives( self ):
        return self.__alternatives
    @alternatives.setter
    def alternatives( self, new_values ):
        self.__alternatives = new_values
        self.update()
    
    @property
    def is_simple( self ):
        return self.__is_simple
    @is_simple.setter
    def is_simple( self, new_value ):
        if type(new_value) is not bool: 
            raise TypeError( "Значение должно быть True/False" )
        self.__is_simple = new_value
    
    @property
    def risk( self ):
        return self.__risk
    @property
    def possibility( self ):
        return self.__possibility
    @property
    def costs( self ):
        return self.__costs
    @property
    def profit( self ):
        return self.__profit
    
    @property
    def main_values( self ):
        try:
            if self.is_simple:
                result = {alter:self.profit.alternatives[alter]/self.costs.alternatives[alter] for alter in self.alternatives}
            else:
                result = {alter:self.profit.alternatives[alter]*self.possibility.alternatives[alter]/(self.costs.alternatives[alter]*self.risk.alternatives[alter]) for alter in self.alternatives}
        except:
            result={alter:0 for alter in self.alternatives}
        return result
        
    ###########################
    
    def add_alternative( self, new_alternative ):
        self.alternatives += [new_alternative]
        self.update()
    
    def add_criteria( self, new_criteria ):
        self.__criterias += [new_criteria]
        self.update()
        
    def update( self ):
        
        supList = [ SupCriteria( criteria, self.alternatives ) for criteria in self.criterias ]
        
        for category in [self.risk, self.possibility, self.costs, self.profit]:
            category.sub_objects = supList
        
        
    def vis( self ):
        #Показывает содержимое в объекте
        for criteria in self.__criterias:
            print(criteria.name)
            print(criteria.description)
        for alternative in self.__alternatives:
            print(alternative.name)
            print(alternative.description)
        
        for category in [self.risk, self.possibility, self.costs, self.profit]:
            print(category.name)
            print()
            a=0
            print(category.matrix.values)
            for criteria in category.sub_objects:
                print('    ' + criteria.name)
                print()
                for alternative in criteria.sub_objects:
                    print('        ' + alternative.name)
                print()
                print(criteria.matrix.values)
                print( category.sub_objects[0].matrix is criteria.matrix )
                a=criteria.matrix
                print('-'*40)
            
    def change_mode( self ):
        #Изменяет режим 
        self.is_simple = not self.is_simple
        
