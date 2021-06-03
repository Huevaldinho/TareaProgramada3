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
        print("\nCEDULA: "+self.cedula)
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
sebastian=Licencia()
sebastian.asignarCedula(1)
#lista=[]
#lista.append(sebastian)
#print(sebastian.obtenerCedula())