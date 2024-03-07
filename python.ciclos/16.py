#Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n leído.

suma = 0
for x in range(3,31):
    if x % 3 == 0:
        suma = suma + x

promedio = suma // 10
print("el promedio es",promedio)        