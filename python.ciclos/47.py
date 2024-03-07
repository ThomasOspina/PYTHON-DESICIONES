#Leer un número entero y calcular a cuánto es igual la sumatoria de todos los
#factoriales de los números comprendidos entre 1 y el número leído.

num = int(input("digite un numero"))

fact = 0
cont = 1
suma = 0
for x in range(1,num+1):
    fact = x * cont
    cont = fact
    suma = suma + fact

print("la suma de los factoriales es",suma)    