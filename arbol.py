class nodoArbol(object):
    def __init__(self, secuencia):
        self.izq = None
        self.der = None
        self.secuencia = secuencia

def insertarNodo_mut(raiz, secuencia):
    if(raiz is None):
        raiz = nodoArbol(secuencia)
    elif(secuencia.por_mutacion < raiz.secuencia.por_mutacion):
        raiz.izq = insertarNodo_mut(raiz.izq,secuencia)
    else:
        raiz.der = insertarNodo_mut(raiz.der,secuencia)
    return raiz
# complejidad O(log2(N))


def insertarNodo_poli(raiz, secuencia):
    if(raiz is None):
        raiz = nodoArbol(secuencia)
    elif(secuencia.por_poli < raiz.secuencia.por_poli):
        raiz.izq = insertarNodo_poli(raiz.izq,secuencia)
    else:
        raiz.der = insertarNodo_poli(raiz.der,secuencia)
    return raiz
# complejidad O(log2(N))


def devolver_lista(raiz, lista):
    if(raiz is not None):
        devolver_lista(raiz.izq, lista)
        lista.append(raiz.secuencia)
        devolver_lista(raiz.der, lista)
# complejidad O(N)
