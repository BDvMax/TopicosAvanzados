# Situación: se registra un terreno cuadrado con un área aleatoria
# y se calcula cuánto mide cada lado.
import math
import random
import datetime

area = random.randint(1, 100)        # random: área del terreno en m2
lado = math.sqrt(area)               # math: lado = raíz cuadrada del área
fecha = datetime.date.today()        # datetime: fecha del registro

print("Área del terreno:", area, "m2")
print("Lado del terreno:", round(lado, 2), "m")
print("Fecha de registro:", fecha)
