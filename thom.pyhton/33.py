#Leer un número entero y determinar si termina en 7.

num = int(input("digite un numero"))

dig = num % 10
if dig == 7:
    print("termina en 7")
else:
    print("no termina en 7")