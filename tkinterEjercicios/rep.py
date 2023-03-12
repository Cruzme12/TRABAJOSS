from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os


pygame.init() #iniciamos modulo de pygame

#funcion boton abrir archivo
def abrirArchivo():
    cancion=filedialog.askopenfilename() #guardar el nombre o la cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
    

def Playsong():
    pygame.mixer.music.play()
def stopsong():
    pygame.mixer.music.stop()
def pausesong():
    pygame.mixer.music.pause()
def resumesong():
    pygame.mixer.music.unpause()
def volumenMas():
    volumensubir=pygame.mixer.music.get_volume() + 0.5
    print(volumensubir)
    pygame.mixer.music.set_volume(volumensubir)
def volumenmenos():
    volumenbajar=pygame.mixer.music.get_volume() - 0.5
    print(volumenbajar)
    pygame.mixer.music.set_volume(volumenbajar)



raiz = Tk()

raiz.title("Reproductor MP3 - GUI")
raiz.iconbitmap("spo.ico")
raiz.geometry("775x650")
raiz.resizable(0,0)
#crear frame
Frameprincipal=Frame(raiz,bg="#738F91")
Frameprincipal.pack(fill="both",expand=1)
#TITULO REPRODUCTOR
tituloReproductor= Label(Frameprincipal,text="REPRODUCTOR MP3-GUI",font=("PowerMax",15,"bold"),bg="#738F91",fg="#FBFBFB")
tituloReproductor.place(relx=0.35,rely=0.05)
#BOTON OPEN SONG
botonOpenSong=Button(Frameprincipal,text="OPEN SONG",bg="#42AB49",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=abrirArchivo)
botonOpenSong.place(relx=0.02,rely=0.7)
#play song
botonPlaySong=Button(Frameprincipal,text="PLAY",bg="#E2504C",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=Playsong)
botonPlaySong.place(relx=0.22,rely=0.7)
#stop song
botonStopSong=Button(Frameprincipal,text="STOP",bg="#FFC400",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=stopsong)
botonStopSong.place(relx=0.42,rely=0.7)
#RESUME song
botonResumeSong=Button(Frameprincipal,text="RESUME",bg="#550099",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=resumesong)
botonResumeSong.place(relx=0.62,rely=0.7)
#PAUSE song
botonPauseSong=Button(Frameprincipal,text="PAUSE",bg="#42AB49",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=pausesong)
botonPauseSong.place(relx=0.82,rely=0.7)
#volumen + song
botonVolumeSong=Button(Frameprincipal,text="Volumen +",bg="#550099",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=volumenMas)
botonVolumeSong.place(relx=0.22,rely=0.85)       
#volumen - song
botonVolumemenosSong=Button(Frameprincipal,text="Volumen -",bg="#550099",cursor="pirate",fg="#FBFBFB",width=12,height=2,font=("retrocomputer",12,"bold"),command=volumenmenos)
botonVolumemenosSong.place(relx=0.62,rely=0.85)                    
raiz.mainloop()
