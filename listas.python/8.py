#Leer 10 números enteros, almacenarlos en un vector y determinar si existe al menos un número repetido.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)

if len(lista) == len(set(lista)):
    print("no hay numeros repetidos")
else:
    print("hay numeros repetidos")
