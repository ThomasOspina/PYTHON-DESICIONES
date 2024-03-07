#Leer dos números y mostrar todos los enteros comprendidos entre ellos.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))


for x in range(num1,num2+1):
    print(x)

for x in range(num2,num1+1):
    print(x)    