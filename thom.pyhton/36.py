#Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.

num = int(input("digite un numero"))

if num > 999 and num < 10000:
    print("tiene cuatro digitos")
    dig4 = num % 10
    num = num // 10
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10 
    x = 0
    y = 0
    if dig1 % 2 == 0:
        x = x + 1
    else:
        y = y + 1

    if dig2 % 2 == 0:
        x = x + 1
    else:
        y = y + 1 

    if dig3 % 2 == 0:
        x = x + 1
    else:
        y = y + 1

    if dig4 % 2 == 0:
        x = x + 1
    else:
        y = y + 1    

    print("tiene",x,"pares, y",y,"impares")             
else:
    print("no tiene cuatro digitos")