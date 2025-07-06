
import io 

fichero = io.open("chatgpt.csv", "r", encoding = "utf-8")

lista = fichero.readlines()


#EJERCICIO 1
'''print(lista[1:])'''


#EJERCICIO 
#recorrer la lista con un bucle for para imprimir cada línea por separado (queda más limpio en la terminal).

nueva_lista = []
edades = []
paises = []
ciudad = []
genero = []




for n_list in lista:
    nueva_lista.append(n_list.strip().split(','))

for campos  in nueva_lista:
    edades.append(campos[0])

edades = edades [1:]

print(edades)


#Imprimir solo la primera columna (edad) de cada fila (sin la cabecera).
























































