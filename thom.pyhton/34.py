#Leer un número entero menor que mil y determinar cuántos dígitos tiene.

num = int(input("digite un numero"))

if num < 1000:
    print("es menor que mil")

    if num > 99 and num < 1000:
        print(num,"tiene tres digitos")

    if num > 9 and num < 100:
        print(num,"tiene dos digitos")

    if num > 0 and num < 10:
        print(num,"tiene un digito")        
else:
    print("no es menor que mil")