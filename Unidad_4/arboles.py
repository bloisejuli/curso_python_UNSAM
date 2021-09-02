#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:39:33 2021

@author: bloisejuli
"""
#arboles.py

import csv

#%% 

# Ejercicio 4.15: Lectura de todos los árboles

def leer_arboles(nombre_archivo):
    '''Apartir de los datos de un archivo devuelve una lista de diccionarios.'''
    lista_diccionarios = []
    
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            lista_diccionarios.append(registro)
                
    return lista_diccionarios

#%%

# Ejercicio 4.16: Lista de altos de Jacarandá

archivo_arboles = '../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(archivo_arboles)
H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#%%

# Ejercicio 4.17: Listas de altos y diámetros de Jacarandá

archivo_arboles = '../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(archivo_arboles)
altura_diametro = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

#%%

# Ejercico 4.18: Diccionario con medidas

archivo_arboles = '../Data/arbolado-en-espacios-verdes.csv'
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dicc_especies = { especie: [ (arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == especie ] for especie in especies}

