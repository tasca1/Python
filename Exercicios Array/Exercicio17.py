import numpy as np

notas = [9.9, 9.7, 9.8, 10, 10]

notas_ordenadas = sorted(notas)

notas_reduzidas = notas_ordenadas[1:-1]

media_final = np.mean(notas_reduzidas)

print("A média final do quesito é:", media_final)