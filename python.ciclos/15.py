#Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.

suma = 0
for x in range(3,61):
    if x % 3 == 0:
        suma = suma + x

print(suma)        