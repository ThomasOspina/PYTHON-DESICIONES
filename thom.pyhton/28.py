#Leer un número entero menor que 50 y positivo y determinar si es un número primo.

num = int(input("digite un numero"))

if num > 0 and num < 50:
    print("es positivo y menor que 50")
    x = 1
    c = 0
    while x <= num:
        if num % x == 0:
            c = c + 1
        x = x + 1

    if c == 2:
        print(num,"es primo")
    else:
        print("no es primo")  
else:
    print("no es positivo o no es menor que 50")

  
