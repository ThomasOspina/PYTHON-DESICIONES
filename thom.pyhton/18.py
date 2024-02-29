#Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    print(dig1,dig2,dig3)
    if dig1 % dig2 == 0:
        print(dig1,"es multiplo de",dig2)

    if dig1 % dig3 == 0:
        print(dig1,"es multiplo de",dig3)    

    if dig2 % dig1 == 0:
        print(dig2,"es multiplo de",dig1)  

    if dig2 % dig3 == 0:
        print(dig2,"es multiplo de",dig3)   

    if dig3 % dig1 == 0:
        print(dig3,"es multiplo de",dig1)    

    if dig3 % dig2 == 0:
        print(dig3,"es multiplo de",dig2)
    else:
        print("ninguno es multiplo")       
else:
    print("no tiene tres digitos")