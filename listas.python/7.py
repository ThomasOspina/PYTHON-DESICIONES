#Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el menor número primo.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)
    
menor = 0    
z = 1
for x in range (0,10):
    c = 0
    y = 1
    while y <= lista[x]:
        if lista[x] % y == 0:
            c = c + 1
        y = y + 1
    if c == 2:
        if z == 1:
            menor = lista[x]
            i = x
            z = 0
        if lista[x] < menor:
            menor = lista[x]
            i = x
if z == 0:
    print("el menor primo es",menor,"se encuentra en la posicion",i+1)                        