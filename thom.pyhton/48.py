#Leer un número entero y si es menor que 100 determinar si es primo.

num = int(input("digite un numero"))

if num < 100:
    print("es menor a 100")
    x = 1
    c = 0
    while x <= num:
        if num % x == 0:
            c = c + 1
        x = x + 1

    if c == 2:
        print(num,"es primo")    
else:
    print("no es menor a 100")