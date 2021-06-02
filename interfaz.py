#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

#INTERFAZ GRÁFICA
#importaciones
from tkinter import Tk,Label,Button,Entry, Frame
from typing import Collection

class Menu(Frame):#hereda de la clase Frame.

    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def crearXML(self):#1
        print("Crear XML")

    def crearlicencia(self):#2
        print("Crear licencia")
    
    def renovar(self):#3
        print("Renovar")

    def generarPDF(self):#4
        print("Generar PDF")

    def reportesExcel(self):#5
        print("Reportes Execel")
    
    def acerca(self):#6
        print("Acerca de...")
    def salir(self):
        print("Salir")

    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Crear XML",width=100,height=3,bg="grey",command=self.crearXML)
        self.btnCrearLicencia=Button(self,text="Crear Licencia",width=100,height=3,bg="grey",command=self.crearlicencia)
        self.btnRenovarLicencia=Button(self,text="Renovar licencia",width=100,height=3,bg="grey",command=self.renovar)
        self.btnGenerarPDF=Button(self,text="Generar PDF",width=100,height=3,bg="grey",command=self.generarPDF)
        self.btnReporteExcel=Button(self,text="Reporte Excel",width=100,height=3,bg="grey",command=self.reportesExcel)
        self.btnAcerca=Button(self,text="Acerca",width=100,height=3,bg="grey",command=self.acerca)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="grey",command=self.salir)

        #Lugar ubicación
        self.btnCrearXML.grid(row=0,column=1,padx=10,pady=10)
        self.btnCrearLicencia.grid(row=1,column=1,padx=10,pady=10)
        self.btnRenovarLicencia.grid(row=2,column=1,padx=10,pady=10)
        self.btnGenerarPDF.grid(row=3,column=1,padx=10,pady=10)
        self.btnReporteExcel.grid(row=4,column=1,padx=10,pady=10)
        self.btnAcerca.grid(row=5,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)

root = Tk()
root.wm_title("Reporte de conductores")#titulo de la ventana
app = Menu(root) 
app.mainloop()