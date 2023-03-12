from tkinter import *
root=Tk()
root.geometry("600x500")
root.title("entry box")

nombre= StringVar()
apellido=StringVar()
def saludar():
    print(f'Hola {nombre.get()} {apellido.get()}')
                                                                       #listbox y chexbot

Frameprincipal= Frame(root,bg="#A0A0A0")
Frameprincipal.pack(fill="both",expand=1)
titulo=Label(Frameprincipal,text="registro",font=("roboto",20,"bold"),bg="#A0A0A0").pack()

nombree=Label(Frameprincipal,text="nombre: ").place(x=10,y=100)
apellidoo=Label(Frameprincipal,text="apellido: ",).place(x=10,y=150)

nombretexto=Entry(Frameprincipal,textvariable=nombre).place(x=80,y=100)
apellidotexto=Entry(Frameprincipal,textvariable=apellido).place(x=80,y=150)

botonsaludar=Button(Frameprincipal,text="Saludar ahora",bg="#42AB49",fg="#FBFBFB",width=10,height=1,font=("retrocomputer",12,"bold"),command=saludar).place(x=10,y=300)

root.mainloop()