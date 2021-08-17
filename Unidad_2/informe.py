# informe.py

# Alumna: Julieta Bloise

# Ejercicio 2.18:
# Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py (usando las funciones leer_camion() y 
# leer_precios()) y completá el programa para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó 
# el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

import csv

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
    

def calcular_costo(precios_camion):
    '''Apartir de una lista de diccionarios calcula el costo del camion.'''
    costo_camion = 0
    for i in range(len(precios_camion)):
        costo_camion += int(precios_camion[i]['cajones']) * float(precios_camion[i]['precio'])
    
    return costo_camion


def calcular_recaudacion(precios_camion, precios_venta):
    '''Apartir de una lista de diccionarios con los precios del camion y un diccionario con los precios de la venta calcula la recaudacion.'''
    recaudacion = 0
    
    for i in range(len(precios_camion)):
        for j in precios_venta:
            if (precios_camion[i]['nombre'] == j):
                recaudacion += int(precios_camion[i]['cajones']) * float(precios_venta[j])
    
    return recaudacion



precios_camion = leer_camion('../Data/camion.csv')
precios_venta = leer_precios('../Data/precios.csv')


costo_camion = calcular_costo(precios_camion)
recaudacion = calcular_recaudacion(precios_camion, precios_venta)

diferencia = recaudacion - costo_camion

print('Costo del camion:', costo_camion)
print('Se recaudo con la venta', recaudacion)

if (diferencia > 0):
    print('Hubo una ganancia de:', round(diferencia, 2))
else:
    print('Hubo una perdidad de:', round(diferencia, 2))