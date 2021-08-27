#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:00:35 2021

@author: bloisejuli
"""
# arboles.py

import csv
from collections import Counter

#%%

# Ejercicio 3.18: Lectura de los árboles de un parque
# Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de 
# diccionarios con la información del parque especificado. La función debe devolver, en una lista un diccionario 
# con todos los datos por cada árbol del parque elegido.
# Observación: La columna que indica el nombre del parque en el que se encuentra el árbol se llama 'espacio_ve' en el archivo CSV.    

def leer_parque(nombre_archivo, parque):
    '''Apartir de los datos de un archivo devuelve una lista de diccionarios.'''
    lista_diccionarios = []
    
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            if registro['espacio_ve'] == parque:
                lista_diccionarios.append(registro)
                
    return lista_diccionarios

#%%

# Ejercicio 3.19: Determinar las especies en un parque
# Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio 
# anterior y devuelva el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista. 

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        tipo = arbol['nombre_com']
        especies.append(tipo)

    lista_especies = set(especies)
    return lista_especies


#%%

# Ejercicio 3.20: Contar ejemplares por especie

def contar_ejemplares(lista_arboles):
    cantidad_arboles = Counter()
    for arbol in lista_arboles:
        cantidad_arboles[arbol['nombre_com']] += 1
        
    return cantidad_arboles


#%% 

# Ejercicio 3.21: Alturas de una especie en una lista

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alto = float(arbol['altura_tot'])
            alturas.append(alto)
    return alturas        


#%%    

# Ejercicio 3.22: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion = int(arbol['inclinacio'])
            inclinaciones.append(inclinacion)
    return inclinaciones
            

#%%

def main():
    #pruebas 3.18
    archivo_arboles = '../Data/arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    arboles = leer_parque(archivo_arboles, parque)
    print(len(arboles))

    #pruebas 3.19
    especies_parque = especies(arboles)
    print(especies_parque)
    
    #pruebas 3.20
    cantidad_arboles = contar_ejemplares(arboles)
    print(cantidad_arboles)
    cantidad_arboles.most_common(5)
    
    #pruebas 3.21
    especie = 'Jacarandá'
    alturas = obtener_alturas(arboles, especie)
    print(alturas)
    altura_maxima = max(alturas)
    print(altura_maxima)
    promedio = sum(alturas)/len(alturas)
    print(promedio)

    #pruebas 3.22
    inclinaciones = obtener_inclinaciones(arboles, especie)
    print(inclinaciones)    

