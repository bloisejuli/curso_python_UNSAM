#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:21:19 2021

@author: bloisejuli
"""

# fileparse.py

#%% 
# Ejercicio 6.9: Trabajando sin encabezados
# Modificá la función parse_csv() de ejercicios anteriores de forma que (opcionalmente) pueda trabajar con archivos  sin encabezados, 
# creando tuplas en lugar de diccionarios.

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)
        
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if select and has_headers:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = [] 
       
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
             
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
            registros.append(registro)

    return registros     
