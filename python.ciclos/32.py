#Leer números hasta que digiten 0 y determinar a cuanto es igual el promedio
#entero de los número primos leídos.

num = int(input("digite un numero"))

suma = 0
cont = 0
c = 0
while num > 0:
    num = int(input("digite un numero"))
    for x in range(1,num+1):
        if num % x == 0:
            c = c + 1

    if c == 2:
        suma = suma + num
        cont = cont + 1  
        c = 0 

promedio = suma // cont   
print("el promedio de los numeros primos es",promedio)
# malditos primos, nose