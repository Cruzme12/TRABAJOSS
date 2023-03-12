#programa 1 de la materia de analisis numerico
#programa que aproxima f(x)=cos^(x) mediante la serie de Maclaurin
#Calcula los errores e imprime una tabla 
#Autor: Erick dayang cruz maldonado

from math import cos
from math import factorial
print("Aproximar mediante la serie de Maclaurin la funcion f(x)=cos(x)")
x= float(input("ingresa el valor de x: "))
n=int(input("ingresa el valor de n: "))
verdadero=cos(x)
print("el valor de x %f y el valor verdadero es: %f" %(x,verdadero))
ant=0
i=0
print(" n     verdadero        termino         aproximacion     Et       Ea    ")
while (1):
    if(i>n): break
    serie = ant + pow(-1,i) * pow(x,(2*i))/(factorial((2*i)))
    term=pow(-1,i) * pow(x,(2*i))/(factorial(2*i))
    Et=100*(verdadero-serie)/verdadero
    Ea=100*(serie-ant)/serie
    ant= serie
    print(" %d          %f     %f     %f       %f       %f " %(i,verdadero,term,serie,Et,Ea))
    i=i+1;    