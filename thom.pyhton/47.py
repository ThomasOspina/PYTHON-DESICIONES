#Leer dos números enteros y si la diferencia entre los dos números es par mostrar
#en pantalla la suma de los dígitos de los números, si dicha diferencia es un número
#primo menor que 10 entonces mostrar en pantalla el producto de los dos números
#y si la diferencia entre ellos terminar en 4 mostrar en pantalla todos los dígitos por separado.

import math

def separar(z):
    while z > 0:
        print(z % 10)
        z = z // 10

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
    print("la diferencia es",dif)
    suma1 = 0
    suma2 = 0
    
    if dif % 2 == 0:
        print(dif,"es par")
        while mayor > 0:
            suma1 = suma1 + (mayor % 10)
            mayor = math.trunc(mayor // 10)

        while menor > 0:
            suma2 = suma2 + (menor % 10)
            menor = math.trunc(menor // 10)

        suma = suma1 + suma2
        print("la suma de los digitos es",suma)
    else:
        print(dif,"no es par")

    x = 1
    c = 0
    while x <= dif:
        if dif % x == 0:
            c = c + 1
        x = x + 1
    
    if c == 2 and dif < 10:
        print(dif,"es primo y menor a 10")
        producto = mayor * menor
        print("el producto de los numeros es",producto)
    else:
        print("no es primo o no es menor a 10") 
   
    dig = dif % 10
    if dig == 4:
        print("la diferencia termina en 4")
        print("numeros separados",num1,num2)
        separar(num1)
        separar(num2)
    else:
        print("la diferencia no termina en 4")
