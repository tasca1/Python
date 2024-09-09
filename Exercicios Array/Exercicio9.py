import numpy as np

notas = np.array([float(input(f"Digite a {i+1} nota: ")) for i in range(15)])

media_notas = np.mean(notas)

print("A media das notas é", media_notas)




