#Leer un número entero y calcular el promedio entero de los factoriales de los
#enteros comprendidos entre 1 y el número leído.

num = int(input("digite un numero"))

fact = 0
cont = 1
suma = 0
for x in range(1,num+1):
    fact = x * cont
    cont = fact
    suma = suma + fact

promedio = suma // num
print("el promedio de los factoriales es",promedio) 
   