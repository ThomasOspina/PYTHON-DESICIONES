#Leer un número de dos dígitos y determinar si pertenece a la serie de Fibonacci.

num = int(input("digite un numero"))

if num > 9 and num < 100:
    print("tiene dos digitos")
    a = 0
    b = 1
    for x in range(1,50):
        c = a + b
        a = b
        b = c
        if num == c:
            print(num,c)
            print("el numero pertenece a la serie fibonacci")