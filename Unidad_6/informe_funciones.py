#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:30:06 2021

@author: bloisejuli
"""

# informe_funciones

#%% 
# Ejercicio 6.11:
# Modificá este programa informe_funciones.py del Ejercicio 6.5 de modo que todo el procesamiento de archivos de entrada de datos se 
# haga usando funciones del módulo fileparse. Para lograr eso, importá fileparse como un módulo y cambiá las funciones leer_camion() 
# y leer_precios() para que usen la función parse_csv().

import fileparse

def hacer_informe(camion, precios):
    lista = []
    diccionario_precios = dict(precios)
    for lote in camion:
        precio_venta = diccionario_precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

def leer_camion(nombre_archivo):
    return fileparse.parse_csv(nombre_archivo, select=['nombre','cajones','precio'], types=[str,int,float])


def leer_precios (nombre_archivo):
    return fileparse.parse_csv(nombre_archivo, types=[str,float], has_headers=False)
    

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('')
    
    for titulo in headers:
        print(f'{titulo:>10s}', end= ' ')

    print('')
    linea = '-'*10
    print(f'{linea:>10s} {linea:>10s} {linea:>10s} {linea:>10s}', end='')
    print('')

    for nombre, cajones, precio, cambio in informe:
        s = f'${precio:>.2f}'
        print(f'{nombre:>10s} {cajones:>10d} {s:>10s} {cambio:>10.2f}')
        
        
#%%

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    precios_camion = leer_camion(nombre_archivo_camion)
    precios_venta = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(precios_camion, precios_venta)
    imprimir_informe(informe)
    
#%%

def main():
    nombre_archivo_camion = '../Data/camion.csv'
    nombre_archivo_precios = '../Data/precios.csv'
    informe_camion(nombre_archivo_camion, nombre_archivo_precios)
