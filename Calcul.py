from tkinter import *
from PIL import*

root=Tk()

global resultado
def sum():
 global resultado
 resultado=(int(num1.get())+int(num2.get()))

def rest(): 
      global resultado
 
      resultado=(int(num1.get())-int(num2.get()))
def div():
    global resultado
 
    resultado=(int(num1.get())/int(num2.get()))
def mul():
         global resultado
         resultado=(int(num1.get())*int(num2.get()))

def desplegar():
      textoNumeroB.config(text=f'{resultado}')

def reiniciar():
      global e1
      global e2
      global num1
      global num2
      e1=Entry(ventanaPrin,textvariable="",font=("Roboto",10)).grid(row=11,column=3,padx=5,pady=5)
      e2=Entry(ventanaPrin,textvariable="",font=("Roboto",10)).grid(row=12,column=3,padx=5,pady=5)
      textoNumeroB.config(text=f'{0}')


ventanaPrin=Frame(root,bg="#738F91")
root.geometry("350x220")
ventanaPrin.grid(row=1,column=1)

num1=IntVar()
num2=IntVar()
resultado=StringVar()


titulo=Label(ventanaPrin,text="CALCULADORA",font=("Roboto",20),bg="#738F91").grid(row=2,column=3,padx=5,pady=5)
numeroA=Label(ventanaPrin,text="NUMERO A ",font=("Roboto",10),bg="#738F91").grid(row=11,column=2,padx=5,pady=5)
e1=Entry(ventanaPrin,textvariable=num1,font=("Roboto",15)).grid(row=11,column=3,padx=5,pady=5)
numeroB=Label(ventanaPrin,text="NUMERO B:",font=("Roboto",10),bg="#738F91").grid(row=12,column=2,padx=5,pady=5)
e2=Entry(ventanaPrin,textvariable=num2,font=("Roboto",15)).grid(row=12,column=3,padx=5,pady=5)
titulo3=Label(ventanaPrin,text="RESULTADO",font=("Roboto",10),bg="#738F91").grid(row=13,column=2,padx=5,pady=5)

textoNumeroB = Label(ventanaPrin, text="", font=("Roboto",15))
textoNumeroB.grid(row=13,column=3,padx=5,pady=5)

Suma=Button(ventanaPrin,text="SUMA",command=sum,bg="#738F91")
Suma.grid(row=16,column=2,pady=1)

Resta=Button(ventanaPrin,text="RESTA",command=rest,bg="#738F91")
Resta.grid(row=17,column=2,pady=1)

Mult=Button(ventanaPrin,text="MULTI",command=mul,bg="#738F91")
Mult.grid(row=16,column=3,pady=1,padx=5)

Division=Button(ventanaPrin,text="DIVISION",command=div,bg="#738F91")
Division.grid(row=17,column=3,pady=1)

c=Button(ventanaPrin,text="C",command=reiniciar,bg="#738F91")
c.grid(row=16,column=4,pady=1)

igual=Button(ventanaPrin,text="=",command=desplegar,bg="#738F91")
igual.grid(row=17,column=4,pady=1)


root.mainloop()
