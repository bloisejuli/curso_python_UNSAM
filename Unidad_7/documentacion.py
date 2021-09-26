#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:04:43 2021

@author: bloisejuli
"""

# documentacion.py

# Ejercicio 7.10: Funciones y documentación
# Para cada una de las siguientes funciones:
#    Pensá cuál es el contrato de la función.
#    Agregale la documentación adecuada.
#    Comentá el código si te parece que aporta.
#    Detectá si hay invariantes de ciclo y comentalo al final de la función

#%%

def valor_absoluto(n):
    ''' 
    Pre: n debe ser un número flotante o entero.
    Post: Devuelve el valor absoluto de n '''
    if n >= 0:
        return n
    else:
        return -n
    
#%%

def suma_pares(lista):
    '''
    Pre: Lista debe ser una lista de numeros enteros.
    Post: Devuleve la suma de los numeros pares. '''
    resultado = 0
    for e in lista:
        if e % 2 ==0:
            resultado += e
        else:
            resultado += 0

    return resultado

# Invariantes de ciclo: resultado.

#%%

def veces(valor, cantidad):
    ''' Suma valor cantidad de veces.
    Pre: Cantidad debe ser un numero >= 0.
    Post: Devuelve la suma de valor''' 
    suma = 0
    nb = cantidad
    while nb != 0:
        #print(nb * a + res)
        suma += valor
        nb -= 1
    return suma

# Invariantes de ciclo: suma, nb. 

#%%

def collatz(n):
    """Cuenta las veces que se itera hasta llegar a 1.
    Pre: n debe ser un numero entero.
    Post: Devuelve un numero natural de las repeticiones.
    """
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

# invariantes de ciclo: n, res.