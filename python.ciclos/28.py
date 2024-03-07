#Leer 2 números enteros y determinar cual de los dos tiene mayor cantidad de dígitos primos.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

c1 = 0
c2 = 0
dig1 = 0
dig2 = 0
cont1 = 0
cont2 = 0
while num1 > 0:
    dig1 = num1 % 10
    for x in range(1, dig1+1):
        if dig1 % x == 0:
            c1 = c1 + 1

    num1 = num1 // 10        
    if c1 == 2:
        cont1 = cont1 + 1
        c1 = 0

while num2 > 0:
    dig2 = num2 % 10
    for z in range(1, dig2+1):
        if dig2 % z == 0:
            c2 = c2 + 1
            
    num2 = num2 // 10
    if c2 == 2:
        cont2 = cont2 + 1
        c2 = 0

 
print(cont1,cont2)

if cont1 == cont2:
    print("tienen la misma cantidad de primos")

if cont1 > cont2:
    print("el primer numero tiene mas digitos primos")  

if cont2 > cont1:
    print("el segundo numero tiene mas digitos primos")   

# no pude        