#Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

for x in range(num1,num2+1):
    if x % 10 == 4:
        print(x)