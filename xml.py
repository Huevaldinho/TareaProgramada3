#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021 6:00 PM
#Última modificación: XX/06/2021 
#Versión: 3.9.2

#FALTA CAMBIAR LOS TEXTOS EN NARANJA POR LO QUE ESTÄ EN LA LISTA informacionLicencias

#Importaciones
import xml.etree.ElementTree as ET
from xml.dom import minidom

#Funciones XML
 
#RAIZ
licencias = ET.Element("licencias")#raiz.
#####################################################################################################################
#TIPO A
tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name="Licencia A")#Tipo A
#SUBTIPO A1
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="A1")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO A1
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario A1"
#REQUISITOS A1
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito A2"

#SUBTIPO A2
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="A2")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO A2
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario A2"
#REQUISITOS A2
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito A2"

#SUBTIPO A3
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="A3")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO A3
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario A3"
#REQUISITOS A3
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Comentario A3"
#####################################################################################################################
#TIPO B
tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name="Licencia B")#Tipo A
#SUBTIPO B1
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="B1")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO B1
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario B1"
#REQUISITOS B1
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito B1"

#SUBTIPO B2
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="B2")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO B2
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario B2"
#REQUISITOS B2
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito B2"

#SUBTIPO B3
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="B3")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO B3
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario B3"
#REQUISITOS B3
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Comentario B3"

#SUBTIPO B4
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="B4")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO B4
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario B4"
#REQUISITOS B3
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Comentario B4"
#####################################################################################################################
#TIPO C
tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name="Licencia C")#Tipo A
#SUBTIPO C1
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="C1")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO C1
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario C1"
#REQUISITOS C1
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito C1"

#SUBTIPO C2
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="C2")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO C2
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario C2"
#REQUISITOS C2
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito C2"

#####################################################################################################################
#TIPO D
tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name="Licencia D")#Tipo A
#SUBTIPO D1
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="D1")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO C1
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario D1"
#REQUISITOS C1
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito D1"

#SUBTIPO D2
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="D2")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO D2
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario D2"
#REQUISITOS D2
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito D2"

#SUBTIPO D3
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="D3")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO D3
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario D3"
#REQUISITOS D3
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito D3"
#####################################################################################################################
#TIPO E
tipoLicencia = ET.SubElement(licencias,'tipoLicencia',name="Licencia E")#Tipo A
#SUBTIPO E1
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="E1")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO E1
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario E1"
#REQUISITOS E1
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito E1"

#SUBTIPO E2
subcategoria= ET.SubElement(tipoLicencia,"subTipo",name="E2")#CAMBIAR QUE ESTÄ EN NARANJA POR NOMBRES DE LA LISTA.
#COMENTARIO E2
comentario=ET.SubElement(subcategoria,"comentario")
comentario.text = "Comentario E2"
#REQUISITOS E2
requisito=ET.SubElement(subcategoria,"requisito")
requisito.text = "Requisito E2"
#####################################################################################################################
#Hace XML
arbol = ET.ElementTree(licencias)#trae todo lo que está en licencia.
arbol.write("XML.xml")#crea el xml
