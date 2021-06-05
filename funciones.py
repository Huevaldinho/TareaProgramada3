#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
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

def generarLicencias(contador):
    ##### CONTADOR DICE LA CANTIDAD DE PERSONAS A GENERAR #####

    if contador == 0: #acaba la recursividad
        return
    
    totalLicencias=lee("licencias")
    lugaresSede={
        1:["Sede Central, \n\tSan Sebastián", "Zona Sur, \n\tPerez Zeledón"],
        2:["Zona Norte, \n\tSan Carlos","GAM, \n\tTránsito San Ramón","GAM, \n\tMontecillos de Alajuela"],
        3:["GAM, \n\tTránsito Cartago"],
        4:["GAM, \n\tBarva de Heredia"],
        5:["Pacífico, \n\tLiberia","Pacífico, \n\tNicoya"],
        6:["Puntarenas, \n\tChacarita","Zona Sur, \n\tRío Claro de Golfito"],
        7:["Limón, \n\tBarrio Sandoval de Moín","Atlántico, \n\tGuápiles"]
        }

    cedula = ''.join(str(random.randint(0,9)) for i in range(9)) #crea la cedula
    nombreLicencia="Lic"+cedula #Le da el nombre al objeto
    nombreLicencia=Licencia() #crea el objeto
    nombreLicencia.asignarCedula(cedula) #asigna la cedula

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
    nombreLicencia.asignarFechaNacimiento(fechaNacimiento) #asigna la fecha

    nombreLicencia.asignarFechaExpedicion(f"{date.today().day}-{date.today().month}-{date.today().year}") #fecha de hoy con formato pedido

    resta=date.today()-fecha #dias desde fecha de nacimiento hasta hoy
    if (resta.days//365)>=18 and (resta.days//365)<=25: #resta entera entre 365 para saber edad
        nombreLicencia.asignarFechaVencimiento(f"{date.today().day}-{date.today().month}-{date.today().year+3}") #fecha vencimiento
    else:
        nombreLicencia.asignarFechaVencimiento(f"{date.today().day}-{date.today().month}-{date.today().year+5}")

    nombreLicencia.asignarTipoLicencia(random.choice(obtenerSubcategorias())) 

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

    nombreLicencia.mostrarTodo() #lo añadí a la clase y es para poder ver qué sucede

    totalLicencias.append(nombreLicencia) #pega el objeto a la BD
    graba("licencias",totalLicencias)

    return generarLicencias(contador-1)
def validarNumeroIngresado(numero=None):#En la interfaz vamos a llamar a esta función que valide el número
    #ingresado en el entry.
    try:
        numero=int(numero)
        if numero>=1 and numero<=250:
            return True
        else:
            return False
    except:
        return False
def formatoCedula(cedula=None):#recibe str solo para que no de error la expresion regular
    if re.match("^[1-9]{1}[0-9]{8}$",cedula):
        return True
    return False
def validarLicencia(cedula=None):
    print("Entra a la funcion")
    today = date.today()#fecha actual
    annoActual=today.year#saca el año para revisar que sea mayor de edad.
    if formatoCedula(str(cedula))==False:
        return False
    try:#si tiene el formato correcto
        licencias=lee("licencias")#carga la base de datos
        for revisar in licencias:#recorre toda la lista de objetos buscando la cédula
            if cedula == revisar.obtenerCedula():#si está en la lista.
                if revisar.obtenerPuntaje()<=6 and revisar.obtenerPuntaje()!=0:
                    return 1#1 significa error 1. no puede renovar porque debe volver a hacer el examen
                elif revisar.obtenerPuntaje()>6:
                    print("Fecha vencimiento.",revisar.obtenerFechaVencimiento())
                    fechaNacimiento=int(revisar.obtenerFechaNacimiento()[-4:])#saca solo el año de nacimiento
                    if annoActual-fechaNacimiento<=25:#sumar 3 años al a fecha de vencimiento
                        now = datetime.now()#saco fecha
                        fechaSinAno = str(now.strftime('%d-%m-%Y'))[0:6]#saco fecha sin año
                        annoSumado=(str(now.strftime('%d-%m-%Y'))[6:])#saco año
                        annoSumado=int(annoSumado)+3#sumo 3 años al año actual
                        revisar.asignarFechaVencimiento(fechaSinAno+str(annoSumado))#pego ambas cosas
                        print("Fecha actualziada:",revisar.obtenerFechaVencimiento())
                        return True
                    else:#es mayor a 25
                        now = datetime.now()
                        fechaSinAno = str(now.strftime('%d-%m-%Y'))[0:6]
                        annoSumado=(str(now.strftime('%d-%m-%Y'))[6:])
                        annoSumado=int(annoSumado)+5
                        revisar.asignarFechaVencimiento(fechaSinAno+str(annoSumado))
                        print("Fecha actualziada:",revisar.obtenerFechaVencimiento())
                        return True
                elif  revisar.obtenerPuntaje()==0:
                    return 2#tiene la licencia retirada permanentemente.
            else:#continua si el objeto de la lista tiene número de cédula diferente.
                continue
    except:#si llega aqui porque tiene otro formato
        print("Error")
        return False
    return False#nunca encontró la cédula
if lee("licencias")==False:
    lista=[]
    graba("licencias",lista)
else:
    #print(lee("licencias"))#lista objetos(licencicias)
    pass

x=lee("licencias")
for i in x:
    print("CEDULA",i.obtenerCedula())
    print("PUNTAJE",i.obtenerPuntaje())
    print("Fecha nacimiento:",i.obtenerFechaNacimiento(),"\n")

