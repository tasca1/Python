import numpy as np

lista = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(6)])

lista_inversa = lista[::-1]

numeros_pares = lista[lista % 2 == 0]

print("Lista normal:", lista)
print("Lista inversa:", lista_inversa)
print("Números pares:", numeros_pares)