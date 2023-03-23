from tkinter import *
from tkinter import ttk

root=Tk()

def Convertir():

    if monedaActual.get()!=Convertirmoneda.get():
        if Convertirmoneda.get()=="PESOS MEXICANOS":
            if monedaActual.get()=="DOLARES":
                resultado = moneda.get()*19.00
                textoNumeroB.config(text=f'{resultado} PESOS MEXICANOS')

            if monedaActual.get()=="EUROS":
                resultado = moneda.get()*20.29
                textoNumeroB.config(text=f'{resultado} PESOS MEXICANOS')

        if Convertirmoneda.get()=="DOLARES":

            if monedaActual.get()=="PESOS MEXICANOS":
                resultado = moneda.get()*0.053
                textoNumeroB.config(text=f'{resultado} DOLARES')
            if monedaActual.get()=="EUROS":
                resultado = moneda.get()*1.07
                textoNumeroB.config(text=f'{resultado} DOLARES')

        if Convertirmoneda.get()=="EUROS":
            if monedaActual.get()=="PESOS MEXICANOS":
                resultado = moneda.get()*0.049
                textoNumeroB.config(text=f'{resultado} EUROS')

            if monedaActual.get()=="DOLARES":
                resultado = moneda.get()*0.94
                textoNumeroB.config(text=f'{resultado} EUROS')
    else:
        textoNumeroB.config(text=f'Verifica lo que introduciste')


moneda = IntVar()
Convertirmoneda = StringVar()
monedaActual = StringVar()

ventanaPrincipal = Frame(root,bg="#738F91")
ventanaPrincipal.grid()

titulo = Label(ventanaPrincipal, text="CONVERTIDOR DE DIVISAS", font=("Roboto",15,),bg="#738F91")
titulo.grid(row=1, column=1, padx=10, columnspan=2)

#Etiqueta moneda actual
titulo = Label(ventanaPrincipal, text="CANTIDAD", font=("Roboto",10),bg="#738F91")
titulo.grid(row=2, column=1, padx=10, pady=10)

textoNumeroA = Entry(ventanaPrincipal, font=("Roboto",10), textvariable=moneda).grid(row=2, column=2, padx=10, pady=10)

#actual
titulo = Label(ventanaPrincipal, text="MONEDA DE ORIGEN", font=("Roboto",10),bg="#738F91")
titulo.grid(row=3, column=1, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["DOLARES", "PESOS MEXICANOS", "EUROS"], state="readonly", textvariable=monedaActual).grid(row=4, column=1, padx=10, pady=10)

#convertir
titulo = Label(ventanaPrincipal, text="CONVERTIR A:", font=("Roboto",10),bg="#738F91")
titulo.grid(row=3, column=2, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["DOLARES", "PESOS MEXICANOS", "EUROS"], state="readonly", textvariable = Convertirmoneda).grid(row=4, column=2, padx=10, pady=10)

#resultado
titulo = Label(ventanaPrincipal, text="RESULTADO", font=("Roboto",10),bg="#738F91")
titulo.grid(row=5, column=1, padx=10, pady=10)

textoNumeroB = Label(ventanaPrincipal, text="", font=("Roboto",10))
textoNumeroB.grid(row=5, column=2, padx=10, pady=10)

#Boton para convertir
botonConvertir = Button(ventanaPrincipal, text="CONVERTIR", font=("Roboto",10), command=Convertir,bg="#738F91").grid(row=6, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()