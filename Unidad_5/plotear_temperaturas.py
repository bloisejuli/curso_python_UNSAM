#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:20:59 2021

@author: bloisejuli
"""

# plotear_temperaturas.py

#%%

# Ejercicio 5.9: 
# Escribí una función plotear_temperaturas() en un archivo plotear_temperaturas.py que lea el archivo de datos temperaturas.npy 

import numpy as np
import matplotlib.pyplot as plt 

def muestra_histograma(arch_temperaturas):
    temperaturas = np.load(arch_temperaturas)
    plt.hist(temperaturas, bins= 25)
    plt.show()

def main():
    muestra_histograma('../Data/temperaturas.npy')
