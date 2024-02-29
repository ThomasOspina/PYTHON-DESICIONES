#Leer un número entero de 2 dígitos y si es par mostrar en pantalla la suma de sus
#dígitos, si es primo y menor que 10 mostrar en pantalla su último dígito y si es
#múltiplo de 5 y menor que 30 mostrar en pantalla el primer dígito.

num = int(input("digite un numero"))

if num > 9 and num < 100:
    print("tiene dos digitos")
    dig1 = num // 10
    dig2 = num % 10
    suma = dig1 + dig2
    if num % 2 == 0:
        print("el numero es par y la suma de los digitos es",suma)
    
    x = 1
    c = 0
    while x <= num:
        if num % x == 0:
            c = c + 1
        x = x + 1

    if c == 2 and num < 10:
        print(num,"es primo y menor a 10")
        print(dig1)

    if num % 5 == 0 and num < 30:
        print(num,"es multiplo de 5 y menor a 30")
        print(dig2)        
else:
    print("no tiene dos digitos")

    