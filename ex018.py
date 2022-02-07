import math

angulo = float(input('Digite o ângulo: '))



seno = math.sin(math.radians(angulo))
cosseno = math.acos(math.radians(angulo))
tangente = math.atan(math.radians(angulo))


print(f'Cosseno: {cosseno:.2f} \nSeno: {seno:.2f} \nTangente: {tangente:.2f}')