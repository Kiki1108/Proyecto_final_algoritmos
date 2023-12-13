
class sec_class(object):
    def __init__(self):
        self.secuencia = None
        self.mutaciones = []
        self.por_mutacion = 0
        self.por_poli = 0
        self.id = None
    
    def set_sec(self, secuencia):
        self.secuencia = secuencia
    
    def set_mut(self, mutaciones):
        self.mutaciones = mutaciones

    def set_por_mutacion(self):
        self.por_mutacion = len(self.mutaciones)/len(self.secuencia)*100
    
    def set_por_poli(self):
        polimorfismos = 0
        for mutacion in self.mutaciones:
            if mutacion[2]: polimorfismos += 1
        self.por_poli = (polimorfismos/len(self.mutaciones))*100
        # complejidad: O(N)
    
    def set_id(self, id):
        self.id = id
    