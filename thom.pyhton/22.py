#Leer un número entero de tres dígitos y determinar si el primer dígito es igual al  último.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    if dig1 == dig3:
        print(dig1,"es igual a",dig3)
    else:
        print("no son iguales")
else:
    print("no tiene tres digitos")