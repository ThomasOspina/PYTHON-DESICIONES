#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

num = int(input("digite un numero"))

if (num > 9) and (num < 99):
    dig1 = num // 10
    dig2 = num % 10
    if (dig1 % 2 == 0) and (dig2 % 2 == 0):
        print("los dos digitos son pares")
    else:
        if (dig1 % 2 == 0):
            print("el primer digito es par")
        else:
            if (dig2 % 2 == 0):
                print("el segundo digito es par")
            else:
                print("ninguno es par")
else:
    print("no tiene dos digitos")
