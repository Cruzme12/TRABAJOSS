#abstraccion 
class cazador:
    #propiedades/atributos 
    #constructor: es el bloque para asignar las propiedades del objeto    ¡¡¡SE DEBE UTILIZAR (SELF) COMO PRIMER PARAMETRO!!!
    #init permite inicializar los valores del constructor
    def __init__(self,nombre,espada,):
        self.nombre=nombre
        self.espada=espada
        
    


    #Metodos 
    def presentar(self):
        print(f'mi nombre es {self.nombre} y mi espada es {self.espada}')
    def ataque(self):
        print("ataque")

    def defensa(self):
        print("defendiendo")

class pilar(cazador):
    def __init__(self, nombre,espada,respiracion, posturas):
        super().__init__(nombre,espada)
        self.respiracion=respiracion
        self.posturas=posturas

    def presentarpilar(self):
        print(f'mi nombre es {self.nombre} y mi espada es {self.espada} mi respiracion de {self.respiracion} y tengo {self.posturas}')
 

cazador1=cazador("tanjiro","espada negra")
cazador1.presentar()
 
print("...................................................................")
rengoku= pilar("rengoku","color rojo","llama",9)
rengoku.presentarpilar()
rengoku.presentar()
