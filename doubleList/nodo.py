class Nodo:    
    def __init__(self, dato):
        self.dato = dato
        self.id = None
        self.next = None
        self.past = None
        self.idMat = None
    
    def __str__(self):
        return str(self.dato)