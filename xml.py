#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

#EXTRAER INFORMACIÓN DE LA PÁGINA
#importaciones
from bs4 import BeautifulSoup
import requests
import pandas as pd
def obtenerInfoHTML():
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
    #REQUISITOS
    requisitos=soup.find_all("ul")
    requisitosTexto=list()
    contadorCategoria=0#reincia al contador
    requisitosListo=[8,9,11,11,12,13,14,15,16,17,18,19]
    listaRequisitosLimpiar=[6,7,8,9]
    for g in requisitos:
        if contadorCategoria in requisitosListo:
            if contadorCategoria in listaRequisitosLimpiar:
                #requisitosTexto.append(g.text[0:-1])
                requisitosTexto.append(g.text)
            else:
                requisitosTexto.append(g.text)
        contadorCategoria+=1
    #A1,A2,A3
    print(requisitosTexto)
obtenerInfoHTML()
