#Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.

num = int(input("digite un numero"))

if (num > 9) and (num < 99):
    dig1 = num // 10
    dig2 = num % 10
    suma = dig1 + dig2
    print("la suma es",suma)
else:
    print("no tiene dos digitos")