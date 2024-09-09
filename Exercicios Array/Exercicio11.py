import numpy as np

numeros = np.array([float(input(f"Digite o {i+1}º número: ")) for i in range(20)])

numeros_invertidos = np.flip(numeros)

print("Array FLIPADA:", numeros_invertidos)



