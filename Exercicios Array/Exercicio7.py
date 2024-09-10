import numpy as np

lista = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(10)])

maior_valor = np.max(lista)
posicao_maior_valor = np.argmax(lista)

print("O maior valor é: ", maior_valor)
print("A posição dele é: ", posicao_maior_valor)