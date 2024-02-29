#Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100):
    print("tienen dos digitos")
    num1dig1 = num1 // 10
    num1dig2 = num1 % 10
    num2dig1 = num2 // 10
    num2dig2 = num2 % 10
    suma = num1dig1 + num1dig2 + num2dig1 + num2dig2
    print(suma)
else:
    print("no tienen dos digitos")