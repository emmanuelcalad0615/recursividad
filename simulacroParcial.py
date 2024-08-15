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

#print(contar_multiplos(n))  

"""E2. Cree una función no recursiva de cola que invierta sólo la segunda mitad de un string.

Por ejemplo, si la función recibe "Hola", deberá retornar "Hoal".
Asuma que el punto medio es tamaño//2"""
 #ay muc!sohcah

def invertir(str, i = 1, str_nor = "", str_inv = ""):
    if i - 1 == len(str)//2:
        return str_nor + str_inv
    str_inv += str[-i]
    str_nor += str[i - 1]
    return invertir(str, i + 1, str_nor, str_inv)      
str = "ay muchachos!"
#print(invertir(str))

"""Cree una función recursiva de cola que calcule la sumatoria de todos los números impares de una matriz nxn.

Por ejemplo, si la función recibe la matriz m = [[1,2],[3,4]], deberá retornar 4 porque los únicos números impares de esta matriz son 1 y 3."""

def identificar_impares(m, i = 0, j = 0, cont = 0):
    if i == len(m):
        return cont
    if m[i][j] % 2 != 0:
        cont += m[i][j]
    if j == len(m[i]) - 1:
        return identificar_impares(m, i + 1, 0, cont)
    return identificar_impares(m, i, j + 1, cont)

m = [[1,2],[3,4]]
#print(identificar_impares(m))
"""E4. Cree una función recursiva que reciba una lista "l", un elemento "e" y un índice "i" y que retorne si el elemento "e" está en la lista "l" en la posición "i".

Por ejemplo, si recibe la lista l = [1,2,3], e=2 y i=0, debería retornar False porque en la posición 0 de l no hay un 2.
Nota: en este ejemplo se tendrá en cuenta el procedimiento para evitar que retornen False siempre y que pasen tres casos de prueba automáticamente."""

def encontrar(l, e, i, index = 0):
    if index == len(l):
        return False
    if l[index] == e and i == index:
        return True
    return encontrar(l, e, i, index + 1)
l = [2, 2, 3]
e = 3
i = 2
print(encontrar(l, e, i))

"""E5. Cree una función recursiva que reciba un string alfanumérico (letras y números) y que extraiga los dígitos del string y retorne el número formado por todos los dígitos. El retorno será de tipo entero.

Por ejemplo, si la función recibe "as34a5j6j35j2", deberá retornar el número 3456352.
Asuma que siempre habrá al menos un número en el string."""
str = "as34a5j6j35j2"
def retornar_numero(str, i = 0, cadena_nv = ""):
    if i == len(str):
        return cadena_nv
    num = str[i]
    if num.isdigit():
        cadena_nv += str[i]
    return retornar_numero(str, i +1, cadena_nv)    

print(retornar_numero(str))