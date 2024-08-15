#Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.

x=int(input("Ingrese el número de multiplos de 2: "))
y=int(input("Ingrese el número de multiplos de 5: "))



for i in range (2, (x*2)+2, 2):
    sumaM2=i+i
for j in range (5, (x*5)+5, 5):
    sumaM5=j+j

print(sumaM2)    
print(sumaM5)    
promM2=sumaM2/x
promM5=sumaM5/y

print(promM2)
print(promM5)


if(promM2>promM5):
    print("El promedio de los multiplos de 2 es mayor que el promedio de los multiplos de 5")
elif(promM5>promM2):
    print("El promedio de los multiplos de 5 es mayor que el promedio de los multiplos de 2")
else:
    print("EL promedio de los multiplos de 2 es igual a promedio de los multiplos de 5")
    




