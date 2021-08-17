# diccionario_geringoso.py

# Alumna: Julieta Bloise

# Ejercicio 2.14:
# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. Las claves del diccionario deben ser las palabras de la 
# lista y los valores deben ser sus traducciones al geringoso (como en el Ejercicio 1.18). Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 

def traducir_a_geringoso(cadena):
    '''Traduce una palabra cualquiera a geringoso.'''

    capadepenapa = ''

    for c in cadena:
        capadepenapa += c 
        if c in 'aeiouáéíóú':
            capadepenapa += 'p' + c
        elif c in 'AEIOUÁÉÍÓÚ':
            capadepenapa += 'P' + c

    return capadepenapa.lower()


def lista_geringosa(lista):
    '''A partir de una lista crea una otra lista con palabras traducidas a geringoso.'''

    palabra_traducidas = []

    for palabra in lista:
        palabra_traducidas.append (traducir_a_geringoso(palabra)) 

    return palabra_traducidas



def diccionario_geringoso (lista):
    '''Crea un diccionario a partir de una lista.'''

    diccionario = {}
    palabras_traducidas = lista_geringosa(lista)
    
    for i in range(len(lista)):
        diccionario[lista[i]] = palabras_traducidas[i]

    return diccionario


lista_frutas = ['banana', 'manzana', 'mandarina']
diccionario = diccionario_geringoso (lista_frutas)
print (diccionario)

