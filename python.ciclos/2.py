#Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído

num = int(input("digite un numero"))

for x in range(1,num+1):
    if x % 2 == 0:
        print(x)
              