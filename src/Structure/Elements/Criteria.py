#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Element import *

class Criteria( Element ):
    """ Класс критериев сравнения иерархии """
    def __init__( self, name, description='' ):
        super().__init__( name, description )
