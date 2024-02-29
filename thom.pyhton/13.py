#Leer dos números enteros de dos dígitos y determinar si la suma de los dos
#números origina un número par.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100):
    print("tienen dos digitos")
    suma = num1 + num2
    if suma % 2 == 0:
        print("la suma es par")
    else:
        print("la suma no es par")
else:
    print("no tienen dos digitos")