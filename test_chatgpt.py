
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

cont_espana = 0
cont_chile = 0
cont_argentina = 0
cont_colombia = 0
cont_peru = 0
cont_mexico = 0


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

print(paises)

for i in range(len(pais)):
    if pais[i] == 'Chile':
        cont_chile += 1

    if pais[i] == 'Argentina':
        cont_argentina += 1

    if pais[i] == 'España':
        cont_espana +=1

    if pais[i] == 'Colombia':
        cont_colombia +=1

    if pais[i] == 'México':
        cont_mexico += 1

    if pais[i] == 'Perú':
        cont_peru += 1
 
print(f'Chile tiene en esta lista {cont_chile} personas')
print(f'Argentina tiene en esta lista {cont_argentina} personas')
print(f'España tiene en esta lista {cont_espana} personas')
print(f'Colombia tiene en esta lista {cont_colombia} personas')
print(f'Mexico tiene en esta lista {cont_mexico} personas')
print(f'Peru tiene en esta lista {cont_peru} personas')
















































