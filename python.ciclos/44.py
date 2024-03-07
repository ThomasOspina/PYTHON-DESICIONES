#Leer un número y calcularle su factorial.

num = int(input("digite un numero"))

fact = 0
cont = 1
for x in range(1,num+1):
    fact = x * cont
    cont = fact

print("el factorial del numero es",cont)    