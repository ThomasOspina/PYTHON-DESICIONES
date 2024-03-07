#Leer 2 números enteros y determinar cual de los dos tiene mayor cantidad de dígitos primos.
lista = [2,3,5,7]
num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

c1 = 0
cont1 = 0
c2 = 0
cont2 = 0
while num1 > 0:
    dig1 = num1 % 10
    num1 = num1 // 10
    for x in range(2,dig1):
        div1 = dig1 % x   
        if div1 == 0:
            cont1 = cont1 + 1
    if dig1 in lista:    
        c1 = c1 + 1
        print(dig1,"es primo")
        
while num2 > 0:
    dig2 = num2 % 10
    num2 = num2 // 10
    for z in range(2,dig2):
        div2 = dig2 % z   
        if div2 == 0:
            cont2 = cont2 + 1
    if dig2 in lista:    
        c2 = c2 + 1
        print(dig2,"es primo")
        
if c1 == c2:
    print("tienen la misma cantidad de digitos primos")   
    
if c1 > c2:
    print("el primer numero tiene mas digitos primos")
    
if c2 > c1:
    print("el segundo numero tiene mas digitos primos")                      