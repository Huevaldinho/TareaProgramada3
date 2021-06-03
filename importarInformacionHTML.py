#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021 6:00 pm
#Última modificación: 
#Versión: 3.9.2

#IMPORTACIONES
from bs4 import BeautifulSoup
import requests
import pandas as pd
from archivos import *
#FUNCIONES HTML
def obtenerCategorias():
    """
    Función: Obtener las categorias de licencias de la página web.
    Entrada: N/A.
    Salida: 
    -categorias(list): Lista de categorias.
    """
    url="https://practicatest.cr/blog/licencias/tipos-licencia-conducir-costa-rica"
    page=requests.get(url)#manda a traer toda la info del url.
    soup = BeautifulSoup(page.content,"html.parser")#
    #Licencias
    licencias=soup.find_all("h2")#Obtiene todas las etiquetas h2.
    categorias= list()#lita para guardar las categorias.
    contadorCategoria=0#porque hay un h2 anterior a este que se está guardando.
    for i in licencias:#saca cada una de las h2.
        if contadorCategoria==0:#para quitar ese vacío que está de primero.
            contadorCategoria+=1
            continue
        categorias.append(i.text)#obtiene solo el contenido que está en el h2.
        contadorCategoria+=1
    return categorias
def obtenerSubcategorias():
    """
    Función: Obtener todas las subcategorias.
    Entrada: N/A.
    Salida: 
    -subCategoriaLimpia: Lista de subcategorias.
    """
    url="https://practicatest.cr/blog/licencias/tipos-licencia-conducir-costa-rica"
    page=requests.get(url)#manda a traer toda la info del url.
    soup = BeautifulSoup(page.content,"html.parser")#
    #Subcategorias
    subLiencias=soup.find_all("h3")#encuentra las etiquetas con h3.
    subCategorias=list()#crea la lista para guardar el contenido de todas las h3.
    contadorCategoria=0#inicia contador para escoger solo las h3 que se ocupa.
    subLiencias=subLiencias[10:]
    for j in subLiencias:#ciclo para sacar solo las h3 que se requiere.
        subCategorias.append(j.text)#guarda el texto de las h3.
        contadorCategoria+=1
    subCategoriaLimpia=[]#lista para guardar las lista limpia, porque está arrastrando \n al final de casi todas.
    contadorCategoria=0
    for k in subCategorias:
        if contadorCategoria==1 or contadorCategoria==2 or contadorCategoria==3 or contadorCategoria==4 or contadorCategoria==5 or contadorCategoria==6 or contadorCategoria==7 or contadorCategoria==8 or contadorCategoria==12 or contadorCategoria==13:
            subCategoriaLimpia.append(k[0:-1])
            contadorCategoria+=1
            continue
        subCategoriaLimpia.append(k)
        contadorCategoria+=1
    return subCategoriaLimpia
def obtenerComentarios():
    """
    Función: Obtener los comentarios de cada subcategoria de licencia.
    Entrada: N/A.
    Salida:
    -comentarioTexto(list): Lista de comentarios.
    """
    url="https://practicatest.cr/blog/licencias/tipos-licencia-conducir-costa-rica"
    page=requests.get(url)#manda a traer toda la info del url.
    soup = BeautifulSoup(page.content,"html.parser")#
    #Comentarios
    comentarios=soup.find_all("p")
    comentarioTexto=list()
    contadorCategoria=0#reincia al contador
    comentarios=comentarios[18:]#Corta la lista para coger solo los comentarios.
    limpiar=[0,4,8,16,17,18,22,26,31,38,43,51,54,67,74]#lista de los que hay que limpiar.
    buenos=[0,4,8,15,16,16,17,18,22,26,31,38,43,53,54,59,63,67,74]#todos los indices que tienen texto
    for n in comentarios:#saca los <p>
        if contadorCategoria in buenos:#buscamos los nos sirven.
            if contadorCategoria in limpiar:#los que tienen \n al final
                comentarioTexto.append(n.text[0:-1])#quita el \n
            else:
                comentarioTexto.append(n.text)
        contadorCategoria+=1
    comentarioTexto.append("Permite manejar todo tipo de vehículo, excepto los de transporte público.")#NO LO ESTA AGARRANDO
    return comentarioTexto
def obtenerRequisitos():
    """
    Función: Obtener los requisitos de cada subcategoria de licencia.
    Entrada: N/A.
    Salida: 
    -requisitosTexto(list): Lista de requisitos
    """
    url="https://practicatest.cr/blog/licencias/tipos-licencia-conducir-costa-rica"
    page=requests.get(url)#manda a traer toda la info del url.
    soup = BeautifulSoup(page.content,"html.parser")#
    #REQUISITOS
    requisitos=soup.find_all("ul")
    requisitosTexto=list()
    contadorCategoria=0#reincia al contador
    requisitosListo=[8,9,11,11,12,13,14,15,16,17,18,19]
    listaRequisitosLimpiar=[6,7,8,9]
    for g in requisitos:
        if contadorCategoria in requisitosListo:
            if contadorCategoria==11:
                requisitosTexto.append("Ser mayor de 18 años.\nCédula o documento de identificación original del aspirante.\nDictamen médico digital para licencia de conducir clase A3.\nHacer examen teórico y examen práctico para licencia de conducir A3.")
            if contadorCategoria in listaRequisitosLimpiar:
                requisitosTexto.append(g.text[0:-1])
            else:
                requisitosTexto.append(g.text)
        contadorCategoria+=1
    return requisitosTexto
def crearListaInformacion():
    """
    Función: Crear lista con la información requerida de la página web.
    Entrada: N/A.
    Salida:
    -[A,B,C,D](list): Matriz con todas las categorias, subcategorias, comentarios y requisitos según cada licencia.
    """
    categorias=obtenerCategorias()
    subCategorias=obtenerSubcategorias()
    comentarios=obtenerComentarios()
    requisitos=obtenerRequisitos()
    A=[categorias[0],[subCategorias[0],subCategorias[1],subCategorias[2]],[comentarios[0],comentarios[1],comentarios[2]],[requisitos[0],requisitos[1],requisitos[2]]]
    B=[categorias[1],[subCategorias[3],subCategorias[4],subCategorias[5],subCategorias[6]],[[comentarios[3],comentarios[4],comentarios[5],comentarios[6]],comentarios[7],comentarios[8],comentarios[9]],[requisitos[3],requisitos[4],requisitos[5],requisitos[6]]]
    C=[categorias[2],[subCategorias[7],subCategorias[8]],[comentarios[10],comentarios[11]],[requisitos[7],requisitos[8]]]
    D=[categorias[3],[subCategorias[9],subCategorias[10],subCategorias[11]],[comentarios[14],comentarios[15],comentarios[16]],requisitos[9]]
    E=[categorias[4],[subCategorias[12],subCategorias[13]],[comentarios[17],comentarios[18]],[requisitos[10],requisitos[11]]]
    #Lista de subCategorias de licencias.
    listaSubCategoriaLicencias=[subCategorias[0],subCategorias[1],subCategorias[2],subCategorias[3],subCategorias[4],subCategorias[5],
    subCategorias[7],subCategorias[8],subCategorias[9],subCategorias[10],subCategorias[12],subCategorias[13]]
    graba("informacionLicencias",[A,B,C,D,E])#Graba toda la información de la página.
    graba("subTiposLicencias",listaSubCategoriaLicencias)#Graba solo las subCategorias.
    return