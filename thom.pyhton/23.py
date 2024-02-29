#Leer un número entero de tres dígitos y determinar cuántos dígitos primos tiene.

num = int(input("digite un numero"))

x = 1 
y = 1
z = 1
c1 = 0
c2 = 0
c3 = 0
if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    while x <= dig1:
        if num % x == 0:
            c1 = c1 + 1
        x = x + 1
    while y <= dig2:
        if num % y == 0:
            c2 = c2 + 1
        y = y + 1
    while z <= dig3:
        if num % z == 0:
            c3 = c3 + 1
        z = z + 1 

    if c1 == 2:
        print("el primer digito es primo")
    else:
        print("el primer digito no es primo")   

    if c2 == 2:
        print("el segundo digito es primo")
    else:
        print("el segundo digito no es primo") 

    if c3 == 2:
        print("el tercer digito es primo")
    else:
        print("el tercer digito no es primo")           
else:
    print("no tiene tres digitos")
