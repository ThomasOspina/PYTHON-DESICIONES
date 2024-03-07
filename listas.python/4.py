#Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)
    
cont = 0    
mayor = max(lista)

for x in range(0,10):        
    if mayor == lista[x]:
        cont = cont + 1
        
print("el mayor es",mayor,"y esta repetido",cont,"veces")    