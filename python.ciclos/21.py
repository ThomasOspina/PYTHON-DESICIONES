#Leer un número entero y determinar a cuánto es igual al suma de sus dígitos.

num = int(input("digite un numero"))

suma = 0
x = 0
while num > 0:
    x = num % 10
    suma = suma + x
    num = num // 10

print(suma)    