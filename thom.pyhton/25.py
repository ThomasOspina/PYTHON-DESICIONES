#Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual
#a la suma de los otros dos.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    suma1 = dig1 + dig2
    suma2 = dig2 + dig3
    suma3 = dig3 + dig1
    if suma1 == dig3:
        print(suma1,"es igual a",dig3)

    if suma2 == dig1:
        print(suma2,"es igual a",dig1)   

    if suma3 == dig2:
        print(suma3,"es igual a",dig2)    
else:
    print("no tiene tres digitos")

