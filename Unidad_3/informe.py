#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:00:35 2021

@author: bloisejuli
"""
# informe.py

# Ejercicio 3.9:
# Modificá el programa informe.py que escribiste antes (ver Ejercicio 2.18) para que use la función zip()

import csv   

def leer_camion(nombre_archivo):
    '''Apartir de los datos de un archivo devuelve una lista de diccionarios.'''
    lista_diccionarios = []
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)

    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            lista_diccionarios.append(record)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')

    f.close()
    return lista_diccionarios    

def leer_precios (nombre_archivo):
    '''Apartir de los datos de un archivo arma un diccionario'''
    nombres_lista = []
    precios_lista = []
    diccionario = {}
    
    with open(nombre_archivo, 'rt') as file:
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




def calcular_recaudacion(precios_camion, precios_venta):
    '''Apartir de una lista de diccionarios con los precios del camion y un diccionario con los precios de la venta calcula la recaudacion.'''
    recaudacion = 0
    
    for i in range(len(precios_camion)):
        for j in precios_venta:
            if (precios_camion[i]['nombre'] == j):
                recaudacion += int(precios_camion[i]['cajones']) * float(precios_venta[j])
    
    return recaudacion


archivo_camion = '../Data/fecha_camion.csv'
archivo_precios = '../Data/precios.csv'

precios_camion = leer_camion(archivo_camion)
precios_venta = leer_precios(archivo_precios)


camion = costo_camion(archivo_camion)
recaudacion = calcular_recaudacion(precios_camion, precios_venta)

diferencia = recaudacion - camion

print(" - BALANCE - ")
print('Costo del camion:', camion)
print('Se recaudo con la venta:', recaudacion)

if (diferencia > 0):
    print('Hubo una ganancia de:', round(diferencia, 2))
else:
    print('Hubo una perdidad de:', round(diferencia, 2))