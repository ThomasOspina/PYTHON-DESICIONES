#Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el promedio
#entero de los datos del vector.

lista = []

for x in range(0,10):
    n = int(input("digite un numero"))
    lista.append(n)
    
suma = 0    
for x in lista:
    suma = suma + x
        
promedio = suma // 10
print("el promedio de los numeros en la lista es",promedio)    