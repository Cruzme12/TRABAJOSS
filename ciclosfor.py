import turtle

turtle.shape('turtle')
lados=int(input("escribe el numero de lados de la figura que quieres"))
longuitud=int(input("escribe la longuitud de cada lado"))
numerofiguras=int(input())

for j in range(0,numerofiguras):
  turtle.fillcolor("orange")
  turtle.begin_fill()

  for i in range(0,lados):

     turtle.forward(longuitud)
     turtle.left(360/lados)
     
  turtle.end_fill()
  
  turtle.right(360/numerofiguras)

turtle.exitonclick()
