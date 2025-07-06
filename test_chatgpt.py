'''Ejercicios ordenados de más fácil a más difícil

    Leer y mostrar datos
    Lee un archivo CSV y muestra todas las filas en pantalla, una a una, sin incluir la cabecera.

    Extraer una columna
    Crea una función que reciba la lista de filas y el nombre de una columna (por ejemplo, “pais”) y devuelva una lista con todos los valores de esa columna.

    Filtrar por género
    Devuelve todas las filas donde el género sea “Mujer” o “Hombre”.

    Añadir una fila nueva
    Simula añadir una nueva persona al listado (solo en memoria, no hace falta modificar el archivo).

    Contar personas por país
    Cuenta cuántas personas hay por cada país y muestra el resultado.

    Calcular media de edades
    Usando la función para extraer columnas, extrae la columna “edad” y calcula la media (sin usar librerías externas).'''

import io 

fichero = io.open("chatgpt.csv", "r", encoding = "utf-8")

lista = fichero.readlines()


#EJERCICIO 1
print(lista[1:])


#EJERCICIO 
#recorrer la lista con un bucle for para imprimir cada línea por separado (queda más limpio en la terminal).

for n_list in lista:
    print(n_list.strip())

























































