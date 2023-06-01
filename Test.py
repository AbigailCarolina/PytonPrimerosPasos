titulo = "Bienvenido al test qué mascota eres"
print(titulo+"\n"+"-"*len(titulo)+"\n")
puntuacion = 0
opcion = input("1.¿Dónde te gusta dormir?\n"
         "a)Cualquier lugar es bueno\n"
         "b)Solo en mi cama\n"
         "c)En cualquier lugar siempre y cuando este con alguien\n")
if opcion == "a":
    puntuacion += 15
elif opcion == "b":
    puntuacion += 10
elif opcion == "c":
    puntuacion += 5
else: print("Esa no es una opción ¬¬")

opcion = input("2.¿A la hora de comer?\n"
         "a)Te gusta que haya postre y si es comida casera mejor\n"
         "b)No hay problema si no es a tu hora, total algún día comerás\n"
         "c)Me enojo si no es a mi hora\n")
if opcion == "a":
    puntuacion += 15
elif opcion == "b":
    puntuacion += 10
elif opcion == "c":
    puntuacion += 5
else: print("Esa no es una opción ¬¬")

opcion = input("3.¿Para tomar que prefieres?\n"
         "a)Lo que sea es bueno\n"
         "b)Agüita de sabor\n"
         "c)Agua simple\n")

if opcion == "a":
    puntuacion += 15
elif opcion == "b":
    puntuacion += 10
elif opcion == "c":
    puntuacion += 5
else: print("Esa no es una opción ¬¬")

if puntuacion >35:
    print("Todos en el barrio te respetan, te pareces al Bucket")
elif (25<= puntuacion >= 35):
    print("No traes nada, te falta barrio, te pareces al June")
elif puntuacion < 26  :
    print("Eres el más shavo del barrio, te pareces al Gato Shavo")
elif puntuacion == 30 :
    print("En el barrio todos te han vistó pero no saben quien eres, te pareces al Messi")
exit()