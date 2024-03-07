#Leer un número entero y determinar a cuánto es igual la suma de todos los enteros
#comprendidos entre 1 y el número leído.

num = int(input("digite un numero"))

suma = 0
for x in range(1,num+1):
    suma = suma + x

print(suma)    