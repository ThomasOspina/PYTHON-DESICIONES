#26.Leer un número entero y determinar cuál es el mayor de sus dígitos.

num = int(input("digite un numero"))

dig = 0
mayor = 0
while num > 0:
    dig = num % 10
    if dig > mayor:
        mayor = dig
    num = num // 10 

print("el mayor digito es",mayor)       
