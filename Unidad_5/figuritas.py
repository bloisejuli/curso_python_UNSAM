#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:20:21 2021

@author: bloisejuli
"""

# figuritas.py

# Datos:

#    Álbum con 670 figuritas.
#    Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#    Cada paquete trae cinco figuritas.

import random
import numpy as np

#%%

# Ejercicio 5.10: Crear

def crear_album(figus_total):
    '''Crea un array con la cantidad de figuritas que tiene el album '''
    return (np.zeros(figus_total, dtype=int))

#%%

# Ejercicio 5.11: Incompleto

def album_incompleto(A):
    ''' Recibe un album y devuelve True si el album esta incompleto y False si esta completo '''
    return (0 in A)

#%%

# Ejercicio 5.12: Comprar

def comprar_figu(figus_total):
    ''' Recibe el número total de figuritas que tiene el album y devuelve un número entero aleatorio que representa la figurita que nos toco'''
    return (np.random.randint(0,figus_total))

#%%

# Ejercicio 5.13: Cantidad de compras

def cuantas_figus(figus_total):
    ''' Recibe el tamaño del album y devuelve la cantidad de figuritas que se debieron comprar para para completarlo '''
    album = crear_album(figus_total)
    cant_figus = 0
    
    while (album_incompleto(album)):
        album[comprar_figu(figus_total)-1] += 1
        cant_figus += 1
        
    return cant_figus

#%% 

# Ejercicio 5.14: 

def estimar_figus_a_comprar(n_repeticiones = 1000, figus_total = 6):
    ''' Ejecutá n_repeticiones = 1000 veces utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en cada repetición. 
    Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas. '''
    lista_cantidad_figus = np.array([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    return round(lista_cantidad_figus.mean())

#%%

# Ejercicio 5.15:

def experimento_figus(n_repeticiones, figus_total):
    ''' Ejecutá n_repeticiones utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en cada repetición. 
    Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de figuritas. '''
    lista_cantidad_figus = np.array([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    return round(lista_cantidad_figus.mean())

# -----------------------------
# input: experimento_figus(100, 670)
# output: 4717