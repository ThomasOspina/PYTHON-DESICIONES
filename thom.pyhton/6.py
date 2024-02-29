#Leer un número entero de dos dígitos menor que 20 y determinar si es primo.

num = int(input("digite numero"))

x = 1
c = 0
if (num > 9) and (num < 20):
    while x <= num:
        if num % x == 0:
            c = c + 1
        x = x + 1
else:
    print("no tiene dos digitos o es mayor a 20")
    
if c == 2:
    print("el numero es primo")