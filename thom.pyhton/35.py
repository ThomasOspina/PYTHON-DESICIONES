#Leer un número entero de dos dígitos, guardar cada dígito en una variable
#diferente y luego mostrarlas en pantalla.

num = int(input("digite un numero"))

if num > 9 and num < 100:
    print("tiene dos digitos")
    dig1 = num // 10
    dig2 = num % 10
    print(dig1)
    print(dig2)
else:
    print("no tiene dos digitos")