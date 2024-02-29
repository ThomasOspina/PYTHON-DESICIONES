#Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10
#entonces mostrar en pantalla todos los enteros comprendidos entre el menor y el
#mayor de los números leídos.

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
    if dif <= 10:
        while mayor >= menor:
            print(mayor)
            mayor = mayor - 1
    else:
        print("la diferencia es mayor a 10")        

