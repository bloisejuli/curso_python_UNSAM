# camion_commandline.py

# Alumna: Julieta Bloise

# Ejercicio 2.10:
# Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la lectura de parámetros por línea de comando según 
# la sugerencia

import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

