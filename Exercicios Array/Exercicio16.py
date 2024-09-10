import numpy as np

#A) Leia um vetor A com N elementos já ordenados e um vetor B com M
#elementos também já ordenados.

elementos1 = int(input("Quantos elementos você gostaria de ter no Vetor A: "))
elementos2 = int(input("Quantos elementos você gostaria de ter no Vetor B: "))


valores1 = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(elementos1)])
valores2 = np.array([float(input(f"Digite o {i+1} número: ")) for i in range(elementos2)])

#B)Intercale os dois vetores A e B, formando um vetor C, sendo que ao
#final do processo de intercalação, o vetor C continue ordenado.
#Nenhum outro processo de ordenação poderá ser utilizado além da
#intercalação dos vetores A e B.

#Caso um vetor (A ou B) termine antes do outro, o vetor C deverá ser
#preenchido com os elementos do vetor que ainda possui informações.

valores3 = np.concatenate((valores1,valores2))

valores3_organizado = sorted(valores3)
for i in range(len(valores3)):
    print(valores3_organizado[i])














