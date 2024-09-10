import numpy as np

N = int(input("Digite o número de elementos do vetor: "))

vetor = np.zeros(N, dtype=int)


print("Digite os valores para o vetor:")
for i in range(N):
    vetor[i] = int(input(f"Elemento {i+1}: "))


vetor_pares = []
vetor_impares = []


for valor in vetor:
    if valor % 2 == 0:
        vetor_pares.append(valor)
    else:
        vetor_impares.append(valor)


vetor_pares = np.array(vetor_pares)
vetor_impares = np.array(vetor_impares)


print("\nVetor original:")
print(vetor)

print("\nVetor com valores pares:")
print(vetor_pares)

print("\nVetor com valores ímpares:")
print(vetor_impares)