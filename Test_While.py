from random import randint
import os

VIDA_INICIAL_PIKACHU = 30
VIDA_INICIAL_SQUIRTLE = 30

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

TAMANO_BARRA_VIDA = 10


while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos del duelo

    # Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 3)
    # ataque bola voltio
    if ataque_pikachu == 1:
        print("Pikachu ataca con bola voltio \n")
        vida_squirtle -= 10
    # ataque onda trueno
    elif ataque_pikachu == 2:
        print("Pikachu ataca con onda trueno \n")
        vida_squirtle -= 11
    elif ataque_pikachu == 3:
        print("Pikachu no atacó")

    puntos_pikachu = int((vida_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU)
    puntos_squirtle = int((vida_squirtle * TAMANO_BARRA_VIDA) / VIDA_INICIAL_SQUIRTLE)

    if vida_pikachu < 0:
        vida_pikachu = 0
    if vida_squirtle < 0:
        vida_squirtle = 0

    print("Pikachu  {} [{}{}] {} \n".format(vida_pikachu, puntos_pikachu*"#",
                                            (TAMANO_BARRA_VIDA-puntos_pikachu)*"-", VIDA_INICIAL_PIKACHU))
    print("Squirtle {} [{}{}] {}\n".format(vida_squirtle, puntos_squirtle*"#",
                                           (TAMANO_BARRA_VIDA-puntos_squirtle)*"-", VIDA_INICIAL_SQUIRTLE))
    input(print("Enter para continuar...\n\n"))
    os.system("cls")

# Turno Squirtle

    print("Turno de Squirtle")
    ataque_squirtle = None
    while ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "P":
        ataque_squirtle = input("Elige un ataque: (P) Placaje, (A) Pistola de Agua, (B) Burbujas o (N) No atacar \n")

# ataque placaje
    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
# ataque pistola de agua
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de agua")
        vida_pikachu -= 12
# ataque burbujas
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbujas")
        vida_pikachu -= 9
# no atacar
    elif ataque_squirtle == "N":
        print("Squirtle no ataca")
    
    if vida_pikachu < 0:
        vida_pikachu = 0
    if vida_squirtle < 0:
        vida_squirtle = 0

    puntos_pikachu = int((vida_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU)
    puntos_squirtle = int((vida_squirtle * TAMANO_BARRA_VIDA) / VIDA_INICIAL_SQUIRTLE)

    print("Pikachu:  {} [{}{}] {} \n".format(vida_pikachu, puntos_pikachu * "#",
                                             (TAMANO_BARRA_VIDA - puntos_pikachu) * "-", VIDA_INICIAL_PIKACHU))
    print("Squirtle: {} [{}{}] {} \n".format(vida_squirtle, puntos_squirtle * "#",
                                             (TAMANO_BARRA_VIDA - puntos_squirtle) * "-", VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...")
    os.system("cls")


if vida_pikachu > vida_squirtle:
        print("Pikachu gana")
else:
        print("Squirtle gana")
