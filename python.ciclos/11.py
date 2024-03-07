#Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros
#comprendidos entre un dígito y otro.

num = int(input("digite un numero"))

if num > 9 and num < 100:
    print("tiene dos digitos")
    dig2 = num % 10
    dig1 = num // 10
    for x in range(dig1,dig2+1):
        print(x)

    for x in range(dig2,dig1+1):
        print(x)    
else:
    print("no tiene dos digitos")