
#abstraccion 
class Pilares:
    #propiedades/atributos 
    nombre=" "
    edad = 18
    espada="Normal"
    estatura=1.6
    respiracion="normal"
    postura=" "


    #Metodos 
    def ataque(self):
        print("ataque")

    def defensa(self):
        print("defendiendo")

#se crea el objeto a partir de la clase
personajemizunoto=Pilares()
personajemizunoto.nombre="pips"

print(f'el personaje {personajemizunoto.nombre}, tiene {personajemizunoto.edad} años y su respiracion es {personajemizunoto.respiracion}')

kibutzuji=input("¿está cerca el enemigo?")
if kibutzuji=="sí":
    personajemizunoto.ataque()

else:
  personajemizunoto.defensa()


personajetsuguko=Pilares()
personajetsuguko.nombre="kanao"

print(f'el personaje {personajetsuguko.nombre}, tiene {personajetsuguko.edad} años y su respiracion es {personajetsuguko.respiracion}')

kibutzuji=input("¿está cerca el enemigo?")
if kibutzuji=="sí":
    personajetsuguko.ataque()

else:
  personajetsuguko.defensa()
