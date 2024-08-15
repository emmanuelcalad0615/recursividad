"""Suma de los n primeros enteros de una secuencia S"""
def suma(n, m, sum = 0):
    if m == 1:
        return sum
    num_str = str(n)
    sum += int(num_str[m])
    return suma(n, m - 1 , sum)
def suma2(n, m):
    if m == 0: 
        return 0
    n_str = str(n)
    num = n // 10 ** (len(n_str)-1)
    return num + suma2(n//10, m-1)
    

n = 12333
n_str = str(n)
num = n // 10 ** (len(n_str)-1)
print(num)