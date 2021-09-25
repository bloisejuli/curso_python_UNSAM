#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:56:28 2021

@author: bloisejuli
"""

# termometro.py

#%%

# Ejericio 5.8:
# Ampliá el código de la función medir_temp(n) en tu archivo termometro.py que escribiste en el Ejercicio 5.6 para que además de devolver 
# las temperaturas simuladas, guarde el vector con estas temperaturas en el directorio Data de tu carpeta de ejercicios, en un archivo 
# llamado temperaturas.npy. Hacé que corra n = 999 veces.

import random
import numpy as np

def medir_temp(n):
    temperaturas = []
    for i in range(n):
        error = random.normalvariate(0, 0.2)
        temperatura = 37.5 + error
        temperaturas.append(temperatura)
        
    temps = np.array(temperaturas)
    np.save('../Data/temperaturas', temps)
    
    return temps


def resumen_temp(n):
    temperaturas = medir_temp(n)
    
    maxima = round(temperaturas.max(), 2)
    minima = round(temperaturas.min(), 2)

    promedio = round(temperaturas.sum()/n, 2)
    mediana = round(np.median(temperaturas), 2)

    return(maxima, minima, promedio, mediana)

#%%

def main():
    n = 99
    (maxima, minima, promedio, mediana) = resumen_temp(n)
