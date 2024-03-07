#Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

c1 = 0
c2 = 0
dig1 = 0
dig2 = 0

while num1 > 0:
    dig1 = num1 % 10
    c1 = c1 + 1
    num1 = num1 // 10

while num2 > 0:
    dig2 = num1 % 10
    c2 = c2 + 1
    num2 = num2 // 10

if c1 == c2:
    print("tienen la misma cantidad de digitos")

if c1 > c2:
    print("el primer numero tiene mas digitos")

if c2 > c1:
    print("el segundo numero tiene mas digitos")            