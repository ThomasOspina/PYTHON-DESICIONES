#Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    if dig1 % 2 == 0:
        print("el primer digito es par")

    if dig2 % 2 == 0:
        print("el segundo digito es par")

    if dig3 % 2 == 0:
        print("el tercer digito es par")
    else:
        print("no tiene pares")    
else:
    print("no tiene tres digitos")