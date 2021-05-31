#PRUEBAS INTERFAZ GRÄFICA CON POO
"""from tkinter import *
class Application(Frame):#hereda de clase Frame.
    def __init__(self, master=None):#contructor. master es el contenedor del frame. master es root, está al final.
        super().__init__(master)#llama al constructor de la clase Frame.
        self.master = master #le dice que el frame está contenido en master(root).
        self.master.geometry("300x300")
        self.pack()
        self.create_widgets()
    def create_widgets(self):#crea botones
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        #Boton de salida.
        self.quit = Button(self, text="QUIT", fg="red",command=self.master.destroy)#se puede usar root.destroy
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = Tk()#crea la ventana principal.
app = Application(master=root)#significa: cree objeto Aplication y se va a ubicar en root.
app.mainloop()#comienza el ciclo de eventos de la ventana.
"""

from tkinter import Tk,Label,Button,Entry, Frame
from typing import Collection


class FrSuma(Frame):#hereda de la clase Frame.

    def __init__(self, master=None):
        super().__init__(master,width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()

    def fSuma(self):
        n1=self.txtNum1.get()#obtiene el Entry llamado  self.txtNum1
        n2=self.txtNum2.get()#obtiene el Entry llamado  self.txtNum2
        r=float(n1)+float(n2)
        self.txtNum3.delete(0,'end')
        self.txtNum3.insert(0,r)#inserta el resultado de la suma en el Entry llamado self.txtNum3
    def crearXML(self):
        print("Crear XML")
    def crearlicencia(self):
        print("Crear licencia")
    def create_widgets(self):#crea los botones y etiquetas.
        self.btnCrearXML=Button(self,text="Crear XML",width=100,height=3,command=self.crearXML)
        self.btnCrearLicencia=Button(self,text="Crear Licencia",width=100,height=3,command=self.crearlicencia)
        
        self.btnSalir=Button(self,text="Salir",width=20,height=3,command=self.master.destroy)
        #Lugar ubicación
        self.btnCrearXML.grid(row=0,column=1,padx=10,pady=10)
        self.btnCrearLicencia.grid(row=1,column=1,padx=10,pady=10)
        self.btnSalir.grid(row=5,column=1,padx=10,pady=10)




root = Tk()
root.wm_title("Suma de numeros")
app = FrSuma(root) 
app.mainloop()
