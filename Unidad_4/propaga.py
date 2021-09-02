#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 20:47:58 2021

@author: bloisejuli
"""

# propaga.py

#%%

# Ejercicio 4.6:
# Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, 
# prendidos fuego o ya gastados (carbonizados). Representaremos esta situación con una lista L con un elemento 
# por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se 
# propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos 
# carbonizados no se encienden nuevamente.

# Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que 
# los 1's se propagaron a sus vecinos con 0. 

def propagar(lista): 
    nuevo = 0
    encendido = 1
    i = 0
    while i < len(lista): # Recorre a derecha
        k = i +1
        if lista[i] == encendido: 
            if  k < len(lista) and lista[k] == nuevo:
                lista [k] = encendido           
        i += 1
    
    j = len(lista) -1
    while j > 0: # Recorre a izquierda
        l = j -1
        if lista[j] == encendido:
            if l >= 0 and lista[l] == nuevo:
                lista[l] = encendido  
        j -= 1
    return lista

#--------------------------------------------
# input: propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# output: [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]

# input: propagar([ 0, 0, 0, 1, 0, 0])
# output: [1, 1, 1, 1, 1, 1]