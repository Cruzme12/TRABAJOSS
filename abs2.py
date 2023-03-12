#abstraccion 
class Pilares:
    #propiedades/atributos 
    #constructor: es el bloque para asignar las propiedades del objeto    ¡¡¡SE DEBE UTILIZAR (SELF) COMO PRIMER PARAMETRO!!!
    #init permite inicializar los valores del constructor
    def __init__(self,nombre,espada,respiracion,posturas,nivelpoder):
        self.nombre=nombre
        self.espada=espada
        self.respiracion=respiracion
        self.posturas=posturas
        self.nivelpoder=nivelpoder
        self.tipo="humano"
    


    #Metodos 
    def ataque(self):
        print("ataque")

    def defensa(self):
        print("defendiendo")

class Aprendiz(Pilares):
    pass

#pilares
himejima=Pilares("himejima","bolas picos","respiracion de la roca",5,100)
rengoku=Pilares("rengoku","katana rojo carmesí","respiracion de llama",9,70)
#lunas
luna1=Pilares("kokushibo","katana lunar","respiracion lunar",9,120)
luna1.tipo="demonio"


print(f'El personaje {himejima.nombre}, su espada es {himejima.espada}, su respiracion es {himejima.respiracion}, tiene {himejima.posturas}, y tiene {himejima.nivelpoder} de nivel de poder')
print("..............................................................................................")
print(f'El personaje {rengoku.nombre}, su espada es {rengoku.espada}, su respiracion es {rengoku.respiracion}, tiene {rengoku.posturas}, y tiene {rengoku.nivelpoder} de nivel de poder')
print("..............................................................................................")
print(f'El personaje {luna1.nombre}, su espada es {luna1.espada}, su respiracion es {luna1.respiracion}, tiene {luna1.posturas}, tiene {luna1.nivelpoder} de nivel de poder y es {luna1.tipo}')

#aprendiz1
Aprendiz=Aprendiz("pips","katana","normalita","0","10")
print(f'El personaje {Aprendiz.nombre}, su espada es {Aprendiz.espada}, su respiracion es {Aprendiz.respiracion}, tiene {Aprendiz.posturas} posturas y tiene {Aprendiz.nivelpoder} de nivel de poder')

print("\U0001f480")