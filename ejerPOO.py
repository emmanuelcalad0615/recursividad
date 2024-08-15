class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

# Crear una instancia de Vehículo
mi_auto = Vehículo(200, 15000)

print("Velocidad máxima:", mi_auto.velocidad_maxima)
print("Kilometraje:", mi_auto.kilometraje)