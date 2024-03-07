#Leer un número entero y mostrar en pantalla su tabla de multiplicar.

num = int(input("digite un numero"))

for x in range(1,11):
    print(num,"x",x,"=",num*x)