from math import pow 
from math import pi
verdadero = pow(pi,4)/90
n = 10000
ant = 0
i = n
print(" n           verdadero    aprox       error et     error ea")
while (1):
    if(i>n): 
        break
    serie = ant + (1/pow(i,4))
    et= 100*(verdadero-serie)/verdadero
    ea=100*(serie-ant)/serie
    ant= serie
    print(" %d          %f     %f     %f    %f   " %(i,verdadero,serie,et,ea))
    i=i-1;    
