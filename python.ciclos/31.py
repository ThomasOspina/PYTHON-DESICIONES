#Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los
#números terminados en 5.

num = int(input("digite un numero"))

suma = 0
cont = 0
while num > 0:
    num = int(input("digite un numero"))
    if num % 10 == 5:
        suma = suma + num
        cont = cont + 1

promedio = suma // cont         
print("el promedio de los numeros terminados en 5 es",promedio)