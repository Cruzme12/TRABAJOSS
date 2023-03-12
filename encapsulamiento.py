class carro:
    #atributos
    #marca,modelo,anio, color, numeroserie,cilindros,tipo de motor
    def __init__(self,marca,modelo,anio,color,numeroserie,cilindros,tipomotor):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.color=color
        self.__numeroserie=numeroserie
        self.cilindros=cilindros
        self.tipomotor=tipomotor
        
 #metodos
    def avanzar(self):
        print("avanzando")

    def frenar(self):
        print("frenando")   

    def verificartenencia(self):
        if self.anio >2010:
            return True
        else:
            return False
        
    def calculartenencia(self):
        if camry.verificartenencia(): 
            return 1000*1.15
        else:
            return "no pagas tenencia"
        
    def presentar(self):
        print(f'{self.marca}\n{self.modelo}\n{self.anio}\n{self.color}\n{self.__numeroserie}\n{self.cilindros}\n{self.tipomotor}')

    def getnumeroserie(self):
        print(self.__numeroserie)

camry=carro("toyota","camry",2021,"blanco","x0001",6,"hibrido") #instanciar
camry.presentar()
#camry.numeroserie="x0001"     se creo otro atributo y se le asignó un valor pero sigue teniendo el atributo encapsulado.
#print(camry.numeroserie)
camry.getnumeroserie()
print(camry.verificartenencia())
print(camry.calculartenencia())
