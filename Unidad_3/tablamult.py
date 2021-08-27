#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 17:45:31 2021

@author: bloisejuli
"""
# tablamult.py

# Ejercicio 3.17:
# Escribí un programa que imprima de forma prolija las tablas de multiplicar del 1 al 9 usando f-strings. 
# Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

print('  ', end=' ')

for i in range(10):
    print(f'{i:>4d}', end=' ')
    
print('')
print('-'*53)


for i in range(10):
    print(i, end=': ')   
    s = 0
    for j in range(10):
        print(f'{s:>4d}', end=' ')
        s +=i
        
    print('')