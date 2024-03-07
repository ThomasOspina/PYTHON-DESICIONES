#Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el número leído.

num = int(input("digite un numero"))

fact = 0
cont = 1
for x in range(1,num+1):
    fact = x * cont
    cont = fact
    print("el factorial de",x,"es",cont)