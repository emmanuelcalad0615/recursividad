class Punto:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def tamaño(self):
        #Utilizaré abs para obtener el valor absoluto de la operación, porque necesito valores positivos
        base = abs(self.esquina_inf_der.coord_x - self.esquina_sup_izq.coord_x)
        altura = abs(self.esquina_sup_izq.coord_y - self.esquina_inf_der.coord_y)
        return base, altura
    def Area(self, base, altura):
        area= base*altura
        return area
    def Perimetro(self,base, altura):
        perimetro= (base*2)+(altura*2)
        return perimetro

esquina_sup_izq = Punto(1, 4)
esquina_inf_der = Punto(6, 2)

rectangulo1 = Rectángulo(esquina_sup_izq, esquina_inf_der)

base, altura = rectangulo1.tamaño()

area=rectangulo1.Area(base,altura)


perimetro=rectangulo1.Perimetro(base,altura)


print(f"El triangulo es de {altura}X{base}")
print(f"El area es= {area}")
print(f"El perímetro= {perimetro}")