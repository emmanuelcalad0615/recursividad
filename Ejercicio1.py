numInt=int(input("Ingrese un número entero de 2 dígitos menor que 20: "))
div=0
if(numInt>=20):
    print("Ingrese un número válido")
else:    
    for j in range (2,int(numInt/2), +1):
        if(numInt%j==0):
            div=div+1

    if(div==0):
        print(f"El número {numInt} es primo")
    else:
        print(f"El número {numInt} no es primo")    
    
        
        