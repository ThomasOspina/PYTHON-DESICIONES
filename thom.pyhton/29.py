#Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej.
#15651, 59895.

num = int(input("ingrese un numero"))

if num > 9999 and num < 100000:
    print("tiene cuatro digitos")
    dig5 = num % 10
    num = num // 10
    dig4 = num % 10
    num = num // 10
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    if dig1 == dig5 and dig2 == dig4:
        print("el numero es capicuo")
    else:
        print("no es capicuo")  