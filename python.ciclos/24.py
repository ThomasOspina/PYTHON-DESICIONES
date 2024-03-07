#Leer un número entero y determinar a cuánto es igual al suma de sus dígitos pares.

num = int(input("digite un numero"))

suma = 0
x = 0
while num > 0:
    x = num % 10
    if x % 2 == 0:
        suma = suma + x
    num = num // 10

print("la suma de sus digitos pares es",suma)