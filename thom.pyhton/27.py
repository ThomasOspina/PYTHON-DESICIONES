#Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene.

num = int(input("digite un numero"))

if num > 999 and num < 10000:
    print("tiene cuatro digitos")
    dig4 = num % 10
    num = num // 10
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10  
    if dig1 % 2 == 0:
        print(dig1,"es par")

    if dig2 % 2 == 0:
        print(dig2,"es par")    

    if dig3 % 2 == 0:
        print(dig3,"es par")

    if dig4 % 2 == 0:
        print(dig4,"es par")    
    else:
        print("no tiene pares")    
else:
    print("no tiene cuatro digitos")