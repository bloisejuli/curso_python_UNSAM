#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:36:09 2021

@author: bloisejuli
"""

# plot_bbin_vs_bsec.py

#%%

# Ejercicio 6.20: Búsqueda binaria vs. búsqueda secuencial
# En este Ejercicio vamos a rehacer los gráficos del ejemplo anterior, pero primero cambiando el algoritmo de búsqueda y luego comparando ambos algoritmos.

import random
import matplotlib.pyplot as plt 
import numpy as np

def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    repeticiones = 0
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        repeticiones += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, repeticiones


def generar_lista(n, m):
    ''' Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1'''
    l = random.sample(range(m), k = n)
    l.sort()
    return l


def generar_elemento(m):
    '''devuelve un elemento aleatorio entre 0 y m-1.'''
    return random.randint(0, m-1)


def experimento_secuencial_promedio(lista, m, k):
    ''' Devuelve la cantidad de comparaciones promedio en k experimentos elementales.'''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista,m,k):
    ''' Cuenta la cantidad de comparaciones que realiza en promedio (entre k experimentos elementales) 
    la búsqueda binaria sobre la lista pasada como parámetro.'''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def grafica_complejidad_busqueda_lineal(m=10000, k=1000):
    largos = np.arange(256)+1 #estos son los largos de listas que voy a usar
    comps_promedio = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    
    for i, n in enumerate(largos):
        lista = generar_lista(n,m) # genero lista de largo n
        comps_promedio[i] = experimento_secuencial_promedio(lista,m,k)
    
    #ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio,label='Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaiciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()


def grafica_complejidad_busqueda_binaria(m=10000, k=1000):
    largos = np.arange(256)+1 #estos son los largos de listas que voy a usar
    comps_promedio = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    
    for i, n in enumerate(largos):
        lista = generar_lista(n,m) # genero lista de largo n
        comps_promedio[i] = experimento_binario_promedio(lista,m,k)
    
    #ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio,label='Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaiciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()

def grafica_complejidad_binaria_vs_lineal():
    '''Genere un experimento y su gráfico, donde se comparan los algoritmos de búsqueda lineal y binaria.'''
    grafica_complejidad_busqueda_lineal()
    grafica_complejidad_busqueda_binaria()
    plt.title('Complejidad Binaria vs Lineal')

#%%
def main():
    grafica_complejidad_binaria_vs_lineal()
