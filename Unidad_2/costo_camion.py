# costo_camion.py

# Alumna: Julieta Bloise

# Ejercicio 2.9:
# Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. 
# Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
# Modificá tu programa costo_camion.py para que use el módulo csv para leer los archivos CSV y probalo en un par de los ejemplos anteriores.

import csv

def costo_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    file = open(nombre_archivo)
    rows = csv.reader(file)
    headers = next(rows)
    
    costo = 0

    for row in rows:
        try:
            cantidad = int(row[1])
            precio = float(row[2])
            costo = costo + cantidad*precio
        except ValueError:
            print("Faltan datos para", row[0], "verificar el archivo." )
    
    file.close()
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
