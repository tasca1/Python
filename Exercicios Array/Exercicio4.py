import numpy as np

lista = np.array([1,5,10,15,20,25,35,70])

x = int(input("Digite um número da ordem para somar: "))

y = int(input("Digite outro número da ordem para somar: "))

num1 = lista[x]
num2 = lista[y]

somatotal = num1 + num2
print(somatotal)