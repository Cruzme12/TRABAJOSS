
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
import time 
import pygame,sys
from pygame.locals import*
from tkinter import filedialog
pygame.init() 


root=Tk()
root.title("love Alarm")
root.geometry("350x350")
ventanaprincipal=Frame(root,width=1000,height=1000,bg="#10ffaa")
ventanaprincipal.grid()

def clock():
    HoraDeReloj=time.strftime("%H")
    MinutosDeReloj=time.strftime("%M")
    SegundosDeReloj=time.strftime("%S")
    Tiempo=time.strftime(HoraDeReloj+":"+MinutosDeReloj+":"+SegundosDeReloj)
    Labelreloj.config(text=Tiempo)
    Labelreloj.after(1000,clock)
   
    if(HoraDeReloj==entryhoras.get()):
        if(MinutosDeReloj==EntryMinutos.get()):
            if(SegundosDeReloj=="00"):
                pygame.mixer.music.play()
                respuesta=MessageBox.askquestion("AskQuestion","Desea pausar la alarma?")
                if(respuesta=="yes"):
                    pygame.mixer.music.stop()
def alarmapotente():
    MessageBox.showwarning("ShowWarning","Alarma establecida")
def mostrarmusica():
    cancion=filedialog.askopenfilename()
    pygame.mixer.music.load(cancion)

LabelTITULO=Label(ventanaprincipal, text="ALARMA",font=("roboto",14,"bold"),background="#10ffaa",foreground="black",width=8,height=2,justify=CENTER)
LabelTITULO.place(x=120,y=10)


LabelHORA=Label(ventanaprincipal,text="Hora",font=("roboto",14,"bold"),background="#10ffaa",foreground="black",width=8,height=2,justify=CENTER)
LabelHORA.place(x=20,y=100)

entryhoras=StringVar()
entradahoras=Entry(ventanaprincipal,font=("roboto",12),textvariable=entryhoras).place(x=140,y=110)
LabelHORA=Label(ventanaprincipal,text="Minuto",font=("roboto",14,"bold"),background="#10ffaa",foreground="black",width=8,height=2,justify=CENTER)
LabelHORA.place(x=20,y=200)

EntryMinutos=StringVar()
EntradaMinutos=Entry(ventanaprincipal,font=("roboto",12),textvariable=EntryMinutos).place(x=140,y=210)
Labelreloj=Label(ventanaprincipal,font=("roboto",14,"bold"),background="#10ffaa",foreground="black",width=8,height=2,justify=CENTER)
Labelreloj.place(x=120,y=50)
ButtonSetAlarma=Button(ventanaprincipal,font=("roboto",12,"bold"),text="Establecer Alarma",command=alarmapotente).place(x=10,y=280)

ButtonMP3=Button(ventanaprincipal,font=("roboto",12,"bold"),text="Seleccionar Musica",command=mostrarmusica).place(x=180,y=280)


clock()
root.mainloop()