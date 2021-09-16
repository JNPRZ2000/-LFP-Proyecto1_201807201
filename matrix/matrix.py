import sys
sys.path.insert(0,"doubleList")
from doubleList.vector import DoubleList

class MatrizV:
    
    def __init__(self):
        self.nombre = None
        self.filas = -1
        self.columnas = -1
        self.ancho = None
        self.alto = None
        self.filtros = []
        self.vf = None #vector filas
        self.vc = None #vector columnas
        self.vd = None #vector datos

    #Este método se usa para dar la dimensión a la matriz y crear sus espacios de memoria
    def dimensionar(self, filas, columnas):
        self.filas = filas #dimension filas
        self.columnas = columnas # dimension columnas
        self.vf = DoubleList()
        for i in range(self.filas):
            self.vc = DoubleList()
            for j in range(self.columnas):
                self.vc.Insert("#FFFFFF")
            self.vf.Insert(self.vc)
    
    def getDimensionFila(self):
        return self.filas
    
    def getDimensionColumna(self):
        return self.columnas

    def getElementByCoordinate(self, fila, columna):
        if fila >= self.filas or columna >= self.columnas:
            return IndexError
        elif fila < 0 or columna < 0:
            return IndexError
        else:
            filaactual = self.vf.cabeza
            while filaactual.id != fila:
                filaactual = filaactual.next
            columnaactual = filaactual.dato.cabeza
            while columnaactual.id != columna:
                columnaactual = columnaactual.next
            return columnaactual.dato

    def getIdMatByCoordinate(self, fila, columna):
        if fila >= self.filas or fila < 0 or columna < 0 or columna >= self.columnas:
            return IndexError
        else:
            filaactual = self.vf.cabeza
            while filaactual.id != fila:
                filaactual = filaactual.next
            columnaactual = filaactual.dato.cabeza
            while columnaactual.id != columna:
                columnaactual = columnaactual.next
            return columnaactual.idMat

    def setElementByCoordinate(self, fila, columna, dato):
        if fila >= self.filas or fila < 0 or columna < 0 or columna >= self.columnas:
            return IndexError
        else:
            filaactual = self.vf.cabeza
            while filaactual.id != fila:
                filaactual = filaactual.next
            columnaactual = filaactual.dato.cabeza
            while columnaactual.id != columna:
                columnaactual = columnaactual.next
            columnaactual.dato = dato
            columnaactual.idMat = "{},{}".format(fila,columna)

    def imprimir(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print("|{}|".format(self.getElementByCoordinate(i,j)), end="")
            print("")
    
    def imprimirIdMat(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print("|{}|".format(self.getIdMatByCoordinate(i,j)), end = "")
            print("")
    
    def setFiltros(self, filtro):
        if filtro in self.filtros:
            print("filtro {} repetido".format(filtro))
        else:
            self.filtros.append(filtro)
    def getFiltros(self):
        return self.filtros
    
    def setNombre(self, nombre):
        self.nombre = nombre 
    def getNombre(self):
        return self.nombre
    
    def setAncho(self, ancho):
        self.ancho = ancho
    def getAncho(self):
        return self.ancho

    def setAlto(self, alto):
        self.alto = alto
    def getAlto(self):
        return self.alto