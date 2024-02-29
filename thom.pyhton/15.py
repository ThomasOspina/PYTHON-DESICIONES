#Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    suma = dig1 + dig2 + dig3
    print("la suma es",suma)
else:
    print("no tiene tres digitos")