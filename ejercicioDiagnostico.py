import random
n = 3
class Juego: 
    pass

class Saltamonte: 
    def __init__(self):
        self.posicion: list =[random.randint(0, n - 1), random.randint(0, n - 1)]
        
    def mover_saltamontes(self) -> tuple[int]:
        x = self.posicion[0]
        y = self.posicion[1]
        x_nueva = random.randint(0, n - 1)
        y_nueva = random.randint(0, n - 1) 
        self.posicion[0] = x_nueva
        self.posicion[1] = y_nueva
        return x, y   

    
        

class Cesped: 
    def __init__(self, n: int, saltamonte: Saltamonte ):
        self.matriz: list[list] = []
        self.saltamontes: Saltamonte = saltamonte
        self.n: int = n

    def crearCesped(self) -> list[list]:
        for i in range(0, self.n):
            fila = []
            for i in range(0, self.n):
                fila.append(0)
            self.matriz.append(fila)    
        return self.matriz     
    
    def posicionar(self):
        

        
        self.matriz[self.saltamontes.posicion[0]][self.saltamontes.posicion[1]] = self.saltamontes

obj_saltamonte = Saltamonte()

obj_cesped = Cesped(n, obj_saltamonte)

matriz = obj_cesped.crearCesped()

print(matriz)

_ =obj_saltamonte.mover_saltamontes()
obj_cesped.posicionar()
print(matriz)
_ =obj_saltamonte.mover_saltamontes()
obj_cesped.posicionar()


print(matriz)






