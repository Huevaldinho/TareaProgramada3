#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 20/06/2021 10:25 pm
#Versión: 3.9.2




"""

:D
:D
:D
:D

"""


#CLASE LICENCIA
class Licencia:
    """
    Función: Crear un objeto con atributos: cédula, nombre completo, fecha de nacimiento,
    fecha de expedición de la licencia, fecha de vencimiento de la licencia, tipo de licencia,
    tipo de sangre, donador, sede, puntaje y correo.
    """ 
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
        """
        Función: Guardar la cédula como atributo del objeto.
        Entrada: 
        -pCedula(str): Cédula de la persona.
        Salida: N/A.
        """
        self.cedula=pCedula
    def asignarNombreCompleto(self,pNombreCompleto):
        """
        Función: Guardar el nombre completo como atributo del objeto.
        Entrada: 
        -pNombreCompleto(str): Nombre de la persona.
        Salida: N/A.
        """
        self.nombreCompleto=pNombreCompleto
    def asignarFechaNacimiento(self,pfechaNacimiento):
        """
        Función: Guardar fecha de nacimiento como atributo del objeto.
        Entrada: 
        -pfechaNacimiento(str): Fecha de nacimiento de la persona.
        """
        self.fechaNacimiento=pfechaNacimiento
    def asignarFechaExpedicion(self,pfechaExpedicion):
        """
        Función: Guardar fecha de expedición como atributo del objeto.
        Entrada:
        -pfechaExpedicion(str): Fecha de expedición de la licencia.
        Salida: N/A.
        """
        self.fechaExpedicion=pfechaExpedicion
    def asignarFechaVencimiento(self,pfechaVencimiento):
        """
        Función: Guardar fecha de veicmiento de la licencia como atributo del objeto.
        Entrada: 
        -pfechaVencimiento(str): Fecha de vencimiento de la cédula.
        Salida: N/A.
        """
        self.fechaVencimiento=pfechaVencimiento
    def asignarTipoLicencia(self,ptipoLicencia):
        """
        Función: Guardar tipo de licencia como atributo del objeto.
        Entrada: 
        -ptipoLicencia(str): Tipo de licencia.
        Salida: N/A.
        """
        self.tipoLicencia=ptipoLicencia
    def asignarTipoSangre(self,ptipoSangre):
        """
        Función: Guardar tipo de sangre del conductor como atributo del objeto.
        Entrada:
        -ptipoSangre(str): Tipo de sangre del conductor.
        Salida: N/A.
        """
        self.tipoSangre=ptipoSangre
    def asignarDonador(self,pdonador):
        """
        Función: Guardar si es donador o no como atributo del objeto.
        Entrada:
        -pdonador(Bool): Si es donador de organos o no.
        Salida: N/A.
        """
        self.donador=pdonador
    def asignarSede(self,psede):
        """
        Función: Guardar sede como atributo del objeto.
        Entrada:
        -psede(str): Sede donde sacó la licencia.
        Salida: N/A.
        """
        self.sede=psede
    def asignarPuntaje(self,ppuntaje):
        """
        Función: Guardar puntaje como atributo del objeto.
        Entrada: 
        -ppuntaje(int): Puntaje obtenido.
        Salida: N/A.
        """
        self.puntaje=ppuntaje
    def asignarCorreo(self,pcorreo):
        """
        Función: Guardar correo como atributo del objeto.
        Entrada: 
        -pcorreo(str): Correo del conductor.
        Salida: N/A.
        """
        self.correo=pcorreo
    #GET
    def obtenerCedula(self):
        """
        Función: Obtener la cédula del conductor.
        Entrada: N/A.
        Salida: self.cedula
        """
        return self.cedula
    def obtenerNombreCompleto(self):
        """
        Función: Obtener nombre completo del conductor.
        Entrada: N/A.
        Salida: self.nombreCompleto.
        """
        return self.nombreCompleto
    def obtenerFechaNacimiento(self):
        """
        Función: Obtener fecha de nacimiento del conductor.
        Entrada: N/A.
        Salida: self.fechaNacimiento.
        """
        return self.fechaNacimiento
    def obtenerFechaExpedicion(self):
        """
        Función: Obtener fecha de expedición de la licencia.
        Entrada: N/A.
        Salida: self.fechaExpedicion.
        """
        return self.fechaExpedicion
    def obtenerFechaVencimiento(self):
        """
        Función: Obtener fecha de vencimiento de la licencia.
        Entrada: N/A.
        Salida: self.fechaVencimiento.
        """
        return self.fechaVencimiento
    def obtenerTipoLicencia(self):
        """
        Función: Obtener tipo de licencia.
        Entrada: N/A.
        Salida: self.tipoLiecencia.
        """
        return self.tipoLicencia
    def obtenerTipoSangre(self):
        """
        Función: Obtener tipo de sangre del conductor.
        Entrada: N/A.
        Salida: self.tipoSangre.
        """
        return self.tipoSangre
    def obtenerDonador(self):
        """
        Función: Obtener si es conductor es donador.
        Entrada: N/A.
        Salida: self.donador.
        """
        return self.donador
    def obtenerSede(self):
        """
        Función: Obtener sede.
        Entrada: N/A.
        Salida: self.sede.
        """
        return self.sede
    def obtenerPuntaje(self):
        """
        Función: Obtener puntaje.
        Entrada: N/A.
        Salida: self.puntaje.
        """
        return self.puntaje
    def obtenerCorreo(self):
        """
        Función: Obtener correo.
        Entrada: N/A.
        Salida: self.correo.
        """
        return self.correo
    
    def mostrarTodo(self):
        """
        Función: Mostrar todos los atributos del objeto.
        Entrada: N/A.
        Salida: [self.cedula,self.nombreCompleto,self.fechaNacimiento,self.fechaExpedicion,self.fechaVencimiento,
        self.tipoLicencia,self.tipoSangre,self.donador,self.sede,self.puntaje,self.correo]
        """
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
        return [self.cedula,self.nombreCompleto,self.fechaNacimiento,self.fechaExpedicion,self.fechaVencimiento,self.tipoLicencia,self.tipoSangre,self.donador,self.sede,self.puntaje,self.correo]
from fpdf import FPDF
from datetime import *

class PDF(FPDF):
    """
    Función: Crear el pdf.
    Entrada: N/A.
    Salida: N/A.
    """
    def republica(self):
        """
        Función: Asignar Titulo al PDF.
        Entrada: N/A.
        Salida: N/A.
        """
        self.set_font("Arial","",11)
        self.set_text_color(0,190,255)
        self.cell(10,9,"REPÚBLICA DE COSTA RICA",0,0,"L")
        self.ln(5)

    def licenciaConducir(self):
        """
        Función: Asignar Licencia de Conducir al PDF.
        Entrada: N/A.
        Salida: N/A.
        """
        self.set_font("Arial","",11)
        self.set_text_color(255,0,17)
        self.cell(10,9,"Licencia de Conducir",0,0,"L")
        self.ln(5)

    def numeroCedula(self,cedula):
        """
        Función: Asignar la cedúla al PDF.
        Entrada: 
        -cedula(str): Cédula del conductor.
        Salida: N/A.
        """
        self.set_font("Arial","B",11)
        self.set_text_color(0,0,0)
        self.cell(7,9,"N°:",0,0,"L")
        self.set_font("Arial","B",11)
        self.set_text_color(255,0,17)
        self.cell(0,9,"CI-"+str(cedula),0,0,"L")
        self.ln(5)
    
    def expedicionNacimiento(self,expedicion,nacimiento):
        """
        Función: Asgianr fecha de expedición y de nacimiento al PDF.
        Entrada: 
        -expedicion(str): Fecha de expedición de licencia.
        -nacimiento(str): Fecha de nacimiento.
        """
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
        """
        Función: Asignar fecha de vencimiento al PDF.
        Entrada: 
        -vencimiento(str): Fecha de vencimiento de la licencia.
        """
        self.set_font("Arial","B",11)
        self.set_text_color(0,0,0)
        self.cell(25,9,"Vencimiento:",0,0,"L")
        self.set_font("Arial","",11)
        self.set_text_color(255,0,17)
        self.cell(0,9,vencimiento,0,0,"L")
        self.ln(5)

    def tipoLicencia(self,tipoLicencia):
        """
        Función: Asignar tipo de licencia al PDF.
        Entrada: 
        -tipo(str): Tipo de licencia.
        """
        self.set_font("Arial","",11)
        self.cell(10,9,"Tipo:",0,0,"L")
        self.set_font("Arial","B",14)
        self.cell(0,9,tipoLicencia,0,0,"L")
        self.ln(5)

    def donador(self,donador):
        """
        Función: Asignar si es donador o no al PDF.
        Entrada: 
        -donador(Bool): Si el conductor es donador de organos.
        Salida: N/A.
        """
        self.set_font("Arial","",11)
        if donador==True:
            self.cell(10,9,"Donador",0,0,"L")
        else:
            self.cell(10,9,"No donador",0,0,"L")
        self.ln(5)

    def tipoSangre(self,sangre):
        """
        Función: Asignar tipo de sangre al PDF.
        Entrada: 
        -sangre(str): Tipo de sangre del conductor.
        Salida: N/A.
        """
        self.set_font("Arial","",11)
        self.set_text_color(0,0,0)
        self.cell(8,9,"T.S.",0,0,"L")
        self.set_text_color(255,0,17)
        self.cell(7,9,sangre,0,0,"L")
        self.ln(5)

    def nombre(self,nombre):
        """
        Función: Asignar nombre de conductor al PDF.
        Entrada: 
        -nombre(str): Nombre del conductor.
        Salida: N/A.
        """
        self.set_font("Arial","B",14)
        self.set_text_color(0,0,0)
        self.cell(8,9,nombre.upper(),0,0,"L")
        self.ln(5)

    def bottom(self,sede):
        """
        Función: Asignar sede al PDF.
        Entrada: 
        -sede(str): Sede.
        Salida: N/A.d
        """
        self.set_font("Arial","",9)
        self.cell(8,9,datetime.now().strftime("%d-%m-%Y %H:%M")+" "+sede,0,0,"L")
    
    def crearPDF(self,cedula,expedicion,nacimiento,vencimiento,tipoLicencia,donador,sangre,nombre,sede):
        """
        Función: Crear el PDF con algunos de sus atributos.
        Entrada: 
        -cedula(str): Cédula del conductor.
        -expedicion(str): Fecha de expedición de licencia.
        -nacimiento(str): Fecha de nacimiento del conductor. 
        -vencimiento(str): Fecha de vencimiento de la licencia.
        -tipoLicencia(str): Tipo de licencia.
        -donador(Bool): Si el conductor es donador o no.
        -sangre(str): Tipo de sangre del conductor.
        -nombre(str): Nombre del conductor.
        -sede(str): Sede.
        Salida: N/A.
        """
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
