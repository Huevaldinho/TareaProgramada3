#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 02/06/2021
#Última modificación: 
#Versión: 3.9.2


#Importaciones
from datetime import datetime
import enum
from os.path import supports_unicode_filenames
import re
from datetime import *
import pickle
import random
import names
import string
import time

#FUNCIONES

def generarLicencia():
    tipoSangre=["O+","O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    sexo=[True, False]
    sexoEleccion=random.choice(sexo)#elige el sexo pero solo para evaluar, si es mujer nombre de mujer o viceversa con hombre
    if sexoEleccion==False:
        nombreCompleto = (names.get_first_name(gender='female')+" "+names.get_last_name()+" "+names.get_last_name()) #mete nombre mujer
    elif sexoEleccion==True:
        nombreCompleto = (names.get_first_name(gender='male')+" "+names.get_last_name()+" "+names.get_last_name()) #mete nombre mujer
    provincia=random.randint(1,9) #inicia cedula
    tomo=""
    asiento=""
    numero1=""
    for j in range (4):
        tomo+=str(random.randint(0,9))
        asiento+=str(random.randint(0,9))
        numero1+=str(random.randint(0,9)) #para el numero de telefono
    cedula=int(str(provincia)+str(tomo)+str(asiento))#lo pasa a INT.
    start_date = date(1961, 1, 1) #inica fecha de nacimiento
    end_date = date(2003, 5, 25)
    time_between_dates = end_date - start_date
    sangre=(random.choice(tipoSangre)) #mete tipo de sangre
    print(cedula,nombreCompleto,sangre,time_between_dates)
generarLicencia()