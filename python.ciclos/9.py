#Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.

for x in range(25,206):
    if x % 10 == 6:
        print(x)