#Determinar a cuánto es igual el promedio entero de los elementos de la serie de
#Fibonacci entre 0 y 1000.

a = 0
b = 1
suma = 1
cont = 1000
for x in range(1,101):
    c = a + b
    a = b
    b = c
    suma = suma + c
    
promedio = suma // cont
print("el promedio de fibonacci es",promedio)    