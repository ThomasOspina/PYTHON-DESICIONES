#Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.

num = int(input("digite un numero"))

if (num > 9) and (num < 99):
    dig1 = num // 10
    dig2 = num % 10
    if dig1 % dig2 == 0:
        print(dig1,"es multiplo de",dig2)
    else:
        if dig2 % dig1 == 0:
            print(dig2,"es miltiplo de",dig1)
        else:
            print("no son multiplos")
else:
    print("no tienen dos digitos")            