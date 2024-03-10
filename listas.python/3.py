#Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran
#los números terminados en 4.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)
    
    
for x in range(0,10):
    if lista[x] % 10 == 4:
        c = x
        print(lista[x],"termina en 4 y esta en la posicion",c)