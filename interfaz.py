#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

#INTERFAZ GRÁFICA
#importaciones
from tkinter import *
from typing import Collection
from tkinter import messagebox
from importarInformacionHTML import *
from xml import *
from funciones import *
import sys
class Menu(Frame):#hereda de la clase Frame.

    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets() 

    def XML(self):#1
        print("Crear XML")
        crearListaInformacion()#NUEVO
        crearXML()#NO ESTÄ SIRVIENDO LA LLAMADA, aunque si crea el archivo.
        messagebox.showinfo("XML creado","Reporte XML creado con éxito.")

    def crearlicencia(self):#2
        root = Tk()
        root.wm_title("Crear licencias")
        crearVentanaLicencias=CreaLicencia(root)
        crearVentanaLicencias.mainloop()
        print("Crear licencia")

    
    def renovar(self):#3
        print("Renovar")

    def generarPDF(self):#4
        print("Generar PDF")

    def reportesExcel(self):#5
        print("Reportes Execel")
        root = Tk()#crea la ventana nueva para el submenu de reportes.
        root.wm_title("Reporte de conductores")#titulo de la ventana
        app = SubMenu(root) 
        app.mainloop()
    
    def acerca(self):#6
        print("Acerca de...")
    def salir(self):
        messagebox.showinfo("Información", "No olvides gestionar pronto tu licencia.")#muestra una ventana
        sys.exit()#Cierra la ventana

    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Crear XML",width=100,height=3,bg="grey",command=self.XML)
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
class SubMenu(Frame):#TODO NUEVo
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Totalidad de licencias",width=100,height=3,bg="grey")
        self.btnCrearLicencia=Button(self,text="Por tipo de licencia",width=100,height=3,bg="grey")
        self.btnRenovarLicencia=Button(self,text="Examen por sanción",width=100,height=3,bg="grey")
        self.btnGenerarPDF=Button(self,text="Los donantes de órganos",width=100,height=3,bg="grey")
        self.btnReporteExcel=Button(self,text="Licencia anulada",width=100,height=3,bg="grey")
        self.btnAcerca=Button(self,text="Licencias por sede",width=100,height=3,bg="grey")
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="grey",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.btnCrearXML.grid(row=0,column=1,padx=10,pady=10)
        self.btnCrearLicencia.grid(row=1,column=1,padx=10,pady=10)
        self.btnRenovarLicencia.grid(row=2,column=1,padx=10,pady=10)
        self.btnGenerarPDF.grid(row=3,column=1,padx=10,pady=10)
        self.btnReporteExcel.grid(row=4,column=1,padx=10,pady=10)
        self.btnAcerca.grid(row=5,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)
class CreaLicencia(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def enviarCantidadCreacion(self):
        #aquí sacamos el entry y mandamos a crear si es válido.
        cantidad=self.entryCantidad.get()
        if validarNumeroIngresado(cantidad):
            generarLicencias(int(cantidad))
            messagebox.showinfo("Se han creado licencias", "Licencias creadas de manera correcta")
        else:
            messagebox.showerror("Intente de nuevo", "Ha habido un error, intente de nuevo")
    def create_widgets(self):#crea los botones y etiquetas.
        self.lblLicencia=Label(self,text="Crear licencias")
        self.lblCantidad=Label(self,text="¿A cuántas personas desea crear licencia?")
        self.entryCantidad=Entry(self)
        self.btnCantidad=Button(self,text="Generar",width=50,height=3,command=self.enviarCantidadCreacion)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="grey",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
        self.lblLicencia.grid(row=0,column=1,padx=10,pady=10)
        self.lblCantidad.grid(row=1,column=1,padx=10,pady=10)
        self.entryCantidad.grid(row=2,column=1,padx=10,pady=10)
        self.btnCantidad.grid(row=3,column=1,padx=10,pady=10)

        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)
root = Tk()
root.wm_title("Reporte de conductores")#titulo de la ventana
app = Menu(root) 
app.config(cursor='pirate')
app.mainloop()