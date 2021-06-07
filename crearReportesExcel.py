#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

import openpyxl
from archivos import *
from clases import *
def reporteTotalidadLicencias():#Función para crear el reporte de todas las licencias
    totalLicencias=lee("licencias")#trae todas la licencias
    listaLicencias=[]#lista para rellenar las filas.(DATOS)
    for i in totalLicencias:#crea la tupla de cada licencia que se va a guardar en la lista que se utiliza para las filas en el excel.
        if i.obtenerDonador():#esto está guardado como bool.
            donador="Si"
        else:
            donador="No"
        persona=(i.obtenerCedula(),i.obtenerNombreCompleto(),i.obtenerFechaNacimiento(),i.obtenerFechaExpedicion(),i.obtenerFechaVencimiento(),
        i.obtenerTipoLicencia(),i.obtenerTipoSangre(),donador,i.obtenerSede(),i.obtenerPuntaje())
        listaLicencias.append(persona)#guarda la fila (tupla) en las lista.


    wb = openpyxl.Workbook()#crea la instancia (archivo).
    hoja = wb.active#toma la instancia que crea wb y la utiliza como activa.
    hoja.title="Totalidad de licencias"#Asigna el nombre de la hoja.

    # Crea la fila del encabezado con los títulos
    hoja.append(('Cédula', 'Nombre completo', 
    'Fecha Nacimiento', 'Fecha Expedición',"Fecha Vencimiento",
    "Tipo licencia","Tipo Sangre","Donador","Sede","Puntaje"))
    for producto in listaLicencias:
        # producto es una tupla con los valores de un producto 
        hoja.append(producto)
    wb.save('totalidadLiencias.xlsx')#guarda el archivo con el nombre.
    return
reporteTotalidadLicencias()
