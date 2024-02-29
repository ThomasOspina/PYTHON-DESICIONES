#Leer un número entero de 4 dígitos y determinar si el primer dígito es múltiplo de alguno de los otros dígitos.

num = int(input("digite un numero"))

if num > 999 and num < 10000:
    print("tiene cuatro digitos")
    dig4 = num % 10
    num = num // 10
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10 
    if dig1 % dig2 == 0:
        print(dig1,"es multiplo de",dig2)

    if dig1 % dig3 == 0:
        print(dig1,"es multiplo de",dig3) 

    if dig1 % dig4 == 0:
        print(dig1,"es multiplo de",dig4)    
    else:
        print("no es multiplo")   
else:
    print("no tiene 4 digitos")