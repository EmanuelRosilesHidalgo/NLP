# Datos para la tabla (ejemplo)
datos = [
    ("Dato1", "Dato2", "Dato3"),
    ("Manzana", "10", "$1.50"),
    ("Banana", "15", "$0.75"),
    ("Naranja", "12", "$2.00"),
]

# Encabezados de las columnas
encabezados = ("Columna 1", "Columna 2", "Columna 3")

# Longitud máxima de cada columna (para alinear)
longitud_columnas = [max(map(len, columna)) for columna in zip(encabezados, *datos)]

# Imprimir encabezados
for i, encabezado in enumerate(encabezados):
    print(encabezado.ljust(longitud_columnas[i]), end='  ')
print()

# Imprimir separador horizontal
for longitud in longitud_columnas:
    print('-' * longitud, end='  ')
print()

# Imprimir datos
for fila in datos:
    for i, dato in enumerate(fila):
        print(dato.ljust(longitud_columnas[i]), end='  ')
    print()