#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:44:44 2021

@author: bloisejuli
"""

# invlista.py

#%%

# Ejercicio 4.5:
# Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero 
# en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la 
# lista de salida y análogamente con los demás elementos.

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e] + invertida
    return invertida

#--------------------------------------------
# input: invertir_lista([1, 2, 3, 4, 5])
# output: [5, 4, 3, 2, 1]

# input: invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
# output: ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']