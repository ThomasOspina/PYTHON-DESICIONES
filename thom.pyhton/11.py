#Leer dos números enteros y determinar cuál es el mayor.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

if num1 > num2:
    print(num1,"es el mayor")
else:
    if num2 > num1:
        print(num2,"es el mayor")
    else:
        print("los numeros son iguales")