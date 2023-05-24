import random
numeroSecreto = random.randint(1, 10)
print("Bienvenido al número secreto")
print("Intenta adivinar el número del 1 al 10 que estoy pensando")
numeroPropuesto=int(input("¿Cuál número crees que es? "))

if numeroPropuesto < 1:
    print("Debes elegir un número mayor a 1")
if numeroPropuesto > 10:
    print("Debes elegir un número menor a 10")
if numeroSecreto == numeroPropuesto:
    print("Que suerte el número secreto es: {}".format(numeroSecreto))
if numeroSecreto != numeroPropuesto:
    print("Buena suerte a la próxima el número es: {}".format(numeroSecreto))