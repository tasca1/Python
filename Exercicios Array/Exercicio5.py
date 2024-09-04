import numpy as np

lista = np.array([1,387,98,33,3467,6,8745,5455454,56,4264526,])

valor_par = np.sum(lista % 2 == 0)

print("Existem ",valor_par,"valor(es) par(es)")