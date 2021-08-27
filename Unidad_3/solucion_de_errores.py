#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:05:23 2021

@author: bloisejuli
"""

# solucion_de_errores.py
# Ejercicios de errores en el código
#%%
# Ejercicio 3.1. Función tiene_a()
# Comentario: Los errores eran que no tenia en cuenta a la 'A' y que si la primer letra de la expresión no era una 
#             'a', la función devolvia False sin verificar el resto de las letras.
#    
#    El tema de la 'A' lo corregí agregando una condición más al if, y el tema de que no recorria toda la expresion
#    lo corregí quitando la condición else y cambiando que solo devuelva false cuando sale del while porque ya 
#    termino de recorrer la palabra.
 
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    
    while i<n :
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        
        i += 1
        
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
# Ejercicio 3.2. Función tiene_a(), nuevamente
# Comentario: Los errores eran que no tenia en cuenta a la 'A' y que no hace una comparación en la condición del
#             if sino que realiza una asignaión, además le faltan los ':' al finalizar la firma de la función, la 
#             condición del while y la condición del if, y, además esta mal escrito el ultimo return, que dice 
#             'Falso', en lugar de 'False'.

#    El tema de la 'A' lo corregí agregando una condición más al if, y para que funcione correctamente cambie
#    la asignacion "expresion[i] = 'a'" por una comparación "expresion[i] == 'a'"
 
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3. Función tiene_uno()
# Comentario: El error era que no podia trabajar con una expresión pura de números ya que lo interpretaba como
#             un entero entonces, no podia usarse la función len().

#    Lo corregí creando una variable que guarde a la expresión leída como un string y así poder mantener el mismo
#    código.

#    A continuación va el código corregido    

def tiene_uno(expresion):
    frase = str(expresion)
    n = len(frase)
    i = 0
    tiene = False

    while (i < n and not tiene):
        if frase[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%% 
# Ejercicio 3.4: Funcion suma()

# Comentario: El error era que la función no devolvía nada, por eso se imprimia "none"

#    Lo corregí agregando un return, para que devuelva el valor de c, que es la variable asignada para la suma.

#    A continuación va el código corregido 

def suma(a,b):
    c = a + b
    return c
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.5: Funcion leer_camion()

# Comentario: El error era que el registro estaba definido afuera del for, entonces siempre se "appendeaba" el
#             mismo objeto de memoria, el que se encontraba al final del archivo

#    Lo corregí definiendo el registro adentro del for, entonces se agrega a la lista camion un nuevo registro
#    en cada iteración.

#    A continuación va el código corregido 

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)









