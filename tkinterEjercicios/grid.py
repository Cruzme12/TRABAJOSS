from tkinter import*
from PIL import ImageTk,Image
root= Tk()
#root.geometry("400x400")
ventanaprincipal=Frame(root)
ventanaprincipal.grid()

titulo=Label(ventanaprincipal,text="height",font=("roboto",20))
titulo.grid(row=1,column=1)
titulo2=Label(ventanaprincipal,text="width",font=("roboto",20))
titulo2.grid(row=2,column=1)

textonombre=Entry(ventanaprincipal,font=("roboto",20)).grid(row=1,column=2,padx=10,pady=10)
textonombre2=Entry(ventanaprincipal,font=("roboto",20)).grid(row=2,column=2,padx=10,pady=10)

botoncerrar=Button(ventanaprincipal,text="zoom in",command=root.destroy,width=10,height=5).grid(row=3,column=4)
boton2cerrar=Button(ventanaprincipal,text="zoom out",command=root.destroy,width=10,height=5).grid(row=3,column=6)

img=Image.open("lewis.png")#variable q contiene el nombre de la imagen
imagenmusica=img.resize((150,100))
imag=ImageTk.PhotoImage(imagenmusica)
mititulo=Label(ventanaprincipal,image=imag)
mititulo.grid(row=1,column=6,rowspan=2,columnspan=4,padx=40,pady=10)

control=IntVar()
preserve=Checkbutton(ventanaprincipal, text="preserve",variable=control,font=("roboto",10))
preserve.grid(row=5,column=1,pady=1)









root.mainloop()