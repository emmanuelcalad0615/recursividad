def calcularFactorial(numero):
    if numero == 0: 
        return 1
    else:
        return numero * calcularFactorial(numero - 1)
    
print(calcularFactorial(3))    