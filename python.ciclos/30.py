#Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos
#para quienes el sea un múltiplo.

num = int(input("digite un numero"))

for x in range(1,num+1):
    if num % x == 0:
        print(x)