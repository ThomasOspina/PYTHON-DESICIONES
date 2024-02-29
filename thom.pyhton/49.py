#Leer un número entero y si es múltiplo de 4 determinar si su último dígito es primo

num = int(input("digite numero"))

if num % 4 == 0:
    print(num,"es multiplo de 4")
    dig = num % 10
    x = 1
    c = 0
    while x <= dig:
        if dig % x == 0:
            c = c + 1
        x = x + 1

    if c == 2:
        print(dig,"es primo")
    else:
        print("no es primo")
else:
    print("no es multiplo de 4")            