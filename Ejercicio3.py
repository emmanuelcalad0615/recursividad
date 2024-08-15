#Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10 entonces mostrar en pantalla todos los enteros comprendidos entre el menor y el mayor de los números leídos.

numInt=int(input("Ingrese un número entero: "))
numInt2=int(input("Ingrese un número entero: "))

dif=numInt-numInt2

if(dif<=10):
    if(numInt<numInt2):
         print(f"Los número comprendidos entre {numInt2} y {numInt}")
         for i in range(numInt+1, numInt2, +1):
              print(f"{i}")
    elif(numInt2<numInt):
         print(f"Los número comprendidos entre {numInt} y {numInt2}")
         for j in range(numInt2+1, numInt, +1):
              print(f"{j}")
else:
     print("La diferencia entre los números es mayor a 10")              
           