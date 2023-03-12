respuesta="si"
lista=[]
while respuesta=="si":
    calificacion=int(input("ingresa la calificacion del alumno:"))
    lista.append(calificacion)


    respuesta=input("presiona si para seguir agragando calificaciones:")

    
print(lista)

prom=sum(lista)/len(lista)
print(f'el promedio general del grupo es {prom}')