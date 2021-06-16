#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 12/06/2021 10:25 pm
#Versión: 3.9.2

from xml.etree.ElementTree import TreeBuilder
import names
import random
import re
import datetime
from datetime import date
from clases import *
from datetime import *
from archivos import *
from importarInformacionHTML import *

def formatoCedula(cedula=None):#recibe str solo para que no de error la expresion regular
    """
    Función: Validar formato de cédula de Costa Rica.
    Entrada: 
    -cedula(str): Cédula.
    Salida:
    -True(Bool): Formato de cédula es correcto.
    -False(Bool): Formato de cédula es incorrecto
    """
    if re.match("^[1-9]{1}[0-9]{8}$",cedula):
        return True
    return False

def formatofecha(fecha=None):
    """
    Función: Validar fecha
    Entrada: Fecha a validar
    Salida: True o false
    """
    if re.match("\d{1,2}-\d{1,2}-\d{4}",fecha):
        return True
    return False
def generarLicencias(contador):
    """
    Función: Crear licencias.
    Entrada: 
    -contador(int): Cantidad de licencias a crear.
    Salida: generarLicencias(contador-1), hasta el contador sea 0.
    """
    ##### CONTADOR DICE LA CANTIDAD DE PERSONAS A GENERAR #####
    if contador == 0: #acaba la recursividad
        return
    totalLicencias=lee("licencias")
    sublicencias=obtenerSubcategorias()
    lugaresSede={
        1:["Sede Central, San Sebastián", "Zona Sur, Perez Zeledón"],
        2:["Zona Norte, San Carlos","GAM, Tránsito San Ramón","GAM, Montecillos de Alajuela"],
        3:["GAM, Tránsito Cartago"],
        4:["GAM, Barva de Heredia"],
        5:["Pacífico, Liberia","Pacífico, Nicoya"],
        6:["Puntarenas, Chacarita","Zona Sur, Río Claro de Golfito"],
        7:["Limón, Barrio Sandoval de Moín","Atlántico, Guápiles"]
        }
    for i in range(contador):
        cedula = ''.join(str(random.randint(1,9)) for i in range(9)) #crea la cedula
        nombreLicencia="Lic"+cedula #Le da el nombre al objeto
        nombreLicencia=Licencia() #crea el objeto
        if formatoCedula(cedula): nombreLicencia.asignarCedula(int(cedula)) #asigna la cedula

        nombre=names.get_first_name()
        apellido1=names.get_last_name()
        apellido2=names.get_last_name()
        nombreLicencia.asignarNombreCompleto(nombre+" "+apellido1+" "+apellido2) #asigna el nombre

        start_date = date(1945, 1, 1) #inica fecha de nacimiento
        end_date = date.today() #fecha de hoy
        end_date=end_date.replace(year=2003) #cambia el anno de hoy por 2003
        time_between_dates = end_date - start_date 
        random_number_of_days = random.randrange(time_between_dates.days)
        fecha=start_date + timedelta(days=random_number_of_days)
        fechaNacimiento=f"{fecha.day}-{fecha.month}-{fecha.year}"
        if formatofecha(fechaNacimiento): nombreLicencia.asignarFechaNacimiento(fechaNacimiento) #asigna la fecha

        nombreLicencia.asignarFechaExpedicion(f"{date.today().day}-{date.today().month}-{date.today().year}") #fecha de hoy con formato pedido

        resta=date.today()-fecha #dias desde fecha de nacimiento hasta hoy
        if (resta.days//365)>=18 and (resta.days//365)<=25: #resta entera entre 365 para saber edad
            nombreLicencia.asignarFechaVencimiento(f"{date.today().day}-{date.today().month}-{date.today().year+3}") #fecha vencimiento
        else:
            nombreLicencia.asignarFechaVencimiento(f"{date.today().day}-{date.today().month}-{date.today().year+5}")

        nombreLicencia.asignarTipoLicencia(random.choice(sublicencias)) #tipo de licencia

        nombreLicencia.asignarTipoSangre(random.choice(["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])) #tipo de Sangre

        nombreLicencia.asignarDonador(random.choice([True,False])) #Donador True o False

        if cedula[0]=="2": #Dependiendo de la primera letra de la cedula
            nombreLicencia.asignarSede(random.choice(lugaresSede[2])) 
        elif cedula[0]=="3":
            nombreLicencia.asignarSede(random.choice(lugaresSede[3]))
        elif cedula[0]=="4":
            nombreLicencia.asignarSede(random.choice(lugaresSede[4]))
        elif cedula[0]=="5":
            nombreLicencia.asignarSede(random.choice(lugaresSede[5]))
        elif cedula[0]=="6":
            nombreLicencia.asignarSede(random.choice(lugaresSede[6]))
        elif cedula[0]=="7":
            nombreLicencia.asignarSede(random.choice(lugaresSede[7]))
        else: #Si es 1 o 8 o 9
            nombreLicencia.asignarSede(random.choice(lugaresSede[1]))

        nombreLicencia.asignarPuntaje(random.randint(0,12)) #puntaje de entre 0 a 12

        nombreLicencia.asignarCorreo(apellido1.lower()+apellido2[0].lower()+nombre[0].lower()+"@gmail.com") #correo con formato pedido

        #nombreLicencia.mostrarTodo() #lo añadí a la clase y es para poder ver qué sucede

        totalLicencias.append(nombreLicencia) #pega el objeto a la BD
    
    graba("licencias",totalLicencias)

    return ""

def validarNumeroIngresado(numero=None):#En la interfaz vamos a llamar a esta función que valide el número
    """
    Función: Validar que el número ingresado para generar las licencias esté en el intervalo [1:250].
    Entrada: 
    -numero(int): Número a validar.
    Salida:
    -True(Bool): Si es válido.
    -False(Bool): Si es inválido.
    """
    #ingresado en el entry.
    try:
        numero=int(numero)
        if numero>=1 and numero<=250:
            return True
        else:
            return False
    except:
        return False

def validarLicencia(cedula=None):
    """
    Función: Renovar fecha de vencimiento.
    Entrada: 
    -cedula(int): Cédula de la licencia que se renovará en caso que se pueda.
    Salida: 1,2,3,4 o 5. 
    -1(int): Puntaje de licencia está entre 1 y 6, por tanto no puede renovar hasta que no 
    repita el examen.
    -2(int): No se puede renovar porque tiene 0 como puntaje.
    -3(int): Renovación realizada correctamente.
    -4(int): Formato de cédula incorrecto.
    -5(int): La cédula no está registrada.
    """
    today = date.today()#fecha actual
    annoActual=today.year#saca el año para revisar que sea mayor de edad.
    if formatoCedula(str(cedula))==False:
        return 4#formato incorrecto
    try:#si tiene el formato correcto
        licencias=lee("licencias")#carga la base de datos
        for revisar in licencias:#recorre toda la lista de objetos buscando la cédula
            if int(cedula) == revisar.obtenerCedula():#si está en la lista.
                if revisar.obtenerPuntaje()<=6 and revisar.obtenerPuntaje()!=0:
                    return 1#puntaje entre 1 y 6. debe hacer el examen otra vez
                elif revisar.obtenerPuntaje()>6:
                    print("Fecha expedición:",revisar.obtenerFechaExpedicion())
                    print("Fecha vencimiento.",revisar.obtenerFechaVencimiento())
                    fechaNacimiento=int(revisar.obtenerFechaNacimiento()[-4:])#saca solo el año de nacimiento
                    if annoActual-fechaNacimiento<=25:#sumar 3 años al a fecha de vencimiento
                        now = datetime.now()
                        fechaSinAno = str(now.strftime('%d-%m-'))
                        revisar.asignarFechaVencimiento(fechaSinAno+str(int(now.strftime('%Y'))+3))#actualiza puntaje
                    else:#es mayor a 25
                        now = datetime.now()
                        fechaSinAno = str(now.strftime('%d-%m-'))
                        revisar.asignarFechaVencimiento(fechaSinAno+str(int(now.strftime('%Y'))+5))#actualiza puntaje
                    print("Fecha actualziada:",revisar.obtenerFechaVencimiento())
                    graba("licencias",licencias)
                    return 3#renovación correcta
                elif  revisar.obtenerPuntaje()==0:
                    return 2#tiene la licencia retirada permanentemente.
            else:#continua si el objeto de la lista tiene número de cédula diferente.
                continue
    except:#si llega aqui porque tiene otro formato
        return 4#
    return 5#cedula no registrada

def licenciaPDF(cedula):
    """
    Función: Crear el PDF de una licencia.
    """
    try:
        for licencias in lee("licencias"):
            if int(cedula)==licencias.obtenerCedula():
                if licencias.obtenerPuntaje()>6:
                    reporte=PDF('L', 'mm', (60, 135))
                    reporte.crearPDF(licencias.obtenerCedula(),
                    licencias.obtenerFechaExpedicion(),
                    licencias.obtenerFechaNacimiento(),
                    licencias.obtenerFechaVencimiento(),
                    licencias.obtenerTipoLicencia(),
                    licencias.obtenerDonador(),
                    licencias.obtenerTipoSangre(),
                    licencias.obtenerNombreCompleto(),
                    licencias.obtenerSede())
                    reporte.output("LicenciaDe"+str(licencias.obtenerCedula())+".pdf","F")
                    return 1
                else:
                    return 2
        return 0
    except:
        return 0

if lee("licencias")==False:
    lista=[]
    graba("licencias",lista)
else:
    #print(lee("licencias"))
    pass

"""
x=lee("licencias")
for i in x:
    print("CEDULA",i.obtenerCedula())
    print("PUNTAJE",i.obtenerPuntaje())
    print("Fecha nacimiento:",i.obtenerFechaNacimiento(),"\n")
"""
