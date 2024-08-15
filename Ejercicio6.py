#Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

numInt=int(input("Ingrese un número entero"))
numInt2=int(input("Ingrese un número entero"))

for i in range(numInt+1, numInt2, +1):

    if(i%10==4):
        print(i)

