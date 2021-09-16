import os
import tkinter as tk
import webbrowser
from tkinter import messagebox as MB
from tkinter import ttk
from tkinter.constants import NW

from automata.analyzer import Analyzer
from matrix.matrix import MatrizV
from metodos.metodos import openFile


class Main:
    def __init__(self):
        self.reporteErrores = ""
        self.reporteTokens = ""
        self.mapas = []
        self.nombres = []
        self.mirrx = True#valore por defecto
        self.mirry = True
        self.mirrd = True
        self.ancho = 600
        self.alto = 600#medida por defecto
        self.ventana=tk.Tk()
        self.ventana.configure(bg = "#383838")
        x_ = self.ventana.winfo_screenwidth()//2-835//2
        y_ = self.ventana.winfo_screenheight()//2-830//2
        self.ventana.geometry("860x780+{}+{}".format(x_,y_)) 
        self.menuleft()
        self.menuup()
        codigos = [
            ["#000000","#FFFFFF","#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000"], 
            ["#FFFFFF","#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000"], 
            ["#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080"], 
            ["#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080"], 
            ["#0000FF","#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080","#000080"], 
            ["#FFFF00","#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080","#000080","#EE82EE"], 
            ["#00FFFF","#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080","#000080","#EE82EE","#F5DEB3"], 
            ["#FF00FF","#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080","#000080","#EE82EE","#F5DEB3","#4682B4"], 
            ["#C0C0C0","#808080","#800000","#808000","#008000","#800080","#008080","#000080","#EE82EE","#F5DEB3","#4682B4","#87CEEB"], 
            ["#808080","#800000","#808000","#008000","#800080","#008080","#000080","#EE82EE","#F5DEB3","#4682B4","#87CEEB","#A0522D"],
            ["#800000","#808000","#008000","#800080","#008080","#000080","#EE82EE","#F5DEB3","#4682B4","#87CEEB","#A0522D","#2E8B57"],
            ["#808000","#008000","#800080","#008080","#000080","#EE82EE","#F5DEB3","#4682B4","#87CEEB","#A0522D","#2E8B57","#4169E1"]
        ]
        self.matrizColores = MatrizV()
        self.matrizColores.dimensionar(12,12)
        for i in range(12):
            for j in range(12):
                self.matrizColores.setElementByCoordinate(i,j,codigos[i][j])

        self.canvas=tk.Canvas(self.menuI, width=self.ancho, height=self.alto, background="aliceblue")
        self.canvas.grid(row = 0, column = 1, padx=20, pady = 25)
        
        self.ventana.iconbitmap("ico.ico")
        self.ventana.title("BITXELART v.1.0")
        self.ventana.mainloop()

    def menuup(self):
        self.style = ttk.Style().configure('TLabelframe', background = "#383838", fg = "#FFC93C")
        self.menuu = ttk.LabelFrame(self.ventana, text = "OPCIONES")
        self.menuu.grid(column = 0, row = 0, sticky="N", pady = 15)

        self.texto = None

        self.cargar = ttk.Button(self.menuu, text = "Cargar", command = self.Cargar)
        self.cargar.grid(row = 0, column = 0, padx = 8, pady = 5)
        self.analizar = ttk.Button(self.menuu, text = "Analizar", command = self.Analizar)
        self.analizar.grid(row = 0, column = 1, padx = 8, pady = 5)
        self.reporte = ttk.Button(self.menuu, text = "Reporte", command = self.Reportes)
        self.reporte.grid(row = 0, column = 2, padx = 8, pady = 5)
        ttk.Button(self.menuu, text = "Salir", command = exit).grid(row = 0, column = 3, padx = 8, pady = 5)

    def Cargar(self):
        self.texto = openFile()

    def Reportes(self):
        if self.reporteErrores == "":
            MB.showerror("Error...", "Previamente no se ha analizado ningun archivo")
        else:
            reporte = open("Reporte de Errores.html","w")
            reporte.write(self.reporteErrores)
            reporte2 = open("Reporte de Tokens.html","w")
            reporte2.write(self.reporteTokens)
            webbrowser.open_new_tab('Reporte de Errores.html')
            webbrowser.open_new_tab('Reporte de Tokens.html')
            
    def Analizar(self):
        if self.texto != None:
            scanner = Analyzer()
            scanner.analizar(self.texto)
            self.reporteErrores += scanner.reporteErrores()
            self.reporteTokens += scanner.reporteTokens()
            self.mapas += scanner.getMapas()
            self.nombres = []
            for mapa in self.mapas:
                self.nombres.append(mapa.getNombre())
            ###
            self.imagenes['values'] = self.nombres
            ###
            self.generateImg()
        else:
            MB.showerror("ERROR","NO se ha cargado un archivo previamente")

    def menuleft(self):
        self.menuI=ttk.LabelFrame(self.ventana,text="IMAGENES Y OPCIONES DE DISEÑO")
        self.menuI.grid(row = 1, column = 0, sticky="W", pady = 10, padx = 10)

        self.subI = tk.Canvas(self.menuI, background = "#383838")
        self.subI.grid(row = 0, column = 0, sticky = "NW", pady = 15, padx = 10)
        ### Combobox para seleccionar Imagenes
        self.lf1 = ttk.LabelFrame(self.subI, text = "SELECCIONE LA IMAGEN")
        self.lf1.grid(row = 0, column = 0, sticky = "NW", pady = 15, padx = 10)
        self.imagenes = ttk.Combobox(self.lf1,state = "readonly")
        self.imagenes.bind("<<ComboboxSelected>>", self.selectImage)
        self.imagenes.grid(row = 0, column = 0)
        ### Combobox para seleccionar Filtros
        self.lf = ttk.LabelFrame(self.subI, text = "SELECCIONE EL DISEÑO")
        self.lf.grid(row = 1, column = 0, sticky = "NW", pady = 15, padx = 10)
        self.opciones = ttk.Combobox(self.lf, values = [
            "Original",
            "Mirror X",
            "Mirror Y",
            "Double Mirror"
        ], state = 'readonly')
        self.opciones.bind("<<ComboboxSelected>>", self.selectOption)
        self.opciones.grid(row = 0, column = 0)
        self.opciones.current(0)
    
    def selectOption(self, event):
        if self.opciones.get() == "Original":
            self.graphic(1)
        elif self.opciones.get() == "Mirror X":
            self.graphic(2)
        elif self.opciones.get() == "Mirror Y":
            self.graphic(3)
        elif self.opciones.get() == "Double Mirror":
            self.graphic(4)
    
    def selectImage(self, event):
        selected = self.imagenes.get()
        for i in range(len(self.nombres)):
            if self.nombres[i] == selected:
                self.matrizColores = self.mapas[i]
                self.alto = self.mapas[i].getAlto()
                self.ancho = self.mapas[i].getAncho()
                filtros = self.mapas[i].getFiltros()
                self.mirrx = False
                self.mirry = False
                self.mirrd = False
                for filtro in filtros:
                    if filtro == "MIRRORX":
                        self.mirrx = True
                    if filtro == "MIRRORY":
                        self.mirry = True
                    if filtro == "DOUBLEMIRROR":
                        self.mirrd = True
                self.canvas.delete(tk.ALL)
                self.canvas.configure(width = self.ancho, height = self.alto)
                i = len(self.nombres)

    def graphic(self, order):
        self.canvas.delete(tk.ALL)
        fila = self.matrizColores.getDimensionFila()
        columna = self.matrizColores.getDimensionColumna()
        fil = self.alto//fila
        col = self.ancho//columna

        if order == 1:
            self.canvas.delete(tk.ALL)
            self.printCanvas(self.matrizColores,fil,col)
        elif order == 2:
            self.canvas.delete(tk.ALL)
            if self.mirrx == True:
                m2 = self.mix(self.matrizColores,fila,columna)
                self.printCanvas(m2,fil,col)
            else:
                self.canvas.create_text(100,10, text = "Filtro no disponible para esta imagen")
        elif order == 3:
            self.canvas.delete(tk.ALL)
            if self.mirry == True:
                m3 = self.miy(self.matrizColores,fila,columna)
                self.printCanvas(m3,fil,col)
            else:
                self.canvas.create_text(100,10, text = "Filtro no disponible para esta imagen")
        elif order == 4:
            self.canvas.delete(tk.ALL)
            if self.mirrd == True:
                m4 = self.dou(self.matrizColores,fila,columna)
                self.printCanvas(m4,fil,col)
            else:
                self.canvas.create_text(100,10, text = "Filtro no disponible para esta imagen")
        self.canvas.update()

    def miy(self, matrix, fila, columna):
        aux = matrix
        aux2 = MatrizV()
        aux2.dimensionar(fila,columna)
        for i in range(fila):
            for j,jj in zip(range(columna),range(columna-1,-1,-1)):
                aux2.setElementByCoordinate(i,j,aux.getElementByCoordinate(i,jj))
        return aux2
    
    def mix(self, matrix, fila, columna):
        aux = matrix
        aux2 = MatrizV()
        aux2.dimensionar(fila,columna)
        for i ,ii in zip(range(fila),range(fila-1,-1,-1)):
            for j in range(aux.getDimensionColumna()):
                aux2.setElementByCoordinate(i,j,aux.getElementByCoordinate(ii,j))
        return aux2
        
    def dou(self, matrix, fila, columna):
        aux = matrix
        aux2 = MatrizV()
        aux2.dimensionar(fila, columna)
        for i,ii in zip(range(fila),range(fila-1,-1,-1)):
            for j,jj in zip(range(columna),range(columna-1,-1,-1)):
                aux2.setElementByCoordinate(i,j,aux.getElementByCoordinate(ii,jj))
        return aux2

    def printCanvas(self, matrix,fil,col):
        for i in range(matrix.getDimensionFila()):
            for j in range(matrix.getDimensionColumna()):
                self.canvas.create_rectangle(fil*i,col*j,fil*(i+1),col*(j+1), fill=matrix.getElementByCoordinate(i,j))
        
    def generateImg(self):
        for mapa in self.mapas:
            alto = mapa.getAlto()
            ancho = mapa.getAncho()
            fila = mapa.getDimensionFila()
            columna = mapa.getDimensionColumna()
            fil = self.alto//fila
            col = self.ancho//columna
            
            if os.path.exists("{}_origin.html".format(mapa.nombre)):
                    pass
            else:
                    html = """
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset='utf-8'>
                            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                            <title>{}</title>
                            <meta name='viewport' content='width=device-width, initial-scale=1'>
                            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
                        </head>
                    <body>
                    <h1>{}<br>FILAS: {} &nbsp; &nbsp; COLUMNAS: {}<br>WIDTH: {} &nbsp; &nbsp; HEIGHT: {}<br>FILTRO: ORIGINAL<h1>\n
                    <table>
                    """.format(mapa.nombre,mapa.nombre,fila,columna,ancho,alto)
                    for i in range(fila):
                        html += "\n<tr>"
                        for j in range(columna):
                            html += """<td WIDTH = "{}" HEIGHT = "{}" style = "background-color: {};"></td>""".format(fil,col,mapa.getElementByCoordinate(j,i))
                        html += "</tr>"
                    html += "\n</table>\n</body>\n</html>"
                    file = open("{}_origin.html".format(mapa.nombre),"w")
                    file.write(html)
                    webbrowser.open_new_tab("{}_origin.html".format(mapa.nombre))
            if "MIRRORX" in mapa.filtros:
                if os.path.exists("{}_mirrorx.html".format(mapa.nombre)):
                    pass
                else:
                    html = """
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset='utf-8'>
                            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                            <title>{}</title>
                            <meta name='viewport' content='width=device-width, initial-scale=1'>
                            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
                        </head>
                    <body>
                    <h1>{}<br>FILAS: {} &nbsp; &nbsp; COLUMNAS: {}<br>WIDTH: {} &nbsp; &nbsp; HEIGHT: {}<br>FILTRO: MIRRORX<h1>\n
                    <table>
                    """.format(mapa.nombre,mapa.nombre,fila,columna,ancho,alto)
                    m = self.mix(mapa, fila, columna)
                    for i in range(fila):
                        html += "\n<tr>"
                        for j in range(columna):
                            html += """<td WIDTH = "{}" HEIGHT = "{}" style = "background-color: {};"></td>""".format(fil,col,m.getElementByCoordinate(j,i))
                        html += "</tr>"
                    html += "\n</table>\n</body>\n</html>"
                    file = open("{}_mirrorx.html".format(mapa.nombre),"w")
                    file.write(html)
                    webbrowser.open_new_tab("{}_mirrorx.html".format(mapa.nombre))                
            if "MIRRORY" in mapa.filtros:
                if os.path.exists("{}_mirrory.html".format(mapa.nombre)):
                    pass
                else:
                    html = """
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset='utf-8'>
                            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                            <title>{}</title>
                            <meta name='viewport' content='width=device-width, initial-scale=1'>
                            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
                        </head>
                    <body>
                    <h1>{}<br>FILAS: {} &nbsp; &nbsp; COLUMNAS: {}<br>WIDTH: {} &nbsp; &nbsp; HEIGHT: {}<br>FILTRO: MIRRORY<h1>\n
                    <table>
                    """.format(mapa.nombre,mapa.nombre,fila,columna,ancho,alto)
                    m = self.miy(mapa, fila, columna)
                    for i in range(fila):
                        html += "\n<tr>"
                        for j in range(columna):
                            html += """<td WIDTH = "{}" HEIGHT = "{}" style = "background-color: {};"></td>""".format(fil,col,m.getElementByCoordinate(j,i))
                        html += "</tr>"
                    html += "\n</table>\n</body>\n</html>"
                    file = open("{}_mirrory.html".format(mapa.nombre),"w")
                    file.write(html)
                    webbrowser.open_new_tab("{}_mirrory.html".format(mapa.nombre))
            if "DOUBLEMIRROR" in mapa.filtros:
                if os.path.exists("{}_doublemirror.html".format(mapa.nombre)):
                    pass
                else:
                    html = """
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset='utf-8'>
                            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                            <title>{}</title>
                            <meta name='viewport' content='width=device-width, initial-scale=1'>
                            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
                        </head>
                    <body>
                    <h1>{}<br>FILAS: {} &nbsp; &nbsp; COLUMNAS: {}<br>WIDTH: {} &nbsp; &nbsp; HEIGHT: {}<br>FILTRO: DOUBLEMIRROR<h1>\n
                    <table>
                    """.format(mapa.nombre,mapa.nombre,fila,columna,ancho,alto)
                    m = self.mid(mapa, fila, columna)
                    for i in range(fila):
                        html += "\n<tr>"
                        for j in range(columna):
                            html += """<td WIDTH = "{}" HEIGHT = "{}" style = "background-color: {};"></td>""".format(fil,col,m.getElementByCoordinate(j,i))
                        html += "</tr>"
                    html += "\n</table>\n</body>\n</html>"
                    file = open("{}_doublemirror.html".format(mapa.nombre),"w")
                    file.write(html)
                    webbrowser.open_new_tab("{}_doublemirror.html".format(mapa.nombre))
inicio = Main()
