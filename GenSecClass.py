from reference import referencia
from secuencias import secuencias
from sec_class import sec_class
from Funciones import *

print("CARGANDO...")

vector_secuencias = []

# creación de la clase secuencia para cada una de las secuencias
print("CREANDO CLASES")
for i in range(len(secuencias)):
    sec = sec_class()
    sec.set_sec(secuencias[i])
    vector_secuencias.append(sec)
    vector_secuencias[i].set_id(i)

# Búsqueda secuencial de mutaciones
# Agrega una array [posición, mutación] al array vector_secuencias[i].mutaciones
print("BUSCANDO MUTACIONES")
buscar_mutaciones(referencia, vector_secuencias)

# Analizar los polimorfirmos
print("BUSCANDO POLIMORFISMOS")
es_polimorfismo(vector_secuencias)

print("GENERANDO ARCHIVO")
archivo = open("VectorSecuencias.py", "w")

chains = []
for secuencia in vector_secuencias:
    chain = [secuencia.secuencia,
             secuencia.mutaciones, 
             secuencia.por_mutacion,
             secuencia.por_poli, 
             secuencia.id]
    chains.append(chain)

archivo.write(f"secuencias = {str(chains)}")
archivo.close

print("LISTO, ARCHIVO GENERADO")