import numpy as np

valores = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(10)])

negativos = valores[valores < 0]
print("Valores negativos:", negativos)

positivos = valores[valores > 0]
soma_positivos = np.sum(positivos)
print("Soma dos valores positivos:", soma_positivos)





