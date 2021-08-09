# geringoso.py

# Alumna: Julieta Bloise

# Ejercicio 1.18:
# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

cadena = input("Escribí la palabra que quieras traducir a geringoso: ")
capadepenapa = ''

for c in cadena:
    if c == "a" or c == "A":
        capadepenapa = capadepenapa + "apa"

    elif c == "e" or c == "E":
        capadepenapa = capadepenapa + "epe"

    elif c == "i" or c == "I":
        capadepenapa = capadepenapa + "ipi"

    elif c == "o" or c == "O":
        capadepenapa = capadepenapa + "opo"

    elif c == "u" or c == "U":
        capadepenapa = capadepenapa + "upu"

    else:
        capadepenapa = capadepenapa + c

print("Palabra en geringoso:", capadepenapa)
