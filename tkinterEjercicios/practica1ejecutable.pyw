from tkinter import* # importamos la libreria tkinter

raiz=Tk()#instanciar con el objeto tk
raiz.title('practica 1')#asigna el titulo de la ventana
raiz.iconbitmap('led.ico')#asigna el icono de la aventana
#raiz.resizable(True,False)#configura el reajuste de tamaño de la ventana
raiz.geometry("600x500")
#raiz.config(width="600px",height="100px")#asigna el tamaño de la ventana
colorfondo="green"
#crear marco o frame
Frame=Frame(raiz)#instanciar un elemento que se llama frame
Frame.pack(fill='both', expand=1)#expandir el marco al tamaño de la raiz
#Frame.pack(side="top")#posiciona el fram en uno de los puntos indicados TOP,LEFT,RIGHT Y BOTTOM
#Frame.pack(anchor=NW)#posiciona el fram en uno de los puntos indicados usando N,S,W,E.
Frame.config(width="600",height="400",cursor="arrow",bg=colorfondo)
                                                       #bg="codigo"
#Elemento etiqueta Lable
titulo=Label(Frame,text="EMMANUEL PUTO",font=("Retro Computer",30),bg=colorfondo)
titulo.pack()
#titulo2
titulo2=Label(Frame,text="ZORRITA",font=("retrocomputer",30),bg=colorfondo)
titulo2.pack()

boton=Button(Frame,text="click aqui",cursor="pirate",width=10,height=1,font=("retrocomputer",10))
boton.pack()
#rgb(0-255,green,blue)                                 
#hexadecimal 0-9 A-F
#RRGGBB                                                
raiz.mainloop()#while true