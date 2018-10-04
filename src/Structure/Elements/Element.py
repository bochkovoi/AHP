#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Element( object ):
    """ Базовый класс элементов """
    def __init__( self, name, description=''):
        self.__name=name
        self.__description=description
    
    #########################
    
    @property
    def name( self ):
        return self.__name
    @name.setter
    def name( self, new_name ):
        self.__name = new_name
        
    @property
    def description( self ):
        return self.__description
    @description.setter
    def description( self, new_description ):
        self.__description = new_description
    
    ##########################
    
    
