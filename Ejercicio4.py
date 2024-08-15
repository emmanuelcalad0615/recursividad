#Leer dos números enteros y determinar si la diferencia entre los dos es un número primo.
numInt=int(input("Ingrese un número entero: "))
numInt2=int(input("Ingrese un número entero: "))

dif=numInt-numInt2
print(f"{dif}")

div=0

for i in range(2, int(dif/2), +1):
    print(i)
    if(dif%i==0):
        div= div+1
if(div==0):
    print("La diferencia entre los dos números es un número primo")
else:
    print("La diferencia entre los dos números no es un número primo ")    
