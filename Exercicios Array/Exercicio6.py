import numpy as np

lista = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(10)]) 

maior_valor = np.max(lista)
menor_valor = np.min(lista)

print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")