#Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.

num = int(input("digite un numero"))

x = 1
c = 0
if (num > 9) and (num < 99):
    while x <= num:
        if num % x == 0:
            c = c + 1
        x = x + 1
else:
    print("no tiene dos digitoso")

if c == 2:
    print("el numero es primo")
    if num < 0:
        print("es negativo")
    else:
        print("no es negativo")
    
    
