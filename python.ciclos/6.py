#Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos
#entre 1 y cada uno de los dígitos.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    for x in range(1,dig1+1):
        print(x)
    print("----")
    for x in range(1,dig2+1):
        print(x)   
    print("----")
    for x in range(1,dig3+1):
        print(x)      
else:
    print("no tiene tres digitos")