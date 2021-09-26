#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:28:50 2021

@author: bloisejuli
"""

# random_walk.py

#%%

# Ejercicio 7.12: Caminatas al azar
#    1.  Modificá el código anterior para ponerles nombres a los ejes ("tiempo" y distancia al origen") y al gráfico.
#    2.  Graficá 12 trayectorias en la misma figura, con diferentes colores.
#    3.  Usá la estructura de subplots sugerida en el Ejercicio 7.11 para graficar tres pubplots en una figura:
#            Arriba, grande, 12 trayectorias aleatorias como en el inciso anterior
#            Abajo a la izquierda la trayectoria que más se aleja del origen.
#            Abajo a la derecha la trayectoria que menos se aleja del origen.

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''Simula una caminata'''
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


def graficar_randomwalk(pasos=100000):
    '''Graficá 12 trayectorias de caminatas simuladas en la misma figura, con diferentes colores.'''
    caminatas = [randomwalk(10000) for _ in range(12)]
    
    lista_abs = [abs(paso.mean()) for paso in caminatas]
    index_max = lista_abs.index(max(lista_abs))
    index_min = lista_abs.index(min(lista_abs))

    plt.subplot(2, 1, 1)
    plt.title("12 Caminatas al azar")
    for i in range(12):
        plt.plot(caminatas[i])
        plt.ylim(-250.0, 250.0)

    plt.subplot(2, 2, 3)
    plt.title("La caminata que más se aleja")
    plt.plot(caminatas[index_max])
    plt.ylim(-250.0, 250.0)
    plt.subplot(2, 2, 4)
    plt.title("La caminata que más se menos")
    plt.plot(caminatas[index_min])
    plt.ylim(-250.0, 250.0)

    plt.show()
