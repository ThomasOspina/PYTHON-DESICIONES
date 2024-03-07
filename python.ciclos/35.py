#Leer dos números enteros y determinar a cuánto es igual el producto mutuo del
#primer dígito de cada uno.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

dig1 = 0
c1 = 0
while num1 > 0:
    dig1 = num1 % 10
    c1 = dig1
    num1 = num1 // 10

dig2 = 0
c2 = 0
while num2 > 0:
    dig2 = num2 % 10
    c2 = dig2
    num2 = num2 // 10

producto = c1 * c2        
print("el producto de los primeros digitos es",producto)
