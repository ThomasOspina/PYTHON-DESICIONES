#Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.

num = int(input("ingrese un numero"))

if num > 999 and num < 10000:
    print("tiene cuatro digitos")
    dig4 = num % 10
    num = num // 10
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    if dig2 == dig3:
        print(dig2,"es igual a",dig3)
    else:
        print("no son iguales")
    