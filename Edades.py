class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_edad(self, edad):
        self.edad = edad
        
    def get_nombre(self):
        return self.nombre
        
    def get_edad(self):
        return self.edad
    
    def mostrar_persona(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    
    def es_mayor_que(self, otra_persona):
        if self.edad > otra_persona.get_edad():
            return True
        else:
            return False

# Creamos dos objetos Persona
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 17)

# Mostramos los datos de las dos personas
persona1.mostrar_persona()
persona2.mostrar_persona()

#método es_mayor_de_edad
print(f"{persona1.get_nombre()} es mayor de edad: {persona1.es_mayor_de_edad()}")
print(f"{persona2.get_nombre()} es mayor de edad: {persona2.es_mayor_de_edad()}")

#método es_mayor_que
print(f"{persona1.get_nombre()} es mayor que {persona2.get_nombre()}: {persona1.es_mayor_que(persona2)}")
print(f"{persona2.get_nombre()} es mayor que {persona1.get_nombre()}: {persona2.es_mayor_que(persona1)}")

        
    