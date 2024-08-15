#Leer un número entero de 2 dígitos y si es par mostrar en pantalla la suma de sus dígitos, si es primo y menor que 10 mostrar en pantalla su último dígito y si es múltiplo de 5 y menor que 30 mostrar en pantalla el primer dígito.

numInt=int(input("Ingrese un número de dos dígitos"))
dig1=numInt//10
dig2=numInt%10
div=0
for i in range(2, numInt, 1):
        if(numInt%i==0):
            div=div+1

if(numInt<10 and numInt>99):
    print("Ingrese un número válido")
else:
    if(numInt%5==0 and numInt<30):
         print(f"El primer dígito de {numInt} es {dig1}")
    elif(numInt%2==0):
        suma=dig1+dig2
        print(f"La suma de los dígitos del número es= {suma}")
    elif(div==0):
         print(f"El último dígito de {numInt} es {dig2}")

         
        

            