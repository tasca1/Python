import numpy as np

n_candidatos = int(input("Digite o número total de candidatos: "))
n_votantes = int(input("Digite o número total de votantes: "))

votos = np.zeros(n_candidatos, dtype=int)

for i in range(n_votantes):
    voto = int(input(f"Digite o número do candidato que o votante {i+1} está votando (1 a {n_candidatos}): "))
    
    if 1 <= voto <= n_candidatos:
        votos[voto - 1] += 1  
    else:
        print("Número inválido.")

print("\nNúmero de votos de cada candidato:")
for i in range(n_candidatos):
    print(f"Candidato {i + 1}: {votos[i]} votos")