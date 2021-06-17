#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021 6:00 pm
#Última modificación: 12/06/2021 10:25 pm
#Versión: 3.9.2

#FALTA CAMBIAR LOS TEXTOS EN NARANJA POR LO QUE ESTÄ EN LA LISTA informacionLicencias

#Importaciones
import xml.etree.ElementTree as ET
from xml.dom import minidom
from archivos import *
#Función XML
def crearXML():
    """
    Función: Crear archivo .xml
    Entrada: N/A.
    Salida: N/A.
    """
    #Trae la base de datos
    info=lee("informacionLicencias")
    licencias = ET.Element("licencias")#raiz.
    contadorCategoria=0
    for tipo in range(len(info)):#ciclo para los tipos de licencia
        tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name=info[contadorCategoria][0])#Crea el tipo de licencia
        for subTipo in range(len(info[tipo][1])):#Ciclo para cada subtipo de licencia
            subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[tipo][1][subTipo])#Agrega el nombre del subtipo
            comentario=ET.SubElement(subcategoria,"comentario")#Comentario del subtipo
            comentario.text = info[tipo][2][subTipo]#Agrega el comentario
            requisito=ET.SubElement(subcategoria,"requisito")#Requisito del subtipo
            requisito.text = info[tipo][3][subTipo]#Agrega el requisito
        contadorCategoria+=1#Aumenta el contador para la categoria.
    arbol = ET.ElementTree(licencias)#trae todo lo que está en licencia.
    arbol.write("XML.xml")#crea el xml
    return