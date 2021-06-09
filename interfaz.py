#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

#INTERFAZ GRÁFICA
#importaciones
from os import waitpid
from tkinter import *
from typing import Collection
from tkinter import messagebox
from tkinter import ttk
from importarInformacionHTML import *
from crearReportesExcel import *
from xmlCreador import *
from funciones import *
import sys
class Menu(Frame):#hereda de la clase Frame.

    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets() 

    def XML(self):#1
        crearListaInformacion()#NUEVO
        crearXML()
        messagebox.showinfo("XML creado","Reporte XML creado con éxito.")

    def crearlicencia(self):#2
        root = Tk()
        root.wm_title("Crear licencias")
        crearVentanaLicencias=CreaLicencia(root)
        crearVentanaLicencias.mainloop()

    def renovar(self):#3
        root = Tk()
        root.wm_title("Renovar licencias")
        crearVentanaRenovar=RenovarLicencia(root)
        crearVentanaRenovar.mainloop()

    def generarPDF(self):#4
        root = Tk()
        root.wm_title("Generar Reporte PDF")
        crearVentanaPDF=CreaPDF(root)
        crearVentanaPDF.mainloop()

    def reportesExcel(self):#5
        root = Tk()#crea la ventana nueva para el submenu de reportes.
        root.wm_title("Reporte de conductores")#titulo de la ventana
        app = SubMenuExcel(root) 
        app.mainloop()
    
    def acerca(self):#6
        messagebox.showinfo("Autores","Pura machine en este código")
        root=Tk()
        root.wm_title("Acerca de nosotros")
        crearVentanaAcerca=Nosotros(root)
        crearVentanaAcerca.mainloop()
    
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

class CreaLicencia(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def enviarCantidadCreacion(self):
        #aquí sacamos el entry y mandamos a crear si es válido.
        cantidad=self.entryCantidad.get()#trae el entry.
        if validarNumeroIngresado(cantidad):#archivo funciones.py
            generarLicencias(int(cantidad))
            messagebox.showinfo("Se han creado licencias", "Se han creado "+cantidad+" licencias.")
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

class RenovarLicencia(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def renovacion(self):
        cedula=self.entryLicencia.get()#trae el entry.
        retorna=validarLicencia(cedula)
        print("Está retornando",retorna)
        if retorna==1:#puntaje entre 1-6
            messagebox.showerror("Ha habido un error","Debido a su puntaje, debe realizar el examen otra vez.")
        elif retorna==2:#puntaje 0
            messagebox.showerror("Ha habido un error","Licencia retirada permanentemente.")
        elif retorna==3:#puntaje mayor a 6
            messagebox.showinfo("Licencia renovada","Se ha renovado la licencia correctamente.")
        elif retorna==4:#formato incorrecto
            messagebox.showerror("Ha habido un error","La cédula ingresada no tiene el formato correcto")
        elif retorna==5:#cédula no registrada
            messagebox.showerror("Ha habido un error","La cédula ingresada no se cuentra registrada")
        self.clear_text()#limpia el entry
        return

    def clear_text(self):#limpa entry de cédula
        self.entryLicencia.delete(0, 'end')#borra el contenido del entry.

    def create_widgets(self):#crea los botones y etiquetas.
        self.lblRenovar=Label(self,text="Renovar licencias")
        self.lblIngresar=Label(self,text="Ingresar cédula")
        self.entryLicencia=Entry(self)
        self.btnRenovar=Button(self,text="Renovar",width=25,height=3,command=self.renovacion)
        self.btnLimpiar=Button(self,text="Limpiar",width=25,height=3,command=self.clear_text)
        self.btnSalir=Button(self,text="Regresar",width=100,height=3,bg="grey",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
        self.lblRenovar.grid(row=0,column=1,padx=10,pady=10)
        self.lblIngresar.grid(row=1,column=1,padx=10,pady=10)
        self.entryLicencia.grid(row=2,column=1,padx=10,pady=10)
        self.btnRenovar.grid(row=3,column=1,padx=10,pady=10)
        self.btnLimpiar.grid(row=4,column=1,padx=10,pady=10)

        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)

class CreaPDF(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def enviarPDF(self):
        if licenciaPDF(self.entryCedulaPDF.get()):
            messagebox.showinfo("Reporte Generado","PDF creado con éxito")
            self.entryCedulaPDF.delete(0, 'end')
        else:
            messagebox.showerror("Error","Ingresó una cédula inexistente, intente de nuevo")

    def create_widgets(self):#crea los botones y etiquetas.
        self.lblLicencia=Label(self,text="Reporte PDF de licencias")
        self.lblCantidad=Label(self,text="Ingrese la cédula de la persona a la que desea generar el PDF")
        self.entryCedulaPDF=Entry(self,bd=5)
        self.btnCantidad=Button(self,text="Generar Reporte",width=50,height=3,command=self.enviarPDF)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="grey",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
        self.lblLicencia.grid(row=0,column=1,padx=10,pady=10)
        self.lblCantidad.grid(row=1,column=1,padx=10,pady=10)
        self.entryCedulaPDF.grid(row=2,column=1,padx=10,pady=10)
        self.btnCantidad.grid(row=3,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)

class SubMenuExcel(Frame):#Reportes excel
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def enviarTotalReporte(self):
        if reporteTotalidadLicencias():
            messagebox.showinfo("Reporte creado","Se ha creado el reporte.")
        else:
            messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
    def enviarTipoLicenciaReporte(self):
        root = Tk()#crea la ventana nueva para el submenu de reportes.
        root.wm_title("Reporte por tipo de licencia")#titulo de la ventana
        app = SubMenuTipoLicencia(root) 
        app.mainloop()
        pass
    def enviarExamenPorSancionReporte(self):
        if reporteExamenSancion():
            messagebox.showinfo("Reporte creado","Se ha creado el reporte.")
        else:
            messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Totalidad de licencias",width=100,height=3,bg="grey",command=self.enviarTotalReporte)
        self.btnCrearLicencia=Button(self,text="Por tipo de licencia",width=100,height=3,bg="grey",command=self.enviarTipoLicenciaReporte)
        self.btnRenovarLicencia=Button(self,text="Examen por sanción",width=100,height=3,bg="grey",command=self.enviarExamenPorSancionReporte)
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

class SubMenuTipoLicencia(Frame):#se cambiaron las opciones
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()
    def crearReportePorTipoLicencia(self):
        opciones=["Licencias de conducir tipo A (motocicletas)","Licencias de conducir tipo B (automóviles y camiones)",
        "Licencias de conducción tipo C (autobús y taxi)","Licencias de conducir tipo D (tractores y maquinaria)",
        "Licencias tipo E (universales)"]
        if not self.opciones.get() in opciones:
            messagebox.showerror("Ha ocurrido un error","Debe seleccionar una opción de la caja de opciones.")
            self.opciones.delete(0,"end")
        else:
            if reporteTipoLicencia(self.opciones.get()):#crarReporetesExcel.py
                messagebox.showinfo("Reporte generado","Se ha generado el reporte.")
                self.opciones.delete(0,"end")
            else:
                messagebox.showerror("Ha ocurrido un error","Ha ocurrido un error, debe cerrar el archivo.")
        return
    def create_widgets(self):#crea los botones y etiquetas.
        self.lblTipo=Label(self,text="Tipo de licencia",width=50,height=3)
        self.opciones=ttk.Combobox(self,width=55,height=5)
        self.opciones["values"]=["Licencias de conducir tipo A (motocicletas)","Licencias de conducir tipo B (automóviles y camiones)",
        "Licencias de conducción tipo C (autobús y taxi)","Licencias de conducir tipo D (tractores y maquinaria)",
        "Licencias tipo E (universales)"]

        self.btnGenerar=Button(self,text="Generar reporte",width=50,height=3,bg="grey",command=self.crearReportePorTipoLicencia)

        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="grey",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.lblTipo.grid(row=0,column=1,padx=10,pady=10)
        self.opciones.grid(row=1,column=1,padx=10,pady=10)
        self.btnGenerar.grid(row=2,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)

class Nosotros(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):#crea los botones y etiquetas.
        self.lblNosotros=Label(self,text="Acerca de nosostros",width=50,height=3)
        self.lblFelipe=Label(self,text="Felipe Obando Arrieta",width=100,height=3)
        self.lblHabladaFelipe=Label(self,text="El más guapo del mundo, tiene una tremenda tula jjj,\
 oriundo de Cartago City.",width=100,height=3)
        

        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="grey",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.lblNosotros.grid(row=0,column=1,padx=10,pady=10)
        self.lblFelipe.grid(row=1,column=1,padx=10,pady=10)
        self.lblHabladaFelipe.grid(row=2,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)




root = Tk()
root.wm_title("Reporte de conductores")#titulo de la ventana
app = Menu(root) 
app.config(cursor='pirate')
app.mainloop()