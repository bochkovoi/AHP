#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from .MatrixErrors import *

class Matrix( object ):
    """ Матрица иерархии Саати """
    def __init__(self, matrix):
        #Проверяем, во всех ли строках количество элементов совпадает с количеством строк
        for line in matrix:
            if len(matrix) != len(line):
                raise SizeError("Ошибка размеров матрицы!")
            
        #Преобразуем матрицу в массив
        matrix=np.asarray(matrix, dtype=np.float64)
        #Объявляем обратную матрицу
        transpose = matrix.transpose()
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 1/transpose[i][j]:
                    raise ValueError("Ошибка: матрица не обратно диагональна!")
        
        #Объявляем матрицу
        self.__matrix = matrix
    
    ##########################
    @property
    def values(self):
        """ Возвращает массив значений матрицы матрицы """
        return self.__matrix
    @property
    def mainVector(self):
        """Возвращает определяющий вектор матрицы """
        
        def is_good(vector, epsilon):
            """Возвращает истину, если каждый элемент матрицы меньше заданного значения"""
            for element in vector:
                if element > epsilon:
                    return False
            return True
        
        def to_vector(mat):
            """ Преобразует матрицу в вектор """
            sum_elements=np.sum(mat)            # Сумма всех элементов
            res=[]                                                            # Изначально, результат - пустой вектор
            for line in mat:
                sum_line=np.sum(line)           
                res = np.append(res, sum_line/sum_elements)
            return res
        
        A = self.__matrix
        B = self.__matrix @ self.__matrix
        #Разница между элементами двух векторов длжна быть меньше установленного значения (0.0001)
        while not(is_good(to_vector(B)-to_vector(A), 0.0001)):      
            A=B
            B=B @ self.__matrix
        return to_vector(B)

    ##########################

