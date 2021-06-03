#Tarea Programada 3
#Elaborado por: Felipe Obando y Sebastián Bermúdez.
#Fecha de creación: 01/06/2021
#Última modificación: 
#Versión: 3.9.2

#Función que graba el archivo.
import pickle
def graba(nombreArchivo,lista):
    """
    Función: Grabar/crear un archivo(base de datos).
    Entradas:
    -nombreArchivo(str): Nombre del archivo en el que se va a grabar/crear.
    -lista(list): Lista que se va a guardar en el archivo.
    Salida: N/A.
    """
    try:
        f=open(nombreArchivo,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nombreArchivo)
    return ""
#Función que lee un archivo
def lee (nomArchLeer):
    """
    Función: Grabar/crear un archivo(base de datos).
    Entradas:
    -nombreArchivo(str): Nombre del archivo que se va a cargar en la RAM.
    Salida: 
    -lista(list): Lista de donadores.
    """
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        f.close()
        return lista
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return False