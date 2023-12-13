import random
from reference import referencia

bases = ["A", "C", "G", "T", "N"]


archivo = open("secuencias.py", "w")

chains = []
for j in range(510):
    chain = ""
    for i in referencia:
        if random.randint(0,50) == 1:
            chain = chain + bases[random.randint(0,4)]
        else:
            chain = chain + i
    chains.append(chain)
 
archivo.write(f"secuencias = {str(chains)}")

archivo.close
# complejidad: O(N^2)
