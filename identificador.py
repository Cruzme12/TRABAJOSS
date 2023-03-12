
class persona:
     
    def __init__(self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    
        
    def mostar(self):
            print(f"Mi nombre es {self.nombre}, tengo {self.edad} y mi DNI ES {self.DNI}")


    def esMayordeEdad(self):
        if self.edad >= 60:
            return "Es mayor de edad"
        else:
            return "Todavia pollito"

people=persona("pepito",50,767678)
people.mostar()
print(people.esMayordeEdad())