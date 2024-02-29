#Leer dos números enteros y determinar si la diferencia entre los dos es un número primo.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

if num1 == num2:
    print("los numero son iguales")
else:
    if num1 > num2:
        mayor = num1
        menor = num2

    if num2 > num1:
        mayor = num2
        menor = num1

    dif = mayor - menor
    print(dif)
    x = 1
    c = 0
    while x <= dif:
        if dif % x == 0:
            c = c + 1
        x = x + 1

    if c == 2:
        print("la diferencia es un numero primo")
    else:
        print("la diferencia no es un numero primo")    
    
