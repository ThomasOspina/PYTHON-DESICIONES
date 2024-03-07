#Determinar a cuánto es igual la suma de los elementos de la serie de Fibonacci entre 0 y 100.

a = 0
b = 1
suma = 1
for x in range(1,101):
    c = a + b
    a = b
    b = c
    suma = suma + c

print("la suma de fibonacci es",suma)    
