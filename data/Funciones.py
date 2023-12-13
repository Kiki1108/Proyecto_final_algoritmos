from  data.arbol import *
from data.sec_class import sec_class

def buscar_mutaciones(reference, secuencias):
    for i in range(len(secuencias)):
        for j in range(len(secuencias[i].secuencia)):
            if reference[j] != secuencias[i].secuencia[j] and secuencias[i].secuencia[j] != "N":
                secuencias[i].mutaciones.append([j, secuencias[i].secuencia[j], False])
        secuencias[i].set_por_mutacion()
# Complejidad O(N^2)


def es_polimorfismo(secuencias):
    for i in range(len(secuencias)):
        for mutacion in secuencias[i].mutaciones:
            contador = 0
            mutacion[2] = False
            for sec in secuencias:
                if buscar_mutacion(sec.mutaciones, mutacion):
                    contador += 1
                if contador > len(secuencias)/100 + 1:
                    mutacion[2] = True
                    break
        secuencias[i].set_por_poli()
        match (int(i/len(secuencias)*500)):
            case 50: print("10%")
            case 100: print("20%")
            case 150: print("30%")
            case 200: print("40%")
            case 250: print("50%")
            case 300: print("60%")
            case 350: print("70%")
            case 400: print("80%")
            case 450: print("90%")
# complejidad O(N^3*log2(N))


def buscar_mutacion(mutaciones, mutacion):
    izq = 0 
    der = len(mutaciones) -1
    
    while izq <= der:
        actual = (der-izq)//2 + izq

        if mutaciones[actual][0] == mutacion[0] and  mutaciones[actual][1] == mutacion[1]:
            return True
        elif mutaciones[actual][0] > mutacion[0]:
            der = actual-1
        elif mutaciones[actual][0] < mutacion[0]:
            izq = actual+1
        elif mutaciones[actual][0] == mutacion[0]:
            return False
    return False
# complejidad O(log2(N))


def imprimir_sec(secuencias):
    while True:
        max, min = 0, float("inf")
        for secuencia in secuencias:
            if secuencia.id > max: max = secuencia.id
            if secuencia.id < min: min = secuencia.id
        print(f"\nElija una secuencia (ids entre {min}, {max})")
        try:
            num = int(input(""))
            control = False
            for secuencia in secuencias:
                if secuencia.id == num:
                    print(f"\n{secuencia.secuencia}\n")
                    control = True
                    break
            if not control:
                print("ERROR: Secuencia no encontrada")
            else: break
        except:
            pass       
# complejidad: O(inf)
# complejidad (sin while): O(N)


def imprimir_sec_mut_array(secuencias):
    while True:
        max, min = 0, float("inf")
        for secuencia in secuencias:
            if secuencia.id > max: max = secuencia.id
            if secuencia.id < min: min = secuencia.id
        print(f"\nElija una secuencia (ids entre {min}, {max})")
        try:
            num = int(input(""))
            control = False
            for secuencia in secuencias:
                if secuencia.id == num:
                    control = True
                    print(f"\n{secuencia.mutaciones}\n")
                    break
            if not control:
                print("ERROR: Secuencia no encontrada")
            else: break
        except:
            pass 
# complejidad: O(inf)
# complejidad (sin while): O(N)


def imprimir_mut_pos(referencia, secuencias):
    while True:
        print(f"\nElija una posición entre 0, {len(referencia)-1}")
        try:
            num = int(input(""))
            print(f"\nPosición: {num}")
            print(f"Originial: {referencia[num]}\n")
            for secuencia in secuencias:
                for mutacion in secuencia.mutaciones:
                    if mutacion[0] == num:
                        print(f"Sec:{secuencia.id}, {mutacion[1]}")
            break
        except:
            pass 
# complejidad: O(inf)
# complejidad (sin while): O(N^2)


def imprimir_datos(secuencias):
    while True:
        max, min = 0, float("inf")
        for secuencia in secuencias:
            if secuencia.id > max: max = secuencia.id
            if secuencia.id < min: min = secuencia.id
        print(f"\nElija una secuencia (ids entre {min}, {max})")
        try:
            num = int(input(""))
            control = False
            for secuencia in secuencias:
                if secuencia.id == num:
                    control = True
                    print(f"Id: {secuencia.id}")
                    print(f"Mutaciones: {len(secuencia.mutaciones)}")
                    print(f"% mutaciones: {int(secuencia.por_mutacion*100)/100}")
                    print(f"% mutaciones polimorficas: {int(secuencia.por_poli*100)/100}")
                    break
            if not control:
                print("ERROR: Secuencia no encontrada")
            else: break
        except:
            pass 
# complejidad: O(inf)
# complejidad (sin while): O(N)
    

def borrar_sec(secuencias):
    while True:
        max, min = 0, float("inf")
        for secuencia in secuencias:
            if secuencia.id > max: max = secuencia.id
            if secuencia.id < min: min = secuencia.id
        print(f"\nElija una secuencia (ids entre {min}, {max})")
        try:
            num = int(input(""))
        except:
            pass
        control = False
        for secuencia in secuencias:
            if secuencia.id == num:
                control = True
        if not control:
            print("ERROR: id de secuencia no encontrada")
        else:
            print(f"Secuencia {num} a borrar ¿está seguro?")
            print("(1) Si")
            print("(2) No")
            while True:
                opcion = input("")
                match opcion:
                    case "1": 
                        print("BORRANDO SECUENCIA...")
                        secuencias.pop(num)
                        print("RECARGANDO POLIMORFISMOS...")
                        es_polimorfismo(secuencias)
                        print("LISTO, SECUENCIA BORRADA\nPRESIONE ENTER PARA CONTINUAR")
                        input("")
                        break
                    case "2": break
                    case _ : pass 
            break
# complejidad: O(inf)
# complejidad (sin while): O(N^3*log2(N))


def insert_sec(referencia, secuencias):
    sec = None
    identificador = None

    # Pedir la secuencia
    while True:
        print(f"Escriba el archivo de la secuencia sola (txt)")
        nombre_archivo = input("")
        try:
            archivo = open(nombre_archivo, "r")
            sec = archivo.read()
        except:
            print("Archivo no encontrado")
            pass
        control = False
        for nucleotido in sec:
            if nucleotido not in ["A", "T", "C", "G", "N"]: 
                print("Secuencia no válida")
                control = True
                break
        if len(sec) != len(secuencias[0].secuencia) or control:
            print("Secuencia no concuerda con tamaño")
        else: break
    # complejidad: O(N)
    
    # Pedir la id
    while True:
        max = 0
        for secuencia in secuencias:
            if secuencia.id > max: max = secuencia.id
        print(f"Escriba id (Segurencia {max+1})")
        try:
            identificador = int(input(""))
        except:
            print("Id no válido")
            pass
        control = False
        for secuencia in secuencias:
            if secuencia.id == identificador:
                print("Id ya está en uso")
                control = True
                break
        if control: pass
        else: break
    # complejidad: O(N)

    secu = sec_class()
    secu.secuencia = sec
    secu.id = identificador

    secuencias.append(secu)
    buscar_mutaciones(referencia, secuencias)
    print(" RECARGANDO POLIMORFISMOS")
    es_polimorfismo(secuencias)
    ordenar_id(secuencias)
# complejidad: O(N^3*log2(N))


def ordenar_id(secuencias):
    lista_ordenada = []
    arbol = None
    for i in range(len(secuencias)):
        arbol = insertarNodo_id(arbol, secuencias[i])
    devolver_lista(arbol, lista_ordenada)

    return lista_ordenada
# complejidad: O(N)   


def imprimir_mutaciones(secuencias):
    ordenado = ordenar_mutacion(secuencias)
    for secuencia in ordenado:
        print(f"Sec: {secuencia.id}, {(int(secuencia.por_mutacion*100))/100}%")
# complejidad: O(N)


def ordenar_mutacion(secuencias):
    lista_ordenada = []
    arbol = None
    for i in range(len(secuencias)):
        arbol = insertarNodo_mut(arbol, secuencias[i])
    devolver_lista(arbol, lista_ordenada)

    return lista_ordenada
# complejidad: O(N)


def imprimir_poli(secuencias):
    ordenado = ordenar_poli(secuencias)
    for secuencia in ordenado:
        print(f"Sec: {secuencia.id}, {(int(secuencia.por_poli*100))/100}%")
# complejidad: O(N)


def ordenar_poli(secuencias):
    lista_ordenada = []
    arbol = None
    for i in range(len(secuencias)):
        arbol = insertarNodo_poli(arbol, secuencias[i])
    devolver_lista(arbol, lista_ordenada)

    return lista_ordenada
# complejidad: O(N)

def guardar(secuencias):
    archivo = open("data/VectorSecuencias.py", "w")

    chains = []
    for secuencia in secuencias:
        chain = [secuencia.secuencia,
                secuencia.mutaciones, 
                secuencia.por_mutacion,
                secuencia.por_poli, 
                secuencia.id]
        chains.append(chain)

    archivo.write(f"secuencias = {str(chains)}")
    archivo.close

    print("LISTO, ARCHIVO GENERADO")
# complejidad: O(N)