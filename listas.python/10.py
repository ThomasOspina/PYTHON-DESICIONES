#Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números terminar en dígito primo.

lista = []
primos = [2,3,5,7]

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)

dig = 0
for x in range(0,10):
    dig = lista[x] % 10
    if dig in primos:
        print(lista[x],"termina en un digito primo")