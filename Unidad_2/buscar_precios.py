#buscar_precios.py

#Alumna: Julieta Bloise

# Ejercicio 2.7:
# A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada 
# fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.


def buscar_precio (fruta):
    f = open('../Data/precios.csv', 'rt')

    for line in f:
        row = line.split(',')
        
        if (row[0] == fruta):
            print("El precio del cajón de", fruta, "es:", row[1])
    
    if (row[0] != fruta):
        print(fruta, "no figura en el listado de precios.")
        
    f.close()