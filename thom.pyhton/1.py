#Leer un número entero y determinar si es un número terminado en 4.

num = int(input("digite un nuemro"))

if (num % 10 == 4):
    print(num,"termina en 4")
else:
    print("no termina en 4")
    