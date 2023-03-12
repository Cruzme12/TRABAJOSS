class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock
    
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
        
    def getStock(self):
        return self.stock
    
    def calcularEnvio(self, peso=9):
        if peso > 10:
            costo_envio = 10.0  # Costo fijo para paquetes pesados
        else:
            costo_envio = peso * 1.5  # Costo por kilo de peso
        
        return costo_envio
    
    def setPrecio(self):
        clave = input("ingrese la contraseña para aceptar los precios:")
        if clave == "1234":
            precio= int(input())
            self.__precio = precio
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
    
    def mostarFisico(self):
        print(f'Articulo: {self.nombre} precio: {self.__precio} En stock: {self.stock}')
    

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, stock, tamano, plataforma):
        super().__init__(nombre, precio, stock)
        self.tamano = tamano
        self.plataforma = plataforma
        self.__precio=precio
    
    def getTamano(self):
        return self.tamano
    
    def getPlataforma(self):
        return self.plataforma
    
    def calcularEnvio(self):
            return 0.0  # El envío es gratuito para productos digitales
            
    def mostarDigital(self):
        print(f'Articulo: {self.nombre} precio: {self.__precio} En stock: {self.stock} Tamano: {self.tamano} Plataforma: {self.plataforma} ')



# PRODUCTOS FISICOS
producto1 = Producto("Camiseta", 30, 10)
producto1.mostarFisico()

producto2 = Producto("Pantalón", 40, 5)
producto3 = Producto("Zapatos", 60, 2)
producto1.setPrecio()


producto1.mostarFisico() 
producto2.mostarFisico()
producto3.mostarFisico()


print("El costo del envio es:",producto1.calcularEnvio())
print("El costo del envio es:",producto2.calcularEnvio())
print("El costo del envio es:",producto3.calcularEnvio())

# PRODUCTOS DIGITALES
producto4 = ProductoDigital("Libro electrónico", 10, 100, "2 MB", "Kindle")
producto5 = ProductoDigital("Juego MARIO KART", 20, 50, "5 GB", "NINTENDO SWITCH")

producto4.mostarDigital()
producto5.mostarDigital()
print("El costo del envio es:",producto4.calcularEnvio())
print("El costo del envio es:",producto5.calcularEnvio())




