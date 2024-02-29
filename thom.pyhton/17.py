#Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    if dig1 == dig2 and dig1 == dig3 and dig2 == dig3:
        print("los numeros son iguales")
    else:
        if dig1 > dig2 and dig1 > dig3:
            print("el primer digito es el mayor")

        if dig2 > dig1 and dig2 > dig3:
            print("el segundo digito es el mayor") 

        if dig3 > dig1 and dig3 > dig2:
            print("el tercer digito es el mayor")       
else:
    print("no tiene tres digitos")