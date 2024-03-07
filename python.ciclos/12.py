#Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

num = int(input("digite un numero"))

if num > 99 and num < 1000:
    print("tiene tres digitos")
    c = 0
    x = 0
    while num > 0:
        x = num % 10
        if x == 1:
            c = c +1
        num = num // 10

    print("el numero tiene",c,"digitos iguales a 1")     
else:
    print("no tiene tres digitos")

# no se usa el ciclo    
            
