#Se define la serie de Fibonacci como la serie que comienza con los dígitos 1 y 0 y
#va sumando progresivamente los dos últimos elementos de la serie, así:
#0 1 1 2 3 5 8 13 21 34.......

a = 0
b = 1
print(a)
print(b)
for x in range(1,101):
    c = a + b
    a = b
    b = c
    print(c)
