#Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus dígitos.

num = int(input("digite un numero"))

if num > 999 and num < 10000:
    print("tiene tres digitos")
    dig4 = num % 10
    num = num // 10
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10  
    suma = dig1 + dig2 + dig3 + dig4
    print("la suma es",suma)
else:
    print("no tiene tres digitos")