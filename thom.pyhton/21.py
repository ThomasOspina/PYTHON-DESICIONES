#Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se
#encuentra el mayor dígito.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))
num3 = int(input("digite un numero"))

if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100) and (num3 > 9 and num2 < 100):
    print("tienen dos digitos")
    a1 = num1 // 10
    a2 = num1 % 10
    b1 = num2 // 10
    b2 = num2 % 10
    c1 = num3 // 10
    c2 = num3 % 10
    if a1 > a2 and a1 > b1 and a1 > b2 and a1 > c1 and a1 > c2:
        print(a1,"es el mayor")

    if a2 > a1 and a2 > b1 and a2 > b2 and a2 > c1 and a2 > c2:
        print(a2,"es el mayor")    

    if b1 > a1 and b1 > a2 and b1 > b2 and b1 > c1 and b1 > c2:
        print(b1,"es el mayor")    

    if b2 > a1 and b2 > a2 and b2 > b1 and b2 > c1 and a1 > c2:
        print(b2,"es el mayor")

    if c1 > a1 and c1 > a2 and c1 > b1 and c1 > b2 and c1 > c2:
        print(c1,"es el mayor")        

    if c2 > a1 and c2 > a2 and c2 > b1 and c2 > b2 and c2 > c1:
        print(c2,"es el mayor")    
else:
    print("no tienen dos digitos")