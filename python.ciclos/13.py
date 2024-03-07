#Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.

num = int(input("digite un numero"))

for x in range(1,num+1):
    if x % 5 == 0:
        print(x)