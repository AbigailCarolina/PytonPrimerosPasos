import random

print("Encuentra al perico \n"
      "------------------- \n"
      "\n"
      "Eres un perrito llamado June, eres suave, bonito y negro; el día de hoy podrías encontrar a un perico par que \n"
      "sea el nuevo integrante de la familia, pero tus decisiones podrían hacer que no lo encuentres, ten cuidado con \n"
      "lo que decides y ayuda a tu familia a encontrarlo. Vives en una casa grande y estás en el patio; andas por ahi \n"
      "caminado cuando ves que alguien te dejo un hueso de carnza, te da curiosidad, lo hueles y ...\n")
carnaza = input("¿Juegas un poco con él? Opción A - Si ------ Opción B - No :\n")

juego_carnaza = False

if carnaza == "A":
    print("Lo muerdes por un rato, vas a tomar agua y después \n")
    juego_carnaza = True

elif carnaza == "B":
        print("Lo ignoras, vas a tomar agua y \n")

else:
    print("No elegiste ni A ni B, así que te duermes y no encuentras al perico.\n")
    exit()

print("te acercas a la puerta, pones la contraseña de la puerta que es \n")
primer_digito = random.randint(1, 10)
segundo_digito = random.randint(1, 10)
contrasena = primer_digito*segundo_digito
resultado = int(input(print("La multiplicación de {} ".format(primer_digito)+"por {}" .format(segundo_digito))))

if contrasena == resultado:
    print("Subes a la habitación de tu dueño, \n")
if contrasena != resultado:
    print("No logras abrir la puerta así que la hermana de tu dueño, te sube a su cuarto, y te duermes, "
          "asi que no encuentras al perico ¡Lo siento perdiste!\n")
    exit()

decision = input("¿Te echas a dormir en sus pies? Opción A - ¿Le lames la cara? Opción B :\n")

if decision == "A":
    print("Se quedan dormidos hasta las 2 p.m., así que cuando bajan tienes toda la energía, "
          "caminas por toda la casa y... encuentras al perico ¡¡Felicidades!!\n")
    exit()

elif decision == "B":
        print("Le lames la cara y como estás mojada se leventa y los dos bajan, abren el zaguan, te sales a la calle \n")
else:
    print("No elegiste ni A ni B, así que te duermes y ¡no encuentras al perico! \n")
    exit()

decision = input("¿Hueles las cacas de los perros de la calle? Si Opción A - No Opción B : \n")

if decision == "B":
    print("avanzas oliendo las casas y todo, hasta que ya no sabes dónde estás y alguien te ve y \n")

    if juego_carnaza == False:
        print("te devuelve a tu casa porque huele mal tu hocico, te pones a caminar en el patio y ¡encuentras al perico!")
    if juego_carnaza == True:
        print("te lleva a su casa y ya no te devuelve asi que no encuentras al perico.")
    exit()

elif decision == "A" :
    print("la mamá de tu dueño, te mete a la casa, en eso \n")

    decision = input("escuchas un ruido ¿vas a revisar qué fue? Si Opción A - No Opción B : \n")
    if decision == "A" :
                print("Encuentras al perico, en hora buena ¡has ganado!\n")
    elif decision == "B":
                print("Te echas y te quedas dormida, lo siento no encuentrás al perico. \n")
    else:
        print("No elegiste ni A ni B, así que te duermes y no encuentras al perico.\n")
        exit()
else:
    print("No elegiste ni A ni B, así que te duermes y no encuentras al perico.\n")
    exit()
exit()


