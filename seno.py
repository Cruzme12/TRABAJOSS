#programa 2 de la materia de analisis numerico
#programa que aproxima f(x)=sin^(x) mediante la serie de Maclaurin
#Calcula los errores e imprime una tabla 
#Autor: Erick dayang cruz maldonado 

from math import log
from math import factorial
from math import exp
print("Aproximar mediante la serie de Maclaurin la funcion f(x)=sin(x)")
x= float(input("ingresa el valor de x: "))
n=int(input("ingresa el valor de n: "))
verdadero=log(x+1)
print("el valor de x %f y el valor verdadero es: %f" %(x,verdadero))
ant=0
i=1
print(" n     verdadero          aproximacion     Et       Ea    ")
while (1):
    if(i>n): break
    serie = ant + (pow(-1,i+1) * pow(x,i))/i
    
    Et=100*(verdadero-serie)/verdadero
    Ea=100*(serie-ant)/serie
    ant= serie
    print(" %d          %f     %f     %f       %f        " %(i,verdadero,serie,Et,Ea))
    i=i+1;   