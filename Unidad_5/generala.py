#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:06:14 2021

@author: bloisejuli
"""

# generala.py

#%%

# Ejercicio 5.1: Generala servida
import random

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return (tirada)

def es_generala(tirada):
    return max(tirada) == min(tirada) #comprueba que todos los numeros son iguales

#%%

# Ejercicio 5.2: Generala no necesariamente sevida
# Escribí una función llamada prob_generala(N) que, a partir de un parámetro N y usando las funciones del 
# Ejercicio 5.1 realice una simulación con N repeticiones, para estimar la probabilidad de obtener una generala 
# al finalizar una mano de tres tiradas. La función debe devolver un número entre 0 y 1. Guardala en un archivo 
# generala.py para el cierre de la clase.

# Quedandome con un dado
from collections import Counter

def nueva_tirada(lista):
     ''' Recibe una lista de dados y se fija cuantos dados necesita para completar los 5 dados para la generala'''
    juego_nuevo = tirar()
    cantidad_a_tirar = 5 - len(lista)
    dados_validos = juego_nuevo[0:cantidad_a_tirar]         
    return dados_validos


def ver_repetidos(tiro, lista):
    ''' Recorre los dados del tiro realizado y los compara con la lista de dados que quiere guardar, si encuentra algún dado igual modifica
        la lista, sino no hace nada'''
    for dado in tiro:
            if dado == lista[0]:
                lista.append(dado)


def generala_no_servida():
    ''' Realiza 3 tiradas en busca de una generala'''
    #PRIMER TIRO
    primer_tiro = tirar()
    
    if es_generala(primer_tiro):
        return True
    
    else:
        numero, cantidad = Counter(primer_tiro).most_common()[0] 
        lista_repetidos=[numero for i in range(cantidad)] 
        
        #SEGUNDO TIRO
        segundo_tiro = nueva_tirada(lista_repetidos)
        ver_repetidos(segundo_tiro, lista_repetidos)
        
        if len(lista_repetidos) == 5:
            return True
        else:
            #TERCER TIRO
            tercer_tiro = nueva_tirada(lista_repetidos)
            ver_repetidos(tercer_tiro, lista_repetidos)
            
            if len(lista_repetidos) == 5:
                return True
        
        return False


def prob_generala(N):    
    ''' Calcula la probabilidad de encontrar una generala en N manos'''
    G = sum([generala_no_servida() for i in range(N)])
    prob = G/N

    print(f'Tiré {N} veces, de las cuáles {G} saqué generala no necesariamente serivda.')
    print(f'Podemos estimar la probabilidad de sacar generala en 3 tiros mediante {prob:.6f}.')   
        
#----------------------------------------------------------------------------------------
# input: prob_generala(100000)
# output: Tiré 100000 veces, de las cuáles 4494 saqué generala no necesariamente serivda.
#         Podemos estimar la probabilidad de sacar generala en 3 tiros mediante 0.044940.

# input: prob_generala(1000000)
# output: Tiré 1000000 veces, de las cuáles 45025 saqué generala no necesariamente serivda.
#         Podemos estimar la probabilidad de sacar generala en 3 tiros mediante 0.045025.

#%%

# Ejercicio 5.2:
# Tirando todos los dados de nuevo si no hubo repetidos en el primer tiro

def generala_no_servida2():
    #PRIMER TIRO
    primer_tiro = tirar()
    
    if es_generala(primer_tiro):
        return True
    
    else:
        numero, cantidad = Counter(primer_tiro).most_common()[0] 
        lista_repetidos=[numero for i in range(cantidad)] 
        
        if len(lista_repetidos) == 1:
            #SEGUNDO TIRO
            lista_repetidos = []
            segundo_tiro = tirar()
            numero, cantidad = Counter(segundo_tiro).most_common()[0] 
            lista_repetidos=[numero for i in range(cantidad)]
            
            if es_generala(segundo_tiro):
                return True
            
        elif len(lista_repetidos) > 1:                             
            #SEGUNDO TIRO
            segundo_tiro = nueva_tirada(lista_repetidos)
            ver_repetidos(segundo_tiro, lista_repetidos)
            
            if len(lista_repetidos) == 5:
                return True

        #TERCER TIRO
        tercer_tiro = nueva_tirada(lista_repetidos)
        ver_repetidos(tercer_tiro, lista_repetidos)
        if len(lista_repetidos) == 5:
            return True
        
        return False


def prob_generala2(N):    
    G = sum([generala_no_servida2() for i in range(N)])
    prob = G/N

    print(f'Tiré {N} veces, de las cuáles {G} saqué generala no necesariamente serivda.')
    print(f'Podemos estimar la probabilidad de sacar generala en 3 tiros mediante {prob:.6f}.')
 
#----------------------------------------------------------------------------------------
# input: prob_generala(100000)
# output: Tiré 100000 veces, de las cuáles 4576 saqué generala no necesariamente serivda.
#         Podemos estimar la probabilidad de sacar generala en 3 tiros mediante 0.045760.

# input: prob_generala(1000000)
# output: Tiré 1000000 veces, de las cuáles 45660 saqué generala no necesariamente serivida.
#         Podemos estimar la probabilidad de sacar generala en 3 tiros mediante 0.045660.