import numpy as np

lista = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(6)])

lista_inversa = lista[::-1]

print("Lista normal", lista)

print("List inversa", lista_inversa)



