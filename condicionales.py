import turtle

turtle.shape("turtle")

continuar = input("bienvenido al graficador. presiona si para graficar y no para terminarlo")
contador=0
while continuar =="si":
 print('''Bienvenido al graficador.
selecciona la opcion a graficar
1) Triangulo
2) Cuadrado
3) Pentagono''')

 opcion=int(input())


 if opcion == 1:
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    
    
 elif opcion == 2:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

 elif opcion == 3:
    turtle.forward(100)
    turtle.left(75)
    turtle.forward(100)
    turtle.left(75)
    turtle.forward(100)
    turtle.left(75)
    turtle.forward(100)
    turtle.left(75)
    turtle.forward(100)
    turtle.left(75)
    
 else:
    print("programa terminado")
    print("calaverita") 

contador+=1
print("programa terminado")
continuar=input("bienvenido al graficador. presiona si para graficar y no para terminarlo")
print("programa terminado")
turtle.exitonclick()