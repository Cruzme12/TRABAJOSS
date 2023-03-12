'''
def nombrefuncion(par1, par2,...,parN):
#codigo
suma=par1+par2...
pass
'''
def suma(lista):
    resul= sum(lista)
    return resul

def resta(numa,numb):
    resul=numa-numb
    return resul

listaNumeros = []

limite = int(input())

for i in range(0,limite):
    numeros=int(input('dame el sumando'))
    listaNumeros.append(numeros)
        
print(suma(listaNumeros))




