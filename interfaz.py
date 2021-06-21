#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 20/06/2021 10:25 pm
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
        super().__init__(master,width=900, height=700)
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
        root.resizable(width=False, height=False)
        crearVentanaLicencias=CreaLicencia(root)
        crearVentanaLicencias['background']='cyan'
        crearVentanaLicencias.mainloop()

    def renovar(self):#3
        root = Tk()
        root.wm_title("Renovar licencias")
        root.resizable(width=False, height=False)
        crearVentanaRenovar=RenovarLicencia(root)
        crearVentanaRenovar['background']='cyan'
        crearVentanaRenovar.mainloop()

    def generarPDF(self):#4
        root = Tk()
        root.wm_title("Generar Reporte PDF")
        root.resizable(width=False, height=False)
        crearVentanaPDF=CreaPDF(root)
        crearVentanaPDF['background']='cyan'
        crearVentanaPDF.mainloop()

    def reportesExcel(self):#5
        root = Tk()#crea la ventana nueva para el submenu de reportes.
        root.wm_title("Reporte de conductores")#titulo de la ventana
        root.resizable(width=False, height=False)
        app = SubMenuExcel(root) 
        app['background']='cyan'
        app.mainloop()
    
    def acerca(self):#6
        root=Tk()
        root.wm_title("Acerca de nosotros")
        root.resizable(width=False, height=False)
        crearVentanaAcerca=Nosotros(root)
        crearVentanaAcerca['background']='cyan'
        crearVentanaAcerca.mainloop()
    
    def salir(self):
        messagebox.showinfo("", "No olvides gestionar pronto tu licencia")#muestra una ventana
        sys.exit()#Cierra la ventana

    def create_widgets(self):#crea los botones y etiquetas.
        self.textoLicencias=Label(self,text="Reporte de Conductores Costa Rica",font=("BiauKai",34,"bold"),fg="LightSkyBlue2",bg='burlywood4')
        self.btnCrearXML=Button(self,text="Crear archivo XML",fg='burlywood4',font=("TimesNewRoman",24),width=27,height=4,bg="LightSkyBlue2",command=self.XML)
        self.btnCrearLicencia=Button(self,text="Crear Licencias",fg='burlywood4',font=("TimesNewRoman",24),width=27,height=4,bg="LightSkyBlue2",command=self.crearlicencia)
        self.btnRenovarLicencia=Button(self,text="Renovar licencia",fg='burlywood4',font=("TimesNewRoman",24),width=27,height=4,bg="LightSkyBlue2",command=self.renovar)
        self.btnGenerarPDF=Button(self,text="Generar PDF",fg='burlywood4',font=("TimesNewRoman",24),width=27,height=4,bg="LightSkyBlue2",command=self.generarPDF)
        self.btnReporteExcel=Button(self,text="Reporte Excel",fg='burlywood4',font=("TimesNewRoman",24),width=27,height=4,bg="LightSkyBlue2",command=self.reportesExcel)
        self.btnAcerca=Button(self,text="Acerca de",fg='burlywood4',font=("TimesNewRoman",24),width=27,height=4,bg="LightSkyBlue2",command=self.acerca)
        self.btnSalir=Button(self,text="Salir",fg='burlywood4',font=("TimesNewRoman",18),width=71,height=3,bg="LightSkyBlue2",command=self.salir)
        #Lugar ubicación
        self.textoLicencias.grid(row=0,column=0,padx=10,pady=5)
        self.textoLicencias.place(relx=0.5,rely=0.1,anchor=CENTER)
        self.btnCrearXML.grid(row=1,column=0,padx=10,pady=4)
        self.btnCrearXML.place(relx=0.25,rely=0.28,anchor=CENTER)
        self.btnCrearLicencia.grid(row=2,column=0,padx=10,pady=4)
        self.btnCrearLicencia.place(relx=0.75,rely=0.28,anchor=CENTER)
        self.btnRenovarLicencia.grid(row=3,column=0,padx=10,pady=4)
        self.btnRenovarLicencia.place(relx=0.25,rely=0.5,anchor=CENTER)
        self.btnGenerarPDF.grid(row=4,column=0,padx=10,pady=4)
        self.btnGenerarPDF.place(relx=0.75,rely=0.5,anchor=CENTER)
        self.btnReporteExcel.grid(row=5,column=0,padx=10,pady=4)
        self.btnReporteExcel.place(relx=0.25,rely=0.72,anchor=CENTER)
        self.btnAcerca.grid(row=6,column=0,padx=10,pady=4)
        self.btnAcerca.place(relx=0.75,rely=0.72,anchor=CENTER)
        self.btnSalir.grid(row=7,column=0,padx=10,pady=4)
        self.btnSalir.place(relx=0.5,rely=0.9,anchor=CENTER)


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

    def clear_text(self):#limpa entry de cédula
        self.entryCantidad.delete(0, 'end')#borra el contenido del entry.

    def create_widgets(self):#crea los botones y etiquetas.
        self.lblCantidad=Label(self,text="¿Cuántas licencias desea generar?",bg='cyan')
        self.entryCantidad=Entry(self,bd=5,width=20)
        self.btnCantidad=Button(self,text="Generar",width=20,command=self.enviarCantidadCreacion)
        self.btnLimpiar=Button(self,text="Limpiar",width=20,command=self.clear_text)
        self.btnSalir=Button(self,text="Regresar",width=20,command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA

        self.lblCantidad.grid(row=0,column=1,padx=10,pady=10)
        self.entryCantidad.grid(row=1,column=1,padx=10,pady=10)
        self.btnCantidad.grid(row=2,column=1,padx=5,pady=10)
        self.btnLimpiar.grid(row=2,column=0,padx=5,pady=10)
        self.btnSalir.grid(row=2,column=2,padx=5,pady=10)

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
        self.lblIngresar=Label(self,text="Ingrese cédula a renovar",bg='cyan')
        self.entryLicencia=Entry(self,bd=5,width=20)
        self.btnRenovar=Button(self,text="Renovar",width=20,command=self.renovacion)
        self.btnLimpiar=Button(self,text="Limpiar",width=20,command=self.clear_text)
        self.btnSalir=Button(self,text="Regresar",width=20,command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        
        self.lblIngresar.grid(row=1,column=1,padx=10,pady=10)
        self.entryLicencia.grid(row=2,column=1,padx=10,pady=10)
        self.btnRenovar.grid(row=3,column=1,padx=10,pady=10)
        self.btnLimpiar.grid(row=3,column=0,padx=10,pady=10)
        self.btnSalir.grid(row=3,column=2,padx=10,pady=10)

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

    def clear_text(self):#limpa entry de cédula
        self.entryCedulaPDF.delete(0, 'end')#borra el contenido del entry.

    def create_widgets(self):#crea los botones y etiquetas.
        self.lblCantidad=Label(self,text="Ingrese la cédula de la persona a la que le desea generar el PDF",bg='cyan')
        self.entryCedulaPDF=Entry(self,bd=5,width=20)
        self.btnCrear=Button(self,text="Crear PDF",width=20,command=self.enviarPDF)
        self.btnLimpiar=Button(self,text="Limpiar",width=20,command=self.clear_text)
        self.btnSalir=Button(self,text="Regresar",width=20,command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA

        self.lblCantidad.grid(row=0,column=1,padx=10,pady=10)
        self.entryCedulaPDF.grid(row=1,column=1,padx=10,pady=10)
        self.btnCrear.grid(row=2,column=1,padx=5,pady=10)
        self.btnLimpiar.grid(row=2,column=0,padx=5,pady=10)
        self.btnSalir.grid(row=2,column=2,padx=5,pady=10)

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
        root.resizable(width=False, height=False)
        app = SubMenuTipoLicencia(root) 
        app['background']='cyan'
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
        root.resizable(width=False, height=False)
        app = SubMenuSede(root) 
        app['background']='cyan'
        app.mainloop()
        pass
    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Totalidad de licencias",width=50,height=2,command=self.enviarTotalReporte)
        self.btnCrearLicencia=Button(self,text="Por tipo de licencia",width=50,height=2,command=self.enviarTipoLicenciaReporte)
        self.btnRenovarLicencia=Button(self,text="Examen por sanción",width=50,height=2,command=self.enviarExamenPorSancionReporte)
        self.btnGenerarPDF=Button(self,text="Los donantes de órganos",width=50,height=2,command=self.enviarDonantesDeOrganos)
        self.btnReporteExcel=Button(self,text="Personas Anuladas",width=50,height=2,command=self.enviarPersonasAnuladas)
        self.btnAcerca=Button(self,text="Licencias por sede",width=50,height=2,command=self.enviarPersonasPorSede)
        self.btnSalir=Button(self,text="Salir",width=50,height=2,command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
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
        super().__init__(master,width=600, height=200)
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
        self.lblTipo=Label(self,text="Seleccione el tipo de licencia",width=50,height=3,bg="cyan")
        self.opciones=ttk.Combobox(self,width=55,height=5)
        self.opciones["values"]=["Licencias de conducir tipo A (motocicletas)","Licencias de conducir tipo B (automóviles y camiones)",
        "Licencias de conducción tipo C (autobús y taxi)","Licencias de conducir tipo D (tractores y maquinaria)",
        "Licencias tipo E (universales)"]
        self.opciones['state']='readonly'
        self.btnGenerar=Button(self,text="Generar reporte",width=20,command=self.crearReportePorTipoLicencia)
        self.btnSalir=Button(self,text="Salir",width=20,command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.lblTipo.place(relx=0.5,rely=0.1,anchor=CENTER)
        self.opciones.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.btnGenerar.place(relx=0.25,rely=0.9,anchor=CENTER)
        self.btnSalir.place(relx=0.75,rely=0.9,anchor=CENTER)
class SubMenuSede(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=600, height=200)
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
        self.lblTipo=Label(self,text="Seleccione la Sede",width=50,height=3,bg='cyan')
        self.opciones=ttk.Combobox(self,width=55,height=5)
        self.opciones["values"]=["Sede Central, San Sebastián", "Zona Sur, Perez Zeledón",
                "Zona Norte, San Carlos","GAM, Tránsito San Ramón","GAM, Montecillos de Alajuela",
                "GAM, Tránsito Cartago",
                "GAM, Barva de Heredia",
                "Pacífico, Liberia","Pacífico, Nicoya",
                "Puntarenas, Chacarita","Zona Sur, Río Claro de Golfito",
                "Limón, Barrio Sandoval de Moín","Atlántico, Guápiles"]
        self.opciones['state']='readonly'
        self.btnGenerar=Button(self,text="Generar reporte",width=20,command=self.crearReporteSede)
        self.btnSalir=Button(self,text="Salir",width=20,command=self.master.destroy)#ESTA CIERRA SOLA LA OTRA VENTANA
        #Lugar ubicación
        self.lblTipo.place(relx=0.5,rely=0.1,anchor=CENTER)
        self.opciones.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.btnGenerar.place(relx=0.25,rely=0.9,anchor=CENTER)
        self.btnSalir.place(relx=0.75,rely=0.9,anchor=CENTER)
class Nosotros(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=500, height=360)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):#crea los botones y etiquetas.
        self.lblNosotros=Label(self,text="Creadores:",font=("TimesNewRoman",25,"bold"),bg='cyan').place(relx=0.5,rely=0.1,anchor=CENTER)
        self.lblSebastian=Label(self,text="Sebastián Bermúdez Acuña",font=("BiauKai",23,),bg='cyan').place(relx=0.5,rely=0.2,anchor=CENTER)
        self.lblCarneDios=Label(self,text="2021110666",font=("TimesNewRoman",18,"italic"),bg='cyan').place(relx=0.5,rely=0.3,anchor=CENTER)
        self.lblFelipe=Label(self,text="Felipe Obando Arrieta",font=("BiauKai",23,),bg='cyan').place(relx=0.5,rely=0.5,anchor=CENTER)
        self.lblCarneFelipe=Label(self,text="2021035489",font=("TimesNewRoman",18,"italic"),bg='cyan').place(relx=0.5,rely=0.6,anchor=CENTER)
        self.btnSalir=Button(self,text="Salir",width=30,height=3,command=self.master.destroy).place(relx=0.5,rely=0.8,anchor=CENTER)

#trae la información del html de una vez, para tener los tipos de licencia desde el principio.
#crearListaInformacion()
root = Tk()
root.wm_title("Reporte de conductores")#titulo de la ventana
root.resizable(width=False, height=False)
app = Menu(root)
app['background']='burlywood4'
app.mainloop()
