#Leer dos números enteros y si la diferencia entre los dos números es par mostrar
#en pantalla la suma de los dígitos de los números, si dicha diferencia es un número
#primo menor que 10 entonces mostrar en pantalla el producto de los dos números
#y si la diferencia entre ellos terminar en 4 mostrar en pantalla todos los dígitos por separado.

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
suma1 = 0
suma2 = 0
#no pude              