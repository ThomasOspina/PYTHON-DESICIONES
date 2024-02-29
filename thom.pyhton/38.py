#Leer tres números enteros y determinar si el último dígito de los tres números es igual.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))
num3 = int(input("digite un numero"))

a = num1 % 10
b = num2 % 10
c = num3 % 10
if a == b and a == c and b == c:
    print("los digitos son iguales")
else:  
    if a == b:
        print(a,"es igual a",b)

    if a == c:
        print(a,"es igual a",c)

    if b == c:
        print(b,"es igual a",c)        
    else:
        print("ningun digito es igual")

