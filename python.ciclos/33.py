#Si 32768 es el tope superior para los números entero cortos, determinar cuál es el
#número primo mas cercano por debajo de él.

num = 32749
cont = 0
for x in range(1,num+1):
    if num % x == 0:
        cont = cont +1
        
if cont == 2:
    print("el numero primo mas cercano a 32768 es",num)   
