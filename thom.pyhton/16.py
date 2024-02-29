#Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    dig3 = num % 10
    num = num // 10
    dig2 = num % 10
    dig1 = num // 10
    if dig1 == dig2 and dig1 == dig3:
        print("sus digitos son iguales")
    else:
        if dig1 == dig2:
            print(dig1,"es igual a",dig2)

        if dig1 == dig3:
            print(dig1,"es igual a",dig3)  
              
        if dig2 == dig3:
            print(dig2,"es igual a",dig3)    
        else:
            print("ninguno es igual")
else:
    print("no tiene tres digitos")