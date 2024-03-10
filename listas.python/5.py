#Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números tienen, de los
#almacenados allí, tienen menos de 3 dígitos.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)
    
cont = 0    
for x in range(0,10):
    if lista[x] < 100:
        cont = cont + 1
        
print("hay",cont,"numeros que tienen menos de tres digitos")