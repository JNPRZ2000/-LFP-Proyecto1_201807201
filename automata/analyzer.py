from automata.Error import Error
from automata.Token import Token
from matrix.matrix import MatrizV

class Analyzer:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.listaMatrices = []
        self.linea = 1
        self.columna = 1
        self.i = 0
        self.estado = "titulo0"
        self.anterior = "titulo0"
        self.buffer = ''
        self.x = None
        self.y = None
        self.f = None
        self.c = None
        self.ancho = None
        self.alto = None
        self.bool = None
        self.matrix = MatrizV()

    def agregar_token(self, caracter, token, linea, columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ""

    def agregar_error(self, caracter, linea, columna):
        self.listaErrores.append(Error(caracter,linea,columna))

    def analizar(self, texto):
        self.i = 0
        while self.i < len(texto):
            if self.estado == "titulo0":
                self.titulo0(texto[self.i])
            elif self.estado == "titulo1":
                self.titulo1(texto[self.i])
            elif self.estado == "titulo2":
                self.titulo2(texto[self.i])
            elif self.estado == "titulo3":
                self.titulo3(texto[self.i])
            elif self.estado == "titulo4":
                self.titulo4(texto[self.i])
            elif self.estado == "titulo5":
                self.titulo5(texto[self.i])
            elif self.estado == "igual":
                self.igual(texto[self.i])
            elif self.estado == "puntocoma":
                self.puntocoma(texto[self.i])
            elif self.estado == "nombre0":
                self.nombre0(texto[self.i])
            elif self.estado == "nombre1":
                self.nombre1(texto[self.i])
            elif self.estado == "ancho0":
                self.ancho0(texto[self.i])
            elif self.estado == "ancho1":
                self.ancho1(texto[self.i])
            elif self.estado == "ancho2":
                self.ancho2(texto[self.i])
            elif self.estado == "ancho3":
                self.ancho3(texto[self.i])
            elif self.estado == "ancho4":
                self.ancho4(texto[self.i])
            elif self.estado == "width":
                self.width(texto[self.i])
            elif self.estado == "alto0":
                self.alto0(texto[self.i])
            elif self.estado == "alto1":
                self.alto1(texto[self.i])
            elif self.estado == "alto2":
                self.alto2(texto[self.i])
            elif self.estado == "alto3":
                self.alto3(texto[self.i])
            elif self.estado == "height":
                self.height(texto[self.i])
            elif self.estado == "filas0":
                self.filas0(texto[self.i])
            elif self.estado == "filas1":
                self.filas1(texto[self.i])
            elif self.estado == "filas2":
                self.filas2(texto[self.i])
            elif self.estado == "filas3":
                self.filas3(texto[self.i])
            elif self.estado == "filas4":
                self.filas4(texto[self.i])
            elif self.estado == "rows":
                self.rows(texto[self.i])
            elif self.estado == "columnas0":
                self.columnas0(texto[self.i])
            elif self.estado == "columnas1":
                self.columnas1(texto[self.i])
            elif self.estado == "columnas2":
                self.columnas2(texto[self.i])
            elif self.estado == "columnas3":
                self.columnas3(texto[self.i])
            elif self.estado == "columnas4":
                self.columnas4(texto[self.i])
            elif self.estado == "columnas5":
                self.columnas5(texto[self.i])
            elif self.estado == "columnas6":
                self.columnas6(texto[self.i])
            elif self.estado == "columnas7":
                self.columnas7(texto[self.i])
            elif self.estado == "column":
                self.column(texto[self.i])
            elif self.estado == "celdas0":
                self.celdas0(texto[self.i])
            elif self.estado == "celdas1":
                self.celdas1(texto[self.i])
            elif self.estado == "celdas2":
                self.celdas2(texto[self.i])
            elif self.estado == "celdas3":
                self.celdas3(texto[self.i])
            elif self.estado == "celdas4":
                self.celdas4(texto[self.i])
            elif self.estado == "celdas5":
                self.celdas5(texto[self.i])
            elif self.estado == "body0":
                self.body0(texto[self.i])
            elif self.estado == "body1":
                self.body1(texto[self.i])
            elif self.estado == "body2":
                self.body2(texto[self.i])
            elif self.estado == "body3":
                self.body3(texto[self.i])
            elif self.estado == "true0":
                self.true0(texto[self.i])
            elif self.estado == "true1":
                self.true1(texto[self.i])
            elif self.estado == "true2":
                self.true2(texto[self.i])
            elif self.estado == "true3":
                self.true3(texto[self.i])
            elif self.estado == "false0":
                self.false0(texto[self.i])
            elif self.estado == "false1":
                self.false1(texto[self.i])
            elif self.estado == "false2":
                self.false2(texto[self.i])
            elif self.estado == "false3":
                self.false3(texto[self.i])
            elif self.estado == "false4":
                self.false4(texto[self.i])
            elif self.estado == "color0":
                self.color0(texto[self.i])
            elif self.estado == "color1":
                self.color1(texto[self.i])
            elif self.estado == "body4":
                self.body4(texto[self.i])
            elif self.estado == "body5":
                self.body5(texto[self.i])
            elif self.estado == "filtros0":
                self.filtros0(texto[self.i])
            elif self.estado == "filtros1":
                self.filtros1(texto[self.i])
            elif self.estado == "filtros2":
                self.filtros2(texto[self.i])
            elif self.estado == "filtros3":
                self.filtros3(texto[self.i])
            elif self.estado == "filtros4":
                self.filtros4(texto[self.i])
            elif self.estado == "filtros5":
                self.filtros5(texto[self.i])
            elif self.estado == "filtros6":
                self.filtros6(texto[self.i])
            elif self.estado == "mirror0":
                self.mirror0(texto[self.i])
            elif self.estado == "mirror1":
                self.mirror1(texto[self.i])
            elif self.estado == "mirror2":
                self.mirror2(texto[self.i])
            elif self.estado == "mirror3":
                self.mirror3(texto[self.i])
            elif self.estado == "mirror4":
                self.mirror4(texto[self.i])
            elif self.estado == "mirror5":
                self.mirror5(texto[self.i])
            elif self.estado == "mirrorx":
                self.mirrorx(texto[self.i])
            elif self.estado == "mirrory":
                self.mirrory(texto[self.i])
            elif self.estado == "double0":
                self.double0(texto[self.i])
            elif self.estado == "double1":
                self.double1(texto[self.i])
            elif self.estado == "double2":
                self.double2(texto[self.i])
            elif self.estado == "double3":
                self.double3(texto[self.i])
            elif self.estado == "double4":
                self.double4(texto[self.i])
            elif self.estado == "double5":
                self.double5(texto[self.i])
            elif self.estado == "double6":
                self.double6(texto[self.i])
            elif self.estado == "double7":
                self.double7(texto[self.i])
            elif self.estado == "double8":
                self.double8(texto[self.i])
            elif self.estado == "double9":
                self.double9(texto[self.i])
            elif self.estado == "double10":
                self.double10(texto[self.i])
            elif self.estado == "double11":
                self.double11(texto[self.i])
            elif self.estado == "espacio":
                self.espacio(texto[self.i])
            elif self.estado == "arrobas":
                self.arroba(texto[self.i])
            elif self.estado == "coma":
                self.coma(texto[self.i])
            self.i +=1

    def titulo0(self, caracter):
        if caracter == "T":
            self.buffer += caracter
            self.columna += 1
            self.estado = "titulo1"
        else:
            self.comprobar(caracter)
    def titulo1(self, caracter):
        if caracter == "I":
            self.buffer += caracter
            self.columna += 1
            self.estado = "titulo2"
        else:
            self.comprobar(caracter)   
    def titulo2(self, caracter):
        if caracter == "T":
            self.buffer += caracter
            self.columna += 1
            self.estado = "titulo3"
            self.anterior = "titulo2"
        else:
            self.comprobar(caracter)         
    def titulo3(self, caracter):
        if caracter == "U":
            self.buffer += caracter
            self.columna += 1
            self.estado = "titulo4"
            self.anterior = "titulo3"
        else:
            self.comprobar(caracter)   
    def titulo4(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "titulo5"
            self.anterior = "titulo4"
        else:
            self.comprobar(caracter)   
    def titulo5(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.agregar_token(self.buffer,'titulo',self.linea,self.columna)
            self.columna += 1            
            self.estado = "igual"
            self.anterior = "titulo5"
        else:
            self.comprobar(caracter)
    
    def igual(self, caracter):
        if caracter == "=":
            self.buffer += caracter
            self.agregar_token(self.buffer, 'igual', self.linea, self.columna)
            self.columna += 1
            if self.anterior == "titulo5":
                self.estado = "nombre0"
            elif self.anterior == "ancho4":
                self.estado = "width"
            elif self.anterior == "alto3":
                self.estado = "height"
            elif self.anterior == "filas4":
                self.estado = "rows"
            elif self.anterior == "columnas7":
                self.estado = "column"
            elif self.anterior == "celdas5":
                self.estado = "body0"
            elif self.anterior == "filtros6":
                self.estado = "mirror0"
            self.anterior = "igual"
        else:
            self.comprobar(caracter)

    def nombre0(self, caracter):
        if caracter == "\"":
            self.buffer += caracter
            self.agregar_token(self.buffer,'comilla',self.linea, self.columna)
            if self.anterior == "nombre1":
                self.estado = "puntocoma"
                self.anterior = "nombre0"
                self.columna += 1
            else:
                self.estado = "nombre1"
                self.anterior = "nombre0"
                self.columna+=1
        else:
            self.comprobar(caracter)
    def nombre1(self, caracter):
        if caracter != "\"":
            self.buffer += caracter
            self.columna +=1
        else:
            self.i -= 1
            self.matrix.setNombre(self.buffer)
            self.agregar_token(self.buffer, 'nombre', self.linea, self.columna)
            self.anterior = "nombre1"
            self.estado = "nombre0"
    
    def puntocoma(self, caracter):
        if caracter == ";":
            self.buffer += caracter 
            self.agregar_token(self.buffer, 'punto y coma', self.linea, self.columna)
            self.columna += 1
            if self.anterior == "nombre0":
                self.estado = "ancho0"
                self.anterior = "puntocoma"
            elif self.anterior == "width":
                self.estado = "alto0"
            elif self.anterior == "height":
                self.estado = "filas0"
            elif self.anterior == "rows":
                self.estado = "columnas0"
            elif self.anterior == "column":
                self.estado = "celdas0"
            elif self.anterior == "body5":
                self.estado = "filtros0"
            elif self.anterior == "filter":
                self.listaMatrices.append(self.matrix)
                self.matrix = MatrizV()
                self.estado = "espacio"
        else:
            self.comprobar(caracter)
    
    def ancho0(self, caracter):
        if caracter == "A":
            self.buffer += caracter
            self.columna += 1
            self.estado = "ancho1"
        else:
            self.comprobar(caracter)
    def ancho1(self, caracter):
        if caracter == "N":
            self.buffer += caracter
            self.columna += 1
            self.estado = "ancho2"
        else:
            self.comprobar(caracter)
    def ancho2(self, caracter):
        if caracter == "C":
            self.buffer += caracter
            self.columna += 1
            self.estado = "ancho3"
        else:
            self.comprobar(caracter)
    def ancho3(self, caracter):
        if caracter == "H":
            self.buffer += caracter
            self.columna += 1
            self.estado = "ancho4"
        else:
            self.comprobar(caracter)
    def ancho4(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.agregar_token(self.buffer,'ancho',self.linea,self.columna)
            self.columna += 1
            self.estado = "igual"
            self.anterior = "ancho4"
        else:
            self.comprobar(caracter)
    def width(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        elif caracter == ";":
            self.i -= 1
            self.matrix.setAncho(int(self.buffer))
            self.agregar_token(self.buffer, "width", self.linea, self.columna)
            self.estado = "puntocoma"
            self.anterior = "width"
        else:
            self.comprobar(caracter)
    
    def alto0(self, caracter):
        if caracter == "A":
            self.buffer += caracter
            self.columna += 1
            self.estado = "alto1"
        else:
            self.comprobar(caracter)
    def alto1(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "alto2"
        else:
            self.comprobar(caracter)
    def alto2(self, caracter):
        if caracter == "T":
            self.buffer += caracter
            self.columna += 1
            self.estado = "alto3"
        else:
            self.comprobar(caracter)
    def alto3(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.agregar_token(self.buffer, "alto", self.linea, self.columna)
            self.columna += 1
            self.estado = "igual"
            self.anterior = "alto3"
        else:
            self.comprobar(caracter)
    def height(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        elif caracter == ";":
            self.i -= 1
            self.matrix.setAlto(int(self.buffer))
            self.agregar_token(self.buffer, 'height', self.linea, self.columna)
            self.estado = "puntocoma"
            self.anterior = "height"
        else:
            self.comprobar(caracter)

    def filas0(self, caracter):
        if caracter == "F":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filas1"
        else:
            self.comprobar(caracter)
    def filas1(self, caracter):
        if caracter == "I":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filas2"
        else:
            self.comprobar(caracter)
    def filas2(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filas3"
        else:
            self.comprobar(caracter)
    def filas3(self, caracter):
        if caracter == "A":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filas4"
        else:
            self.comprobar(caracter)
    def filas4(self, caracter):
        if caracter == "S":
            self.buffer += caracter
            self.agregar_token(self.buffer, "filas", self.linea, self.columna)
            self.columna += 1
            self.estado = "igual"
            self.anterior = "filas4"
        else:
            self.comprobar(caracter)
    def rows(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        elif caracter == ";":
            self.i -= 1
            self.f = int(self.buffer)
            self.agregar_token(self.buffer, "rows", self.linea, self.columna)
            self.estado = "puntocoma"
            self.anterior = "rows"
        else:
            self.comprobar(caracter)

    def columnas0(self, caracter):
        if caracter == "C":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas1"
        else:
            self.comprobar(caracter)
    def columnas1(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas2"
        else:
            self.comprobar(caracter)
    def columnas2(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas3"
        else:
            self.comprobar(caracter)
    def columnas3(self, caracter):
        if caracter == "U":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas4"
        else:
            self.comprobar(caracter)
    def columnas4(self, caracter):
        if caracter == "M":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas5"
        else:
            self.comprobar(caracter)
    def columnas5(self, caracter):
        if caracter == "N":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas6"
        else:
            self.comprobar(caracter)
    def columnas6(self, caracter):
        if caracter == "A":
            self.buffer += caracter
            self.columna += 1
            self.estado = "columnas7"
        else:
            self.comprobar(caracter)
    def columnas7(self, caracter):
        if caracter == "S":
            self.buffer += caracter
            self.agregar_token(self.buffer, "columnas", self.linea, self.columna)
            self.columna += 1
            self.estado = "igual"
            self.anterior = "columnas7"
        else:
            self.comprobar(caracter)
    def column(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna += 1
        else:
            self.i -= 1
            self.c = int(self.buffer)
            self.matrix.dimensionar(self.f,self.c)
            self.f = None
            self.c = None
            self.agregar_token(self.buffer, "column", self.linea, self.columna)
            self.estado = "puntocoma"
            self.anterior = "column"

    def celdas0(self, caracter):
        if caracter == "C":
            self.buffer += caracter
            self.columna += 1
            self.estado = "celdas1"
        else:
            self.comprobar(caracter)
    def celdas1(self, caracter):
        if caracter == "E":
            self.buffer += caracter
            self.columna += 1
            self.estado = "celdas2"
        else:
            self.comprobar(caracter)
    def celdas2(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "celdas3"
        else:
            self.comprobar(caracter)
    def celdas3(self, caracter):
        if caracter == "D":
            self.buffer += caracter
            self.columna += 1
            self.estado = "celdas4"
        else:
            self.comprobar(caracter)
    def celdas4(self, caracter):
        if caracter == "A":
            self.buffer += caracter
            self.columna += 1
            self.estado = "celdas5"
        else:
            self.comprobar(caracter)
    def celdas5(self, caracter):
        if caracter == "S":
            self.buffer += caracter
            self.agregar_token(self.buffer, "celdas", self.linea, self.columna)
            self.columna += 1
            self.estado = "igual"
            self.anterior = "celdas5"
        else:
            self.comprobar(caracter)

    def body0(self, caracter):
        if caracter == "{":
            self.buffer += "{"
            self.agregar_token(self.buffer, 'apertura P', self.linea, self.columna)
            self.columna +=1
            self.estado = "body1"

        else:
            self.comprobar(caracter)
    def body1(self, caracter):
        if caracter == "[":
            self.buffer += "["
            self.agregar_token(self.buffer, 'apertura S', self.linea, self.columna)
            self.columna +=1
            self.estado = "body2"
        else:
            self.comprobar(caracter)
    def body2(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
        else:
            self.i -= 1
            self.x = int(self.buffer)
            self.agregar_token(self.buffer, 'x', self.linea, self.columna)
            self.estado = "coma"
            self.anterior = "body2"    
    def body3(self, caracter):
        if caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
        else:
            self.i -= 1
            self.y = int(self.buffer)
            self.agregar_token(self.buffer, 'y', self.linea, self.columna)
            self.estado = "coma"
            self.anterior = "body3"
    
    def true0(self, caracter):
        if caracter == "T":
            self.buffer += caracter
            self.columna += 1
            self.estado = "true1"
        else:
            self.i -= 1
            self.estado = "false0"
    def true1(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna += 1
            self.estado = "true2"
        else:
            self.comprobar(caracter)
    def true2(self, caracter):
        if caracter == "U":
            self.buffer += caracter
            self.columna += 1
            self.estado = "true3"
        else:
            self.comprobar(caracter)
    def true3(self, caracter):
        if caracter == "E":
            self.buffer += caracter
            self.bool = True
            self.agregar_token(self.buffer, "true", self.linea, self.columna)
            self.columna += 1
            self.anterior = "true3"
            self.estado = "coma"
        else:
            self.comprobar(caracter)

    def false0(self, caracter):
        if caracter == "F":
            self.buffer += caracter
            self.columna += 1
            self.estado = "false1"
        else:
            self.comprobar(caracter)
    def false1(self, caracter):
        if caracter == "A":
            self.buffer += caracter
            self.columna += 1
            self.estado = "false2"
        else:
            self.comprobar(caracter)
    def false2(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "false3"
        else:
            self.comprobar(caracter)
    def false3(self, caracter):
        if caracter == "S":
            self.buffer += caracter
            self.columna += 1
            self.estado = "false4"
        else:
            self.comprobar(caracter)
    def false4(self, caracter):
        if caracter == "E":
            self.buffer += caracter
            self.bool = False
            self.agregar_token(self.buffer, "false", self.linea, self.columna)
            self.columna += 1
            self.estado = "coma"
            self.anterior = "false4"
        else:
            self.comprobar(caracter)

    def color0(self, caracter):
        if caracter == "#":
            self.buffer += caracter
            self.columna += 1
            self.estado = "color1"
        else:
            self.comprobar()
    def color1(self, caracter):
        if caracter != "]":
            self.buffer += caracter
            self.columna += 1
        else:
            if self.bool == True:
                self.matrix.setElementByCoordinate(self.x,self.y,self.buffer)
            self.x = None
            self.y = None
            self.bool = None
            self.agregar_token(self.buffer, 'color', self.linea, self.columna)
            self.estado = "body4"
            self.i -= 1
    def body4(self, caracter):
        if caracter == "]":
            self.buffer += caracter
            self.agregar_token(self.buffer, 'cerradura S', self.linea, self.columna)
            self.columna += 1
        elif caracter == ",":
            self.i -= 1
            self.estado = "coma"
            self.anterior = "body4"
        elif caracter  == "}":
            self.i -= 1
            self.estado = "body5"
        elif caracter == "[":
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.i -= 1
            self.estado = "body1"
        else:
            self.comprobar(caracter)
    def body5(self, caracter):
        if caracter == "}":
            self.buffer += caracter
            self.agregar_token(self.buffer, 'cerradura P', self.linea, self.columna)
            self.estado = "puntocoma"
            self.anterior = "body5"
        else:
            self.comprobar(caracter)

    def filtros0(self, caracter):
        if caracter == "F":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filtros1"
        else:
            self.comprobar(caracter)
    def filtros1(self, caracter):
        if caracter == "I":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filtros2"
        else:
            self.comprobar(caracter)
    def filtros2(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filtros3"
        else:
            self.comprobar(caracter)
    def filtros3(self, caracter):
        if caracter == "T":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filtros4"
        else:
            self.comprobar(caracter)
    def filtros4(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filtros5"
        else:
            self.comprobar(caracter)
    def filtros5(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.columna += 1
            self.estado = "filtros6"
        else:
            self.comprobar(caracter)
    def filtros6(self, caracter):
        if caracter == "S":
            self.buffer += caracter
            self.agregar_token(self.buffer, 'filtros', self.linea, self.columna)
            self.columna += 1
            self.estado = "igual"
            self.anterior = "filtros6"
        else:
            self.comprobar(caracter)

    def mirror0(self, caracter):
        if caracter == "M":
            self.buffer += caracter
            self.columna += 1
            self.estado = "mirror1"
        elif caracter == "D":
            self.i -= 1
            self.estado = "double0"
        elif caracter == ";":
            self.i -= 1
            self.estado = "puntocoma"
            self.anterior = "filter"
        else:
            self.comprobar(caracter)
    def mirror1(self, caracter):
        if caracter == "I":
            self.buffer += caracter
            self.columna += 1
            self.estado = "mirror2"
        else:
            self.comprobar(caracter)
    def mirror2(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna += 1
            self.estado = "mirror3"
        else:
            self.comprobar(caracter)
    def mirror3(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna += 1
            self.estado = "mirror4"
        else:
            self.comprobar(caracter)
    def mirror4(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.columna += 1
            self.estado = "mirror5"
        else:
            self.comprobar(caracter)
    def mirror5(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna += 1
        elif caracter == "X":
            self.estado = "mirrorx"
            self.i -= 1
        elif caracter == "Y":
            self.estado = "mirrory"
            self.i -= 1
        else:
            self.comprobar(caracter)
    def mirrorx(self, caracter):
        if caracter == "X":
            self.buffer += caracter
            self.matrix.setFiltros(self.buffer)
            self.agregar_token(self.buffer,'espejo x', self.linea, self.columna)
            self.columna += 1
        elif caracter == ",":
            self.i-=1
            self.estado = "coma"
            self.anterior = "filter"
        elif caracter == ";":
            self.i -= 1
            self.estado = "puntocoma"
            self.anterior = "filter"
        else:
            self.comprobar(caracter)
    def mirrory(self, caracter):
        if caracter == "Y":
            self.buffer += caracter
            self.matrix.setFiltros(self.buffer)
            self.agregar_token(self.buffer,'espejo y', self.linea, self.columna)
            self.columna += 1
        elif caracter == ",":
            self.i-=1
            self.estado = "coma"
            self.anterior = "filter"
        elif caracter == ";":
            self.i -= 1
            self.estado = "puntocoma"
            self.anterior = "filter"
        else:
            self.comprobar(caracter)
    def double0(self, caracter):
        if caracter == "D":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double1"
        else:
            self.comprobar(caracter)
    def double1(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double2"
        else:
            self.comprobar(caracter)
    def double2(self, caracter):
        if caracter == "U":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double3"
        else:
            self.comprobar(caracter)
    def double3(self, caracter):
        if caracter == "B":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double4"
        else:
            self.comprobar(caracter)
    def double4(self, caracter):
        if caracter == "L":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double5"
        else:
            self.comprobar(caracter)
    def double5(self, caracter):
        if caracter == "E":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double6"
        else:
            self.comprobar(caracter)
    def double6(self, caracter):
        if caracter == "M":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double7"
        else:
            self.comprobar(caracter)
    def double7(self, caracter):
        if caracter == "I":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double8"
        else:
            self.comprobar(caracter)
    def double8(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double9"
        else:
            self.comprobar(caracter)
    def double9(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double10"
        else:
            self.comprobar(caracter)
    def double10(self, caracter):
        if caracter == "O":
            self.buffer += caracter
            self.columna +=1
            self.estado = "double11"
        else:
            self.comprobar(caracter)
    def double11(self, caracter):
        if caracter == "R":
            self.buffer += caracter
            self.matrix.setFiltros(self.buffer)
            self.agregar_token(self.buffer, 'espejo D', self.linea, self.columna)
            self.columna +=1
        elif caracter == ",":
            self.i-=1
            self.estado = "coma"
            self.anterior = "filter"
        elif caracter == ";":
            self.i -= 1
            self.estado = "puntocoma"
            self.anterior = "filter"
        else:
            self.comprobar(caracter)

    def espacio(self, caracter):
        if caracter != "@":
            self.comprobar(caracter)
        else:
            self.i -= 1
            self.estado = "arrobas"

    def arroba(self, caracter):
        if caracter == "@":
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(self.buffer, 'arrobas', self.linea, self.columna)
            self.i -= 1
            self.estado = "titulo0"

    def coma(self, caracter):
        if caracter == ",":
            self.buffer += caracter
            self.agregar_token(self.buffer, 'coma', self.linea, self.columna)
            self.columna += 1
            if self.anterior == "body2":
                self.estado = "body3"
            elif self.anterior == "body3":
                self.estado = "true0"
            elif self.anterior == "true3" or self.anterior == "false4":
                self.estado = "color0"
            elif self.anterior == "filter":
                self.estado = "mirror0"
            elif self.anterior == "body4":
                self.estado = "body1"
        elif caracter == "]" and self.anterior == "body4":
            self.buffer += caracter
            self.agregar_error(self.buffer, self.linea, self.columna)
            self.buffer = ''
            self.columna += 1
            self.i -= 1
            self.estado = "body1"
        else:
            self.comprobar(caracter)
    
    def comprobar(self, caracter):
        if caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            if caracter == "\t":
                self.columna += 4
            else:
                self.columna += 1      
        elif caracter == '\r':
            pass
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1 

    def getMapas(self):
        return self.listaMatrices

    def reporteErrores(self):
        re = """
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset='utf-8'>
                <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                <title>REPORTE DE ERRORES</title>
                <meta name='viewport' content='width=device-width, initial-scale=1'>
                <link rel='stylesheet' type='text/css' media='screen' href='reporte.css'>
            </head>
        <body>
        <h1>REPORTE DE ERRORES<h1>\n
        """
        if len(self.listaErrores) == 0:
            re += "<h3>No se detectaron errores</h3>\n"
        else:       
            re += """
            <table>
            <thead>
                <tr><th>&nbsp;&nbsp;&nbsp;&nbsp;Caracter&nbsp;&nbsp;</th><th>&nbsp;&nbsp;Fila&nbsp;&nbsp;</th><th>&nbsp;&nbsp;Columna&nbsp;&nbsp;</th></tr>\n
            </thead>
            <tbody>
            """
            for i in range(len(self.listaErrores)):
                re += "\t<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(
                    self.listaErrores[i].descripcion,
                    self.listaErrores[i].linea,
                    self.listaErrores[i].columna)
            re += "\n\t</tbody>\n</table>"
        re+= """
        </body>
        </html>
        """
        return re
    
    def reporteTokens(self):
        re = """
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset='utf-8'>
                <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                <title>REPORTE DE TOKENS</title>
                <meta name='viewport' content='width=device-width, initial-scale=1'>
                <link rel='stylesheet' type='text/css' media='screen' href='reporte.css'>
            </head>
        <body>
            <h1>REPORTE DE TOKENS</h1>
            <table>
                </thead>
                <tr><th>&nbsp;&nbsp;LEXEMA&nbsp;&nbsp;</th><th>&nbsp;&nbsp;TOKEN&nbsp;&nbsp;</th><th>&nbsp;&nbsp;LINEA&nbsp;&nbsp;</th><th>&nbsp;&nbsp;COLUMNA&nbsp;&nbsp;</th></tr>\n
                </thead>
            <tbody>
        """
        for i in range(len(self.listaTokens)):
            re += "\t\t<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(
                    self.listaTokens[i].lexema,
                    self.listaTokens[i].tipo,
                    self.listaTokens[i].linea,
                    self.listaTokens[i].columna)
        re += """
                </tbody>
                </table>
            </body>
            </html>
        """
        return re
