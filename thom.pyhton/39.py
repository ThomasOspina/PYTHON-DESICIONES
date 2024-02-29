#Leer tres números enteros y determina si el penúltimo dígito de los tres números es igual.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))
num3 = int(input("digite un numero"))
  
a = num1 // 10
b = num2 // 10
c = num3 // 10
a1 = a % 10
b1 = b % 10
c1 = c % 10
print(a1,b1,c1)
if a1 == b1 and a == c1 and b1 == c1:
    print("los digitos son iguales")
else:  
    if a1 == b1:
        print(a1,"es igual a",b1)

    if a1 == c1:
        print(a1,"es igual a",c1)

    if b1 == c1:
        print(b1,"es igual a",c1)        
    else:
        print("ningun digito es igual")