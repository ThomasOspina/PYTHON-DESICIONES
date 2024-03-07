#Si 32768 es el tope superior para los números entero cortos, determinar cuál es el
#número primo mas cercano por debajo de él.

c = 0
for x in range (1,327443+1):
    if 32768 % x == 0:
        c = c + 1

if c == 2:
    print("es primo")     

#me cago en los primos, nose     