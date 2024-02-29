#Leer dos números enteros y determinar si la diferencia entre los dos es un número
#divisor exacto de alguno de los dos números.

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
    if mayor % dif == 0:
        print(dif,"es divisor de",mayor)

    if menor % dif == 0:
        print(dif,"es divisor de",menor)    
    else:
        print(dif,"no es divisor")

