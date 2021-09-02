#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 18:25:26 2021

@author: bloisejuli
"""
# busqueda_en_listas.py

#%%

# Ejercicio 4.3:
# Escribir una función buscar_u_elemento() que reciba una lista y un elemento y devuelva la posición de la 
# última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).

def buscar_u_elemento(lista, elemento):
    i = 0
    posicion = -1
    while i < len(lista): 
        if lista[i] == elemento:
            posicion = i
        i += 1
    return posicion

def buscar_n_elementos(lista, elemento):
    i=0
    posicion = -1
    cantidad = 0
    while i < len(lista):
        if lista[i] == elemento:
            posicion = i
            cantidad += 1
        i += 1
    return posicion, cantidad

#%%

# Ejercicio 4.4:
# Crear una función maximo() que busque el valor máximo de una lista de números 
# positivos.

def maximo(lista):
    i = 0
    m = lista[0]
    while i < len(lista): 
        if m < lista[i]:
            m = lista[i]
        i += 1
    return m
    
def minimo(lista):    
    i = 0
    m = lista[0]
    while i < len(lista): 
        if m > lista[i]:
            m = lista[i]
        i += 1
    return m
    
    