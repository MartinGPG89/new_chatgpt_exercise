
import io 

fichero = io.open("chatgpt.csv", "r", encoding = "utf-8")

lista = fichero.readlines()


#EJERCICIO 1
'''print(lista[1:])'''


#EJERCICIO 
#recorrer la lista con un bucle for para imprimir cada línea por separado (queda más limpio en la terminal).

nueva_lista = []
edades = []
pais = []
ciudad = []
genero = []




for n_list in lista:
    nueva_lista.append(n_list.strip().split(','))

for campos  in nueva_lista:
    edades.append(campos[0])
    pais.append(campos[1])
    ciudad.append(campos[2])
    genero.append(campos[3])

edades = edades [1:]
pais = pais[1:]
ciudad = ciudad[1:]
genero = genero[1:]




# Imprimir todos los países distintos


paises = set(pais)
ciudades = set(ciudad)
generos = set(genero)

print(generos, paises, ciudades)




















































