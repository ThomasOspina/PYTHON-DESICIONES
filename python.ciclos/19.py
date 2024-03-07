#Leer un número entero y determinar si es primo.

num = int(input("digite un numero"))

c = 0
for x in range(1,num+1):
    if num % x == 0:
        c = c + 1

if c == 2:
    print(num,"es primo")        
