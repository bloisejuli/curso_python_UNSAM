#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:17:32 2021

@author: bloisejuli
"""

#arboles.py

#%%

# Ejercicio 5.26:
# En este caso vamos a graficar un punto en el plano (x,y) por cada árbol en el dataset (o para cada árbol de cierta especie). El 
# punto correspondiente a un árbol con diámetro d y altura h será ubicado en la posición x=d e y=h. Este tipo  de gráfico permite 
# visualizar relaciones o tendencias entre las variables y es muy útil en el análisis exploratorio de datos.
# Escribí una función scatter_hd(lista_de_pares) que a partir de una lista de pares como la que generaste en el Ejercicio 4.17 
# genere un scatterplot para visualizar la relación entre altura y diámetro de los Jacarandás del dataset.

import matplotlib.pyplot as plt
import numpy as np
import csv

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


def altura_y_diametro (nombre_archivo):
    '''Apartir de los datos de un archivo devuelve una lista de tuplas con la altura y diametros de Jacarandas.'''
    arboleda = leer_arboles(nombre_archivo)
    altura_diametro = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    return altura_diametro


def divide_altura_diametro(lista_tupla):
    '''Divide los datos de una tupla en diametros y alturas.'''
    h_y_d =  np.array(lista_tupla)
    altura, diametro = np.split(h_y_d,2, axis=1)
    return altura, diametro


def plotea_diametro_vs_alto(alto, diametro, especie):
    '''Grafica la relacion diametro - altura'''
    plt.xlabel("Diametro (cm)")
    plt.ylabel("Alto (m)")
    plt.title("Relación diámetro-alto " + (f"para {especie}s"))
    plt.scatter(diametro,alto, alpha=0.3, s=90, label=especie)
    plt.legend()
    plt.show()    


def scatter_hd(arboleda):
    '''Apartir de una lista de pares de altura y diametro genera un scatterplot'''
    alto, diametro = divide_altura_diametro(altura_y_diametro(arboleda))
    plotea_diametro_vs_alto(alto, diametro, 'Jacarandá')
    plt.figure()
    
#%%
def main():
    archivo_arboles = '../Data/arbolado-en-espacios-verdes.csv'
    scatter_hd(archivo_arboles)
    
if __name__ == "__main__":
    main()