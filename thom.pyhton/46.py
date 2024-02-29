#Leer un número entero de 2 dígitos y si terminar en 1 mostrar en pantalla su primer
#dígito, si termina en 2 mostrar en pantalla la suma de sus dígitos y si termina en 3
#mostrar en pantalla el producto de sus dos dígitos.

num = int(input("digite un numero"))

if num > 9 and num < 100:
    print("tiene dos digitos")
    dig1 = num // 10
    dig2 = num % 10
    suma = dig1 + dig2
    producto = dig1 * dig2
    if dig2 == 1:
        print(dig1)

    if dig2 == 2:
        print(suma)   

    if dig2 == 3:
        print(producto)     