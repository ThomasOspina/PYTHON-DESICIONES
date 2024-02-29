#Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.

num = int(input("digite un numero"))

if (num > 9) and (num < 99):
    dig1 = num // 10
    dig2 = num % 10
    if dig1 == dig2:
        print("los numeros son iguales")
    else:
        print("no son iguales")