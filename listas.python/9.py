#Leer 10 números enteros, almacenarlos en un vector y mostrar en pantalla todos los enteros
#comprendidos entre 1 y cada uno de los números almacenados en el vector.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)

for x in lista:
    j = 1
    while j <= lista[x]:
        print(j)
        j = j + 1
    print("_____")       