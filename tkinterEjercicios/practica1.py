from tkinter import* # importamos la libreria tkinter

raiz=Tk()#instanciar con el objeto tk
raiz.title('practica 1')#asigna el titulo de la ventana
raiz.iconbitmap('led.ico')#asigna el icono de la aventana
raiz.resizable(True,False)#configura el reajuste de tamaño de la ventana
#raiz.config(width="600px",height="100px")#asigna el tamaño de la ventana


raiz.mainloop()#while true