#Leer un número entero y determinar si tiene 3 dígitos.

num = int(input("digite un nuemro"))

if (num > 99) and (num < 999):
    print("el numero tiene tres digitos")
else:
    print("no tiene tres digitos")