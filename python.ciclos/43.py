#Determinar cuántos elementos de la serie de Fibonacci se encuentran entre 1000 y 2000.

a = 0
b = 1
for x in range(1,101):
    c = a + b
    a = b
    b = c
    if c > 999 and c < 2001:
        print(c)