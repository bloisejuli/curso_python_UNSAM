#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:09:09 2021

@author: bloisejuli
"""

# bbin.py

#%% 
# Ejercicio 6.15:
# Usando lo que hiciste en el Ejercicio 6.14, agregale al archivo bbin.py una función insertar(lista, x) que reciba una lista ordenada 
# y un elemento. Si el elemento se encuentra en la lista solamente devuelve su posición; si no se encuentra en la lista, lo inserta en 
# la posición correcta para mantener el orden. En este segundo caso, también debe devolver su posición.


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos


def donde_insertar(lista, x):
    i = 0
    try:
        while lista[i] < x:
            i += 1
    except IndexError:
        i = i
        
    return i


def insertar(lista, x):
    pos = busqueda_binaria(lista,x)
    if (busqueda_binaria(lista, x) == -1):
        pos = donde_insertar(lista,x)
        lista.insert(pos, x)
            
    return pos
            
            
            