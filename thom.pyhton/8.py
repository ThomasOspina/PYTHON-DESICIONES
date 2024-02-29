#Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.

num = int(input("digite un numero"))

x = 1 
y = 1
c1 = 0
c2 = 0
if (num > 9) and (num < 99):
    dig1 = num // 10
    dig2 = num % 10
    while x <= dig1:
        if dig1 % x == 0:
            c1 = c1 + 1
        x = x + 1

    while y <= dig2:
        if dig2 % y == 0:
            c2 = c2 + 1
        y = y + 1
else:
    print("no tiene dos digitos")        

if c1 == 2:
    print("el primer digito es primo")
else:
    print("el primer digito no es primo")

if c2 == 2:
    print("el segundo digito es primo")
else:
    print("el segundo digito no es primo")
