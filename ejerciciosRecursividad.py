#Cree una función recursiva que devuelva la última posición de un número n en una lista l
def retornar_ultimo(lista, i = 0):
    if len(lista) - 1 == i :
        return lista[i]
    if len(lista)  ==  0:
        return "La lista esta vacia"
    return retornar_ultimo(lista, i + 1)

lista = [1, 2, 5, 6, 77]
num = retornar_ultimo(lista)
#print(num)

#Cree una función recursiva que determine si un elemento e está en una lista l
def encontrar(lista, e, i = 0 ):
    if len(lista) == i :
        return False
    if lista[i] == e :
        return True
    
    return encontrar(lista, e, i+1)

e = 5
#print(encontrar(lista, e))

#Cree una función recursiva que sume los números pares de una lista l
def sumar (lista, i = 0, acum = 0):
    if len(lista) == i:
        return acum
    if lista[i] % 2 == 0:
        acum += lista[i]
    return sumar(lista, i+1, acum)

#print(sumar(lista))

#Cree una función recursiva que reciba un string s y remueva sus vocales

def remover(str, i = 0, strCon = ""):
    if len(str) == i:
        return strCon
    
    if str[i] not in "aeiou" and str[i] not in "AEIOU":
        strCon += str[i]

    return remover(str, i+1, strCon)    
str = "Emmanuel Calad Correa"
#print(remover(str))

#definir función recursiva que multiplique vía sumas sucesivas

def multiplicar(num1, num2, i = 0, acum = 0):
    if i == num2:
        return acum
    acum = acum + num1
    return multiplicar(num1, num2, i+1, acum)

#print(multiplicar(10, 507))

#cree una función recursiva que reciba un string y determine si tiene caracteres repetidos o no.

def encontrar_repetidos(str, anterior = "", i = 0):
    if len(str) == i:
        return False
    if anterior in str:
        return True
    anterior = str[i]
    return encontrar_repetidos(str, anterior, i+1)

str = "hkhr"
#print(encontrar_repetidos(str))

#Cree una función recursiva que reciba una lista y un número. La función debe retornar la posición del número si existe y si no, retornar un -1.

def retornar_posicion(n, lista, i = 0):
    if len(lista) == i: 
        return -1
    if lista[i] == n:
        return i
    return retornar_posicion(n, lista, i + 1)

#print(retornar_posicion(77, lista))
"""E1. Cree una función recursiva de cola que reciba un entero y retorne cuántos dígitos de este número son múltiplos de 2 y de 4. Ignore el cero.

Por ejemplo: si la función recibe el número 34523, deberá retornar 1 ya que hay sólo un número que es múltiplo de ambos números (el 4)."""
        
n = 44582
def contar_multiplos(n, div = 1, cont = 0 ):
    if n // div == 0:
        return cont
    n_nuevo = n // div
    residuo = n_nuevo % 10
    if residuo % 2 == 0 and residuo % 4 == 0:
        cont = cont + 1
    return contar_multiplos( n, div * 10, cont)

print(contar_multiplos(n))    




#print(encontrar_multiplos(18444))
str = "ay muchachos!"
def invertir_str(str, i = 1, k = 0, str_nv = "", str_reverse = ""):
    if k > len(str)/2:
        return str_nv + str_reverse
    str_nv += str [k]
    str_reverse += str [-i]

    return invertir_str(str, i+1, k+1, str_nv, str_reverse)

#print(invertir_str(str))

def sumar_numeros(matriz, i = 0, k = 0, acum = 0):
    if i == len(matriz):
        return  acum
    if matriz[i][k] % 2 != 0:
        acum += matriz[i][k]
    if k == len(matriz) - 1:
        return sumar_numeros(matriz, i + 1, 0, acum)
    return sumar_numeros(matriz, i, k + 1, acum)

    
matriz = [[1, 3, 5, 6 ],[4, 3, 5, 6], [2, 3, 9, 10], [1, 3, 43, 2]]
#print(sumar_numeros(matriz))

#Cree una función que reciba un lista con listas y números, por ejemplo [[[5,[4,3,[1]]]]] y devuelva cuál es la profundidad máxima en la que está ubicada algún número, en este caso la respuesta sería 5, ya que el 1 está a 5 accesos de profundidad ---> (1)


#Cree una función recursiva sin cola que reciba un un número y devuelva "cantidad par" o "cantidad impar" con base en la cantidad de dígitos que tiene. ----> (1)
def definir_par(n, div = 1):
    if n % div == n:
        return 0
    
    

    return 1 + definir_par(n, div * 10)    
    


    

#print(definir_par(23440))