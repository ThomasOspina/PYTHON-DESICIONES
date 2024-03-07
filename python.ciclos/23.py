#Leer un número entero y determinar si la suma de sus dígitos es también un número primo.

num = int(input("digite un numero"))

suma = 0
x = 0
while num > 0:
    x = num % 10
    suma = suma + x
    num = num // 10

print(suma)
c = 0
for z in range(1,suma+1):
    if suma % z == 0:
        c  = c + 1

if c == 2:
    print("la suma es un numero primo")
else:
    print("la suma no es un numero primo")