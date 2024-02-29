#Leer un número entero y si es múltiplo de 4 mostrar en pantalla su mitad, si es
#múltiplo de 5 mostrar en pantalla su cuadrado y si es múltiplo e 6 mostrar en
#pantalla su primer dígito. Asumir que el número no es mayor que 100.

num = int(input("digite un numero"))
if num < 100:
    if num % 4 == 0:
        mitad = num // 2
        print(mitad)
    else:
        print("no es multiplo de 4")    

    if num % 5 == 0:
        cuadrado = num ** num
        print(cuadrado)
    else:
        print("no es multiplo de 5")

    if num % 6 == 0:
        dig = num % 10
        print(dig)
    else:
        print("no es multiplo de 6")
else:
    print("no es menor a 100")        

