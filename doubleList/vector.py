#from doubleList.nodo import Nodo
import sys
sys.path.insert(0,"doubleList")
from doubleList.nodo import Nodo


class DoubleList:
    def __init__(self):
        self.size = 0
        self.cabeza = None
        self.cola = None
    
    def Size(self):
        return self.size
    
    def String(self):
        cadena = "["
        actual = self.cabeza
        continuar = True
        while continuar == True:
            if actual.next == None:
                cadena += str(actual.dato)+"-"+str(actual.id)+"]"
                continuar = False
            else:
                cadena += str(actual.dato)+"-"+str(actual.id)+","
                actual = actual.next
        return cadena
    
    def Insert(self, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nodo
            self.cabeza.id = 0
            self.cola = self.cabeza
        else:
            nodo.past = self.cola
            nodo.id = self.cola.id+1
            self.cola.next = nodo
            self.cola = nodo
        self.size += 1

    def InsertNode(self, dato, idMat):
        nodo = Nodo(dato, idMat)
        if self.cabeza == None:
            nodo.idMat = idMat
            self.cabeza = nodo
            self.cabeza.id = 0
            self.cola = self.cabeza
        else:
            nodo.idMat = idMat
            nodo.past = self.cola
            nodo.id = self.cola.id+1
            self.cola.next = nodo
            self.cola = nodo
        self.size +=1

    def Recorrer(self):
        actual = self.cabeza
        while actual:
            dato = actual.dato
            actual = actual.next
            yield dato
    def RecorrerID(self):
        actual = self.cabeza
        while actual:
            id = actual.id
            actual = actual.next
            yield id

    def RetornoPorID(self, id):
        if id == 0:
            return self.cabeza.dato
        else:
            actual = self.cabeza
            while actual.id != id:
                actual = actual.next
            return actual.dato
    
    def ChangeById(self, id, dato):
        actual = self.cabeza
        while actual.id != id:
            actual = actual.next
        actual.dato = dato

