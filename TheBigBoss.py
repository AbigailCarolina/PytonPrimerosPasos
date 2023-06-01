import random

print("The big boss \n"
      "------------- \n"
      "\n"
      "Eres un perrito te dicen June y estás todo menso, pero suave y bonito, bueno no tan bonito porque eres negro "
      "y te apesta el hocico; un día te despiertas y por ahí ves que alguien te dejo un hueso de carnaza,"
      " te da curiosidad, lo hueles y ...\n")
carnaza = input ("¿Juegas un poco con él? Opción A - Si ------ Opción B - No :\n")

jugo_carnaza= False

if carnaza == "A":
    print("Lo muerdes por un rato, vas a tomar agüita de sabor y después")
elif carnaza == "a":
    print("Lo muerdes por un rato, vas a tomar agüita de sabor y después")
elif carnaza == "B":
    print("Lo ignoras, vas a tomar agüita de sabor y")
elif carnaza == "b":
    print("Lo ignoras, vas a tomar agüita de sabor y")
else:
    print ("No elegiste ni A ni B, así que te duermes")


print("Te acercas a la puerta, pones la contraseña de la puerta que es")
contrasena=0
primer_digito = random.randint (1,10)
segundo_digito = random.randint (1,10)

resultado = input (print ("La multiplicación de {} ".format(primer_digito)+"por {}" .format(segundo_digito)))


