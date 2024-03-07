#Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.

lista = []

for i in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)
    
mayor = 0
for i in range(0,10):
    if lista[i] % 2 == 0:
        if lista[i] > mayor:
            mayor = lista[i]
            z = i
print("el numero mayor par es",mayor,"y esta en al posicion",z)
    