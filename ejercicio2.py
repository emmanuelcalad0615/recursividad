#Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.
numInt=int(input("Ingrese un número entero de dos dígitos"))

if(numInt<10 and numInt>99):
    print("ingrese un número válido")
else:
    dig1=numInt//10
    dig2=numInt%10
    div=0
    
    
    for i in range(2, dig1, +1):
        if(dig1%i):
            div=div+1
    for j in range(2, dig2, +1):
        if(numInt%j):
            div=div+1
    
    if(div==0 ):
        print("Ambos dígitos son primos")
    else:
        print("Almenos uno de los dígitos no es primo")            
            

    