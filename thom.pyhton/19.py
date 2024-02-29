#Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

if num1 >  num2:
    num2 = int(input("digite un tercer numero"))
    if num1 > num2:
        print("el mayor es",num1)
    else:
        print("el mayor es",num2)
else:
    if num2 >  num1:
        num1 = int(input("digite un tercer numero"))
        if num2 > num1:
            print("el mayor es",num2)
        else:
            print("el mayor es",num1)

        