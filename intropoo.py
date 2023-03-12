#clase Padre
class NombreClasePadre:        #aquí se hace la clase nueva.
    pass

#clase Hijo

class NombreClaseHijo(NombreClasePadre):        #aquí se hace la clase nueva.
    pass


objeto= NombreClasePadre()     #aquí se hace un objeto nuevo.

objetonuevo = NombreClaseHijo() #aqui se hace el objeto hijo con las caracteristicas del objeto padre

#herencia