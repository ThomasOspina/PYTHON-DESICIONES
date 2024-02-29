#Leer tres números enteros y mostrarlos ascendentemente.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))
num3 = int(input("digite un numero"))

if num1 > num2 and num2 > num3:
    print(num3)
    print(num2)
    print(num1)

if num1 > num3 and num3 > num2:
    print(num2)
    print(num3)
    print(num1) 

if num2 > num1 and num1 > num3:
    print(num3)
    print(num1)
    print(num2)

if num2 > num3 and num3 > num1:
    print(num1)
    print(num3)
    print(num2)   

if num3 > num1 and num1 > num2:
    print(num2)
    print(num1)
    print(num3)

if num3 > num2 and num2 > num1:
    print(num1)
    print(num2)
    print(num3)                