#Leer un número entero y mostrar todos los divisores exactos del número
#comprendidos entre 1 y el número leído.

num = int(input("digite un numero"))

for x in range(1,num+1):
    if num % x == 0:
        print(x)