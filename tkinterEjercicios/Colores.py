from tkinter import *
from tkinter import messagebox as messageBox
from tkinter import ttk
from tkinter import colorchooser as colorChooser 

root=Tk()
root.geometry("350x300")


def cambiar():
    
    print("#"+c1.get()+c2.get()+c3.get())
    x=c1.get()+c2.get()+c3.get()
    if len(x)>6:
       B.config(text=f'Introdujiste mas de \n 6 digitos, revisa.')

    elif len(x)<6:
       B.config(text=f'Introdujiste menos de \n 6 digitos, revisa.')

    else:
     ventanaPrin.config(bg=("#"+c1.get()+c2.get()+c3.get()))

c1=StringVar()
c2=StringVar()
c3=StringVar()

ventanaPrin=Frame(root)
ventanaPrin.pack(fill="both", expand=1)

titulo=Label(ventanaPrin,text="Ajuste de color",font=("roboto",25))
titulo.grid(row=1,column=2,padx=5,pady=5)

rojo=Label(ventanaPrin,text="Rojo",font=("roboto",20))
rojo.grid(row=3,column=1,padx=5,pady=5)
color1=Entry(ventanaPrin,textvariable=c1,font=("roboto",10))
color1.grid(row=3,column=2,padx=5,pady=5)

verde=Label(ventanaPrin,text="Verde",font=("roboto",20))
verde.grid(row=6,column=1,padx=5,pady=5)
color2=Entry(ventanaPrin,textvariable=c2,font=("roboto",10))
color2.grid(row=6,column=2,padx=5,pady=5)

azul=Label(ventanaPrin,text="Azul",font=("roboto",20))
azul.grid(row=9,column=1,padx=5,pady=5)
color3=Entry(ventanaPrin,textvariable=c3,font=("roboto",10))
color3.grid(row=9,column=2,padx=5,pady=5)


CambiarColor=Button(ventanaPrin,text="Cambinar color",font=("roboto",15),command=cambiar)
CambiarColor.grid(row=13,column=2,padx=5,pady=5)

B = Label(ventanaPrin, text="", font=("roboto",15))
B.grid(row=15, column=2, padx=10, pady=10)


root.mainloop()