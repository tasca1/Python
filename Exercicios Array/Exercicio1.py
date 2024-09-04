
import numpy as np

#a)
a = np.array([1, 0, 5 ,-2, -5, 7])

#b)
sub_a = a[0:3]
soma = 0
for i in sub_a:
    soma = soma + i
print(soma)  

#c)
a[4] = 100 
print(a)

#d)
soma1 = 0
for i in range(6):
    lista = a[i]
    print(lista)
