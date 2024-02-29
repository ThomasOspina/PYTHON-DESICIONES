#Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.

num1 = int(input("digite un numero"))
num2 = int(input("digite un numero"))

if (num1 > 9 and num1 < 100) and (num2 > 9 and num2 < 100):
    print("tienen dos digitos")
    num1dig1 = num1 // 10
    num1dig2 = num1 % 10
    num2dig1 = num2 // 10
    num2dig2 = num2 % 10
    if num1dig1 == num1dig2 and num1dig1 == num2dig1 and num1dig1 == num2dig2:
        print("los digitos son iguales")
    else:
        if num1dig1 == num1dig2:
            print(num1dig1,"es igual a",num1dig2)
        
        if num1dig1 == num2dig1:
            print(num1dig1,"es igual a",num2dig1)
            
        if num1dig1 == num2dig2:
            print(num1dig1,"es igual a",num2dig2)  
                
        if num1dig2 == num2dig1:
            print(num1dig2,"es igual a",num2dig1)  
                     
        if num1dig2 == num2dig2:
            print(num1dig2,"es igual a",num2dig2)   
                        
        if num2dig1 == num2dig2:
            print(num2dig1,"es igual a",num2dig2) 
        else:
            print("ninguno es igual") 
else:
    print("no tienen dos digitos")