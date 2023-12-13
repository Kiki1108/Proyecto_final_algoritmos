from data.sec_class import sec_class
from data.Funciones import *
try: 
    from data.VectorSecuencias import secuencias as secs
except: 
    print("""ERROR: No se encotró el archivo VectorSecuencias.py. Intente usando el archivo GenSecClass.py""")
    quit()

print("CARGANDO...")
secuencias = []
referencia = open("data/referencia.txt", "r").read()

for sec in secs:
    secuencia = sec_class()
    secuencia.secuencia = sec[0]
    secuencia.mutaciones = sec[1]
    secuencia.por_mutacion = sec[2]
    secuencia.por_poli = sec[3]
    secuencia.id = sec[4]

    secuencias.append(secuencia)
# complejidad: O(N)

while True:
    print("""\nElija una opción:
(1) Imprimir referencia
(2) Imprimir secuencia #
(3) Imprimir mutaciones secuencia #
(4) Imprimir mutaciones lugar #
(5) Imprimir datos secuencia #
(6) Borrar secuencia
(7) Insertar secuencia
(8) Imprimir por % mutaciones
(9) Imprimir por % mutaciones polimorficas
(10) Guardar
(0) Guardar y salir """)
    
    opcion = input("")

    match opcion:
        case "1": print("referencia:\n", referencia)
        case "2": imprimir_sec(secuencias)
        case "3": imprimir_sec_mut_array(secuencias)
        case "4": imprimir_mut_pos(referencia, secuencias)
        case "5": imprimir_datos(secuencias)
        case "6": borrar_sec(secuencias)
        case "7": insert_sec(referencia, secuencias)
        case "8": imprimir_mutaciones(secuencias)
        case "9": imprimir_poli(secuencias)
        case "10": guardar(secuencias)
        case "0": guardar(secuencias); break
        case _: pass
# Complejidad O(inf)

