#Leer dos números enteros y determinar si la diferencia entre los dos es un número par.

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
    if dif % 2 == 0:
        print(dif,"la diferencia en un numero par")
    else:
        print("la diferencia no es un numero par")