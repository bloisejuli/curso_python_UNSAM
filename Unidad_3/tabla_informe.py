#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:28:32 2021

@author: bloisejuli
"""
# tabla_informe.py

# Ejercicio 3.16:
# Realizar un programa que dado un archivo imprima un tabla con formato


import csv

def hacer_informe(precios_camion, precios_venta):
    lista_frutas = []
    for fruta in precios_camion:
        if fruta['nombre'] in precios_venta:
            cambio = float(precios_venta[fruta['nombre']]) - float(fruta['precio'])
            fruta['cambio'] = cambio
            tupla_frutas = tuple(fruta.values())
            lista_frutas.append(tupla_frutas)
    
    return(lista_frutas)

        

def crear_lista(nombre_archivo):
    '''Apartir de los datos de un archivo crea una lista.'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        
    return camion
    

def leer_camion(nombre_archivo):
    '''Apartir de los datos de un archivo devuelve una lista de diccionarios.'''
    camion_lista = crear_lista(nombre_archivo)
    lista_diccionarios = []

    for i in range(len(camion_lista)):
        camion_diccionario = {'nombre': camion_lista[i][0], 'cajones' : camion_lista[i][1], 'precio' : camion_lista[i][2]}
        lista_diccionarios.append(camion_diccionario)

    return lista_diccionarios


def leer_precios (nombre_archivo):
    '''Apartir de los datosde un archivo arma un diccionario'''
    nombres_lista = []
    precios_lista = []
    diccionario = {}
    
    with open(nombre_archivo, 'r') as file:
        rows = csv.reader(file)
        
        for row in rows:
            try:
                nombre = row[0]
                precio = row[1]
                nombres_lista.append(nombre)
                precios_lista.append(precio)

            except IndexError:
                print("Una linea del archivo", nombre_archivo, "se encontraba en blanco." )

            for i in range(len(nombres_lista)):
                diccionario[nombres_lista[i]] = precios_lista[i]

    return diccionario
    


archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'

precios_camion = leer_camion(archivo_camion)
precios_venta = leer_precios(archivo_precios)
informe = hacer_informe(precios_camion, precios_venta)

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
    
    
#Output:
    
#    Nombre    Cajones     Precio     Cambio 
#---------- ---------- ---------- ----------
#      Lima        100     $32.20       8.02
#   Naranja         50     $91.10      15.18
#     Caqui        150    $103.44       2.02
# Mandarina        200     $51.23      29.66
#   Durazno         95     $40.37      33.11
# Mandarina         50     $65.10      15.79
#   Naranja        100     $70.44      35.84