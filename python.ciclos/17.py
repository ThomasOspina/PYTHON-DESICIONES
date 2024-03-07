#Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que
#los y primeros múltiplos de 5 para valores de x y y leídos.

suma = 0
for x in range(2,21):
    if x % 2 == 0:
        suma = suma + x

promedio = suma // 10

for z in range(1,31):
    if z % 5 == 0:
        if promedio > z:
            print(promedio,"es mayor a",z)