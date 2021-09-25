#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:00:35 2021

@author: bloisejuli
"""
# informe.py

#%% 
# Ejercicio 12:
# modifica el archivo costo_camion.py del 3.9 para que use la función informe_funciones.leer_camion() del programa informe_funciones.py.
 
import informe_funciones
import csv

def costo_camion(nombre_archivo):
    ''' A partir de un archivo calcula el costo total del camion'''
    costo_total = 0
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)

    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')

    f.close()
    return costo_total

#%%

def main():
    archivo_camion = '../Data/camion.csv'
    precios_camion = informe_funciones.leer_camion(archivo_camion)
    camion = costo_camion(archivo_camion)

    print('Costo del camion:', camion)
