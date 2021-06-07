#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

#CLASE LICENCIA
class Licencia:
    def __init__(self):
        self.cedula=""
        self.nombreCompleto=""
        self.fechaNacimiento=""
        self.fechaExpedicion=""
        self.fechaVencimiento=""
        self.tipoLicencia=""
        self.tipoSangre=""
        self.donador=False
        self.sede=""
        self.puntaje=0
        self.correo=""
    #SET
    def asignarCedula(self,pCedula):
        self.cedula=pCedula
    def asignarNombreCompleto(self,pNombreCompleto):
        self.nombreCompleto=pNombreCompleto
    def asignarFechaNacimiento(self,pfechaNacimiento):
        self.fechaNacimiento=pfechaNacimiento
    def asignarFechaExpedicion(self,pfechaExpedicion):
        self.fechaExpedicion=pfechaExpedicion
    def asignarFechaVencimiento(self,pfechaVencimiento):
        self.fechaVencimiento=pfechaVencimiento
    def asignarTipoLicencia(self,ptipoLicencia):
        self.tipoLicencia=ptipoLicencia
    def asignarTipoSangre(self,ptipoSangre):
        self.tipoSangre=ptipoSangre
    def asignarDonador(self,pdonador):
        self.donador=pdonador
    def asignarSede(self,psede):
        self.sede=psede
    def asignarPuntaje(self,ppuntaje):
        self.puntaje=ppuntaje
    def asignarCorreo(self,pcorreo):
        self.correo=pcorreo
    #GET
    def obtenerCedula(self):
        return self.cedula
    def obtenerNombreCompleto(self):
        return self.nombreCompleto
    def obtenerFechaNacimiento(self):
        return self.fechaNacimiento
    def obtenerFechaExpedicion(self):
        return self.fechaExpedicion
    def obtenerFechaVencimiento(self):
        return self.fechaVencimiento
    def obtenerTipoLicencia(self):
        return self.tipoLicencia
    def obtenerTipoSangre(self):
        return self.tipoSangre
    def obtenerDonador(self):
        return self.donador
    def obtenerSede(self):
        return self.sede
    def obtenerPuntaje(self):
        return self.puntaje
    def obtenerCorreo(self):
        return self.correo
    
    def mostrarTodo(self):
        print("\nCEDULA: "+str(self.cedula))
        print("\nNOMBRE: "+self.nombreCompleto)
        print("\nFECHA NACIMIENTO: "+self.fechaNacimiento)
        print("\nFECHA EXPEDICION: "+self.fechaExpedicion)
        print("\nFECHA VENCIMIENTO: "+self.fechaVencimiento)
        print("\nTIPO LICENCIA: "+self.tipoLicencia)
        print("\nTIPO SANGRE: "+self.tipoSangre)
        print("\nDONADOR: "+str(self.donador))
        print("\nSEDE: "+self.sede)
        print("\nPUNTAJE: "+str(self.puntaje))
        print("\nCORREO: "+self.correo)
from fpdf import FPDF
from datetime import *

class PDF(FPDF):
    def republica(self):
        self.set_font("Arial","",11)
        self.set_text_color(0,190,255)
        self.cell(10,9,"REPÚBLICA DE COSTA RICA",0,0,"L")
        self.ln(5)

    def licenciaConducir(self):
        self.set_font("Arial","",11)
        self.set_text_color(255,0,17)
        self.cell(10,9,"Licencia de Conducir",0,0,"L")
        self.ln(5)

    def numeroCedula(self,cedula):
        self.set_font("Arial","B",11)
        self.set_text_color(0,0,0)
        self.cell(7,9,"N°:",0,0,"L")
        self.set_font("Arial","B",11)
        self.set_text_color(255,0,17)
        self.cell(0,9,"CI-"+str(cedula),0,0,"L")
        self.ln(5)
    
    def expedicionNacimiento(self,expedicion,nacimiento):
        self.set_text_color(0,0,0)
        self.set_font("Arial","B",11)
        self.cell(23,9,"Expedición:",0,0,"L")
        self.set_font("Arial","",11)
        self.cell(0,9,expedicion,0,0,"L")
        self.ln(5)
        self.set_font("Arial","B",11)
        self.cell(23,9,"Nacimiento:",0,0,"L")
        self.set_font("Arial","",11)
        self.cell(0,9,nacimiento,0,0,"L")
        self.ln(5)

    def vencimiento(self,vencimiento):
        self.set_font("Arial","B",11)
        self.set_text_color(0,0,0)
        self.cell(25,9,"Vencimiento:",0,0,"L")
        self.set_font("Arial","",11)
        self.set_text_color(255,0,17)
        self.cell(0,9,vencimiento,0,0,"L")
        self.ln(5)

    def tipoLicencia(self,tipoLicencia):
        self.set_font("Arial","",11)
        self.cell(10,9,"Tipo:",0,0,"L")
        self.set_font("Arial","B",14)
        self.cell(0,9,tipoLicencia,0,0,"L")
        self.ln(5)

    def donador(self,donador):
        self.set_font("Arial","",11)
        if donador==True:
            self.cell(10,9,"Donador",0,0,"L")
        else:
            self.cell(10,9,"No donador",0,0,"L")
        self.ln(5)

    def tipoSangre(self,sangre):
        self.set_font("Arial","",11)
        self.set_text_color(0,0,0)
        self.cell(8,9,"T.S.",0,0,"L")
        self.set_text_color(255,0,17)
        self.cell(7,9,sangre,0,0,"L")
        self.ln(5)

    def nombre(self,nombre):
        self.set_font("Arial","B",14)
        self.set_text_color(0,0,0)
        self.cell(8,9,nombre.upper(),0,0,"L")
        self.ln(5)

    def bottom(self,sede):
        self.set_font("Arial","",9)
        self.cell(8,9,datetime.now().strftime("%d-%m-%Y %H:%M")+" "+sede,0,0,"L")
    
    def crearPDF(self,cedula,expedicion,nacimiento,vencimiento,tipoLicencia,donador,sangre,nombre,sede):
        self.set_margins(0.1, 0.1 ,0.1)
        self.set_auto_page_break(True)
        self.add_page()
        self.republica()
        self.licenciaConducir()
        self.numeroCedula(cedula)
        self.expedicionNacimiento(expedicion,nacimiento)
        self.vencimiento(vencimiento)
        self.tipoLicencia(tipoLicencia)
        self.donador(donador)
        self.tipoSangre(sangre)
        self.nombre(nombre)
        self.bottom(sede)


#license=PDF('L', 'mm', (60, 135))
#license.crearPDF(cedula,expedicion,nacimiento,vencimiento,tipoLicencia,donador,sangre,nombre,sede)
#license.output("pruebasReporte.pdf","F")