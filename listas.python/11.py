#“Cargar” dos vectores cada uno con 5 datos enteros y determinar si los datos almacenados en
#ambos vectores son exactamente los mismos tanto en contenido como en posición.

lista1 = []
lista2 = []

for x in range(0,5):
    n1 = int(input("digite un numero en la lista 1"))
    lista1.append(n1)

for z in range(0,5):
    n2 = int(input("digite un numero en la lista 2"))
    lista2.append(n2)    

for x in range(0,5):
    for z in range(0,5):
        if lista1[x] == lista2[z]:
            print(lista1[x],"es igual a",lista2[z],"y es estan en la misma posicion")
