class persona:
    
    def __init__(self,nombre,apellido,):
        self.nombre=nombre
        self.apellido=apellido
        

    #Metodos 
    def presentar(self):
        print(f'mi nombre es {self.nombre} y mi apellido es {self.apellido}')
    

class maestro(persona):
    def __init__(self, nombre,apellido,carrera, edad):
        super().__init__(nombre,apellido)
        self.carrera=carrera
        self.edad=edad

    def presentarmaestro(self):
        print(f'mi nombre es {self.nombre} y mi apellido es {self.apellido} mi carrera es {self.carrera} y mi edad es {self.edad}')
 
class alumno(maestro):
    def __init__(self, nombre,apellido,carrera, edad,semestre,sexo,turno,numerocontrol,prom):
        super().__init__(nombre,apellido)
        self.carrera=carrera
        self.edad=edad
        self.semestre=semestre
        self.sexo=sexo
        self.turno=turno
        self.numerocontrol=numerocontrol
        self.prom=prom

    def presentaralumno(self):
        print(f'mi nombre es {self.nombre} y mi apellido es {self.apellido} mi carrera es {self.carrera} y mi edad es {self.edad} voy en {self.semestre} soy del sexo {self.sexo} del turno {self.turno} mi numero de control es {self.numerocontrol} y mi promedio es {self.prom}')

persona1=persona("erick","maldonado")
persona1.presentar()
 
print("...................................................................")

maestro=maestro("julio","perez","electronica",20)
maestro.presentar()
maestro.presentarmaestro()
