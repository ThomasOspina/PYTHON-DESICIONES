#Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y
#mostrarlo en pantalla.

lista = []
a = 0
b = 1
for x in range(0,10):
    lista.append(a)
    c = a + b
    a = b
    b = c
    
print(lista)    