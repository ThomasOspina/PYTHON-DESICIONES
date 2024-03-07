#Leer un número entero y determinar a cuánto es igual el primero de sus dígitos.

num = int(input("digite un numero"))

dig = 0
x = 0
while num > 0:
    dig = num % 10
    x = dig
    num = num // 10

print("su primer digito es",x)    