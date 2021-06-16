#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 12/06/2021 10:25 pm
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
        self.btnCrearXML=Button(self,text="Crear XML",width=100,height=3,bg="#49A",command=self.XML)
        self.btnCrearLicencia=Button(self,text="Crear Licencia",width=100,height=3,bg="#49A",command=self.crearlicencia)
        self.btnRenovarLicencia=Button(self,text="Renovar licencia",width=100,height=3,bg="#49A",command=self.renovar)
        self.btnGenerarPDF=Button(self,text="Generar PDF",width=100,height=3,bg="#49A",command=self.generarPDF)
        self.btnReporteExcel=Button(self,text="Reporte Excel",width=100,height=3,bg="#49A",command=self.reportesExcel)
        self.btnAcerca=Button(self,text="Acerca",width=100,height=3,bg="#49A",command=self.acerca)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.salir)

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
            messagebox.showerror("Intente de nuevo", "El valor que ingrese debe ser un numero mayor a 1 y menor a 250")

    def create_widgets(self):#crea los botones y etiquetas.
        self.lblLicencia=Label(self,text="Crear licencias")
        self.lblCantidad=Label(self,text="¿A cuántas personas desea crear licencia?")
        self.entryCantidad=Entry(self)
        self.btnCantidad=Button(self,text="Generar",width=50,height=3,command=self.enviarCantidadCreacion)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
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
        self.btnSalir=Button(self,text="Regresar",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
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
        if licenciaPDF(self.entryCedulaPDF.get())==1:
            messagebox.showinfo("Reporte Generado","PDF creado con éxito")
            self.entryCedulaPDF.delete(0, 'end')
        elif licenciaPDF(self.entryCedulaPDF.get())==2:
            messagebox.showinfo("Reporte no generado","La persona con la cédula que ingresó posee un puntaje menor a 6, por lo que \
no puede obtener su licencia.")
        else:
            messagebox.showerror("Error","Ingresó una cédula inexistente, intente de nuevo")

    def create_widgets(self):#crea los botones y etiquetas.
        self.lblLicencia=Label(self,text="Reporte PDF de licencias")
        self.lblCantidad=Label(self,text="Ingrese la cédula de la persona a la que desea generar el PDF")
        self.entryCedulaPDF=Entry(self,bd=5)
        self.btnCantidad=Button(self,text="Generar Reporte",width=50,height=3,command=self.enviarPDF)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
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
        if reporteTotalidadLicencias()==2:
            messagebox.showinfo("Reporte creado","Se ha creado el reporte.")
        elif reporteTotalidadLicencias()==1:
            messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
        else:
            messagebox.showwarning("No se pudo crear el archivo","No existen personas que cumplan sus parámetros de búsqueda.")
    def enviarTipoLicenciaReporte(self):
        root = Tk()#crea la ventana nueva para el submenu de reportes.
        root.wm_title("Reporte por tipo de licencia")#titulo de la ventana
        app = SubMenuTipoLicencia(root) 
        app.mainloop()
        pass
    def enviarExamenPorSancionReporte(self):
        if reporteExamenSancion()==2:
            messagebox.showinfo("Reporte creado","Se ha creado el reporte.")
        elif reporteExamenSancion()==1:
            messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
        else:
            messagebox.showwarning("No se pudo crear el archivo","No existen personas que cumplan sus parámetros de búsqueda.")
    def enviarDonantesDeOrganos(self):
        if reporteDonanteOrganos()==2:
            messagebox.showinfo("Reporte creado","Se ha creado el reporte.")
        elif reporteDonanteOrganos()==1:
            messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
        else:
            messagebox.showwarning("No se pudo crear el archivo","No existen personas que cumplan sus parámetros de búsqueda.")
    def enviarPersonasAnuladas(self):
        if reporteLicenciaAnulada()==2:
            messagebox.showinfo("Reporte creado","Se ha creado el reporte.")
        elif reporteLicenciaAnulada()==1:
            messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
        else:
            messagebox.showwarning("No se pudo crear el archivo","No existen personas que cumplan sus parámetros de búsqueda.")
    def enviarPersonasPorSede(self):
        root = Tk()#crea la ventana nueva para el submenu de reportes.
        root.wm_title("Reporte por Sede")#titulo de la ventana
        app = SubMenuSede(root) 
        app.mainloop()
        pass
    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Totalidad de licencias",width=100,height=3,bg="#49A",command=self.enviarTotalReporte)
        self.btnCrearLicencia=Button(self,text="Por tipo de licencia",width=100,height=3,bg="#49A",command=self.enviarTipoLicenciaReporte)
        self.btnRenovarLicencia=Button(self,text="Examen por sanción",width=100,height=3,bg="#49A",command=self.enviarExamenPorSancionReporte)
        self.btnGenerarPDF=Button(self,text="Los donantes de órganos",width=100,height=3,bg="#49A",command=self.enviarDonantesDeOrganos)
        self.btnReporteExcel=Button(self,text="Personas Anuladas",width=100,height=3,bg="#49A",command=self.enviarPersonasAnuladas)
        self.btnAcerca=Button(self,text="Licencias por sede",width=100,height=3,bg="#49A",command=self.enviarPersonasPorSede)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
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
            if reporteTipoLicencia(self.opciones.get())==2:#crarReporetesExcel.py
                messagebox.showinfo("Reporte generado","Se ha generado el reporte.")
                self.opciones.delete(0,"end")
            elif reporteTipoLicencia(self.opciones.get())==1:
                messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
            else:
                messagebox.showwarning("No se pudo crear el archivo","No existen personas que cumplan sus parámetros de búsqueda.")
        return
    def create_widgets(self):#crea los botones y etiquetas.
        self.lblTipo=Label(self,text="Tipo de licencia",width=50,height=3)
        self.opciones=ttk.Combobox(self,width=55,height=5)
        self.opciones["values"]=["Licencias de conducir tipo A (motocicletas)","Licencias de conducir tipo B (automóviles y camiones)",
        "Licencias de conducción tipo C (autobús y taxi)","Licencias de conducir tipo D (tractores y maquinaria)",
        "Licencias tipo E (universales)"]

        self.btnGenerar=Button(self,text="Generar reporte",width=50,height=3,bg="#49A",command=self.crearReportePorTipoLicencia)

        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.lblTipo.grid(row=0,column=1,padx=10,pady=10)
        self.opciones.grid(row=1,column=1,padx=10,pady=10)
        self.btnGenerar.grid(row=2,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=6,column=1,padx=10,pady=10)
class SubMenuSede(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()
    def crearReporteSede(self):
        opciones=["Sede Central, San Sebastián", "Zona Sur, Perez Zeledón",
                "Zona Norte, San Carlos","GAM, Tránsito San Ramón","GAM, Montecillos de Alajuela",
                "GAM, Tránsito Cartago",
                "GAM, Barva de Heredia",
                "Pacífico, Liberia","Pacífico, Nicoya",
                "Puntarenas, Chacarita","Zona Sur, Río Claro de Golfito",
                "Limón, Barrio Sandoval de Moín","Atlántico, Guápiles"]
        if self.opciones.get() in opciones:
            if reporteLicenciasPorSede(self.opciones.get())==2:#crarReporetesExcel.py
                messagebox.showinfo("Reporte generado","Se ha generado el reporte.")
                self.opciones.delete(0,"end")
            elif reporteLicenciasPorSede(self.opciones.get())==1:
                messagebox.showwarning("Aviso de creación","El archivo está abierto, cierrelo para continuar")
            else:
                messagebox.showwarning("No se pudo crear el archivo","No existen personas que cumplan sus parámetros de búsqueda.")
        else:
            messagebox.showerror("Ha ocurrido un error","Debe seleccionar una opción de la caja de opciones.")
            self.opciones.delete(0,"end")
    def create_widgets(self):#crea los botones y etiquetas.
        self.lblTipo=Label(self,text="Reporte por Sede",width=50,height=3)
        self.opciones=ttk.Combobox(self,width=55,height=5)
        self.opciones["values"]=["Sede Central, San Sebastián", "Zona Sur, Perez Zeledón",
                "Zona Norte, San Carlos","GAM, Tránsito San Ramón","GAM, Montecillos de Alajuela",
                "GAM, Tránsito Cartago",
                "GAM, Barva de Heredia",
                "Pacífico, Liberia","Pacífico, Nicoya",
                "Puntarenas, Chacarita","Zona Sur, Río Claro de Golfito",
                "Limón, Barrio Sandoval de Moín","Atlántico, Guápiles"]
        self.opciones['state']='readonly'
        
        self.btnGenerar=Button(self,text="Generar reporte",width=50,height=3,bg="#49A",command=self.crearReporteSede)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
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
        self.lblHabladaFelipe=Label(self,text="Holi, soy Felipe.",width=100,height=3)
        self.btnSalir=Button(self,text="Salir",width=100,height=3,bg="#49A",command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.lblNosotros.grid(row=5,column=1,padx=10,pady=10)
        self.lblFelipe.grid(row=6,column=1,padx=10,pady=10)
        self.lblHabladaFelipe.grid(row=7,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=9,column=1,padx=10,pady=10)

#trae la información del html de una vez, para tener los tipos de licencia desde el principio.
#crearListaInformacion()
root = Tk()
root.wm_title("Reporte de conductores")#titulo de la ventana
app = Menu(root) 
app.mainloop()
