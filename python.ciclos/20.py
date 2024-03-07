#Leer un número entero y determinar cuántos dígitos tiene.

num = int(input("digite un numero"))

c = 0
while num > 0:
    num = num // 10
    c = c + 1

print("el numero tiene",c,"digitos")

