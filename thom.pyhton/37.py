#Leer dos números enteros y determinar cuál es múltiplo de cuál.

num1 = int(input("digite un numero"))

num2 = int(input("digite un numero"))

if num1 % num2 == 0:
    print(num1,"es multiplo de",num2)
else:
    if num2 % num1 == 0:
        print(num2,"es multiplo de",num1)
    else:
        print("ninguno es multiplo")