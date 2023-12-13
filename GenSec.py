import random

bases = ["A", "C", "G", "T", "N"]

referencia = open("data/referencia.txt", "r").read()
archivo = open("data/secuencias.txt", "w")

chain = ""
for j in range(510):
    if j != 0: chain = chain + "\n"
    for i in referencia:
        if random.randint(0,50) == 1:
            chain = chain + bases[random.randint(0,4)]
        else:
            chain = chain + i
 
archivo.write(chain)

archivo.close
# complejidad: O(N^2)
