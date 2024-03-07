#Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.

num = int(input("digite un numero"))

suma = 0
x = 0
c = 0
while num > 0:
    x = num % 10
    c = c +1
    suma = suma + x
    num = num // 10

promedio = suma // c
print(promedio)
print("el promedio es",promedio)    