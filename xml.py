#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021 6:00 pm
#Última modificación: 
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
    info=lee("informacionLicencias")#Trae la información que está en la base de datos para crear el XML
    #RAIZ
    licencias = ET.Element("licencias")#raiz.
    #####################################################################################################################
    #TIPO A
    tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name=info[0][0])#Tipo A
    #Subtipo A1
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[0][1][0])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario A1
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[0][2][0]
    #Requisito A1
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[0][3][0]
    #Subtipo A2
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[0][1][1])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario A2
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[0][2][1]
    #Requisito A2
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[0][3][1]
    #Subtipo A3
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[0][1][2])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario A3
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[0][2][2]
    #Requisito A3
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[0][3][2]
    #####################################################################################################################
    #TIPO B
    tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name=info[1][0])#Tipo B
    #Subtipo B1
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[1][1][0])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario B1
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[1][2][0][0]+info[1][2][0][1]+info[1][2][0][2]+info[1][2][0][3]
    #Requisito B1
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[1][3][0]
    #Subtipo B2
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[1][1][1])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario B2
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[1][2][1]
    #Requisito B2
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[1][3][1]
    #Subtipo B3
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[1][1][2])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario B3
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[1][2][2]
    #Requisito B3
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[1][3][2]
    #Subtipo B4
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[1][1][3])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario B4
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[1][2][3]
    #Requisito B3
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[1][3][3]
    #####################################################################################################################
    #TIPO C
    tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name=info[2][0])#Tipo C
    #Subtipo C1
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[2][1][0])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario C1
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[2][2][0]
    #Requisito C1
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[2][3][0]
    #Subtipo C2
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[2][1][1])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario C2
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[2][2][1]
    #Requisito C2
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[2][3][1]
    #####################################################################################################################
    #TIPO D
    tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name=info[3][0])#Tipo D
    #Subtipo D1
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[3][1][0])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario D1
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[3][2][0]
    #Requisito D1
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[3][3]
    #Subtipo D2
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[3][1][1])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario D2
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[3][2][1]
    #Requisito D2
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[3][3]
    #Subtipo D3
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[3][1][2])#el 1 debe ser 2
    #Comentario D3
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[3][2][2]
    #Requisito D3
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[3][3]
    #####################################################################################################################
    #TIPO E
    tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name=info[4][0])#Tipo E
    #Subtipo E1
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[4][1][0])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario E1
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[4][2][0]
    #Requisito E1
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[4][3][0]
    #Subtipo E2
    subcategoria= ET.SubElement(tipoLicencia,"subTipo",name=info[4][1][1])#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
    #Comentario E2
    comentario=ET.SubElement(subcategoria,"comentario")
    comentario.text = info[4][2][1]
    #Requisito E2
    requisito=ET.SubElement(subcategoria,"requisito")
    requisito.text = info[4][3][1]
    #####################################################################################################################
    arbol = ET.ElementTree(licencias)#trae todo lo que está en licencia.
    arbol.write("XML.xml")#crea el xml
    return