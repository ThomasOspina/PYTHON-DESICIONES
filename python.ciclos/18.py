#Leer dos números entero y mostrar todos los múltiplos de 5 comprendidos entre el menor y el mayor.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

for x in range(num1,num2+1):
    if x % 5 == 0:
        print(x)

for x in range(num2,num1+1):
    if x % 5 == 0:
        print(x)        