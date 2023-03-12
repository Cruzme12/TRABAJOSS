#programa 1 de la materia de analisis numerico
#programa que aproxima f(x)=e^(x) mediante la serie de Maclaurin
#Calcula los errores e imprime una tabla 
#Autor: Ing. Jose Guadalupe Espejel Panigua 

from math import factorial 
from math import log
print("Aproximar mediante la serie de Maclaurin la funcion f(x)=e^(x)")
x= float(input("ingresa el valor de x: "))
n=int(input("ingresa el valor de n: "))
verdadero=log(1+x)
print("el valor de x %f y el valor verdadero es: %f" %(x,verdadero))
ant=0
i=0
print(" n     verdadero        aprox         error et         error ea")
while (1):
    if(i>n): break
    serie = ant + pow(x,i)/(factorial(i))
    et= 100*(verdadero-serie)/verdadero
    ea=100*(serie-ant)/serie
    ant= serie
    print(" %d          %f     %f     %f    %f   " %(i,verdadero,serie,et,ea))
    i=i+1;    