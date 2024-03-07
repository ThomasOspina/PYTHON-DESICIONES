#Leer un número entero y determinar cuántas veces tiene el dígito 1.

num = int(input("digite un numero"))

c = 0
x = 0
while num > 0:
    x = num % 10
    if x == 1:
        c = c +1
    num = num // 10

print("el numero tiene",c,"digitos iguales a 1")    