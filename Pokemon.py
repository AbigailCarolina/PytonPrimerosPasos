import readchar
import os
import random

POS_X = 0  # width
POS_Y = 1  # height
MAP_WIDTH = 10  # ancho X
MAP_HEIGHT = 10  # alto Y

WILD_POKEMONS = 5
VIDA_INICIAL_PIKACHU = 10
VIDA_INICIAL_GYM_POKEMON = 15
VIDA_INICIAL_WILD_POKEMON = 30
LIFE_POINTS = 50
TAMANO_BARRA_VIDA = 10

my_position = [1, 3]
trainers = 6
map_trainers = []
map_wild_pokemons = []

water_pokemon = ["Squirtle", "Wartortle", "Blastoise", "Psyduck", "Golduck", "Poliwag", "Poliwhirl"]
fire_pokemon = ["Charmander", "Charmeleon", "Vulpix", "Ninetales", "Growlithe", "Arcanine"]
grass_pokemon = ["Tangela", "Chikorita", "Bayleef"]
electric_pokemon = ["Electrode", "Electabuzz", "Raichu", "Voltorb", "Jolteon", "Zapdos"]
psychic_pokemon = ["Abra", "Kadabra", "Alakazam", "Slowpoke", "Drowzee", "Hypno", "Mewtwo"]
water_attacks = ["burbuja", "chorro de agua", "hidrobomba", "cascada"]
fire_attacks = ["brasas", "giro de fuego", "lanza llamas", "llamarada", ]
grass_attacks = ["absorción", "danza de pétalos", "esporas", "látigo cepa"]
electric_attacks = ["impactrueno", "onda trueno", "golpe trueno", "rayo"]
psychic_attacks = ["Fuerza Psíquica", "Psicoonda", "Psicorayo", "Hipnosis"]

gym = None
gym_pokemon = None
lista_ataques_gym_pokemon = []
ataque_gym_pokemon = None
medals = ["Agua", "Fuego", "Planta", "Eléctrico", "Psíquico"]

experience = 0
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_gym_pokemon = VIDA_INICIAL_GYM_POKEMON
vida_wild_pokemon = VIDA_INICIAL_WILD_POKEMON

while True:
    while len(map_trainers) < trainers:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_trainers and new_position != my_position:
            map_trainers.append(new_position)

    while len(map_wild_pokemons) < WILD_POKEMONS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_wild_pokemons and new_position != my_position:
            map_wild_pokemons.append(new_position)
    # DRAW MAP
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("¦", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "   "
            object_in_cell = None

            for trainer in map_trainers:
                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = " ♦ "
                    object_in_cell = trainer

            for wild_pokemon in map_wild_pokemons:
                if wild_pokemon[POS_X] == coordinate_x and wild_pokemon[POS_Y] == coordinate_y:
                    char_to_draw = " ◊ "
                    object_in_cell = wild_pokemon


            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @ "

                if object_in_cell in map_trainers:
                    # BATTLE OF GYM
                    os.system("cls")
                    gym = random.choice(medals)
                    if gym == "Agua":
                        gym_pokemon = random.choice(water_pokemon)
                        lista_ataques_gym_pokemon = water_attacks
                    elif gym == "Fuego":
                        gym_pokemon = random.choice(fire_pokemon)
                        lista_ataques_gym_pokemon = fire_attacks
                    elif gym == "Planta":
                        gym_pokemon = random.choice(grass_pokemon)
                        lista_ataques_gym_pokemon = grass_attacks
                    elif gym == "Eléctrico":
                        gym_pokemon = random.choice(electric_pokemon)
                        lista_ataques_gym_pokemon = electric_attacks
                    elif gym == "Psíquico":
                        gym_pokemon = random.choice(psychic_pokemon)
                        lista_ataques_gym_pokemon = psychic_attacks
                    print("======== Gimnasio {} ========\n".format(gym))
                    print("Veo que vienes por la medalla del Gimnasio {}, veamos si lográs vencerme".format(gym))
                    input(print("Enter para continuar...\n"))
                    while vida_pikachu > 0 and vida_gym_pokemon > 0:
                        # TURN GYM POKEMON
                        print("Turno de {}".format(gym_pokemon))
                        ataque_random_gym_pokemon = random.randint(0, 4)
                        # ataque 1
                        if ataque_random_gym_pokemon == 0:
                            ataque_gym_pokemon = lista_ataques_gym_pokemon[0]
                            print("{} ataca con {}\n".format(gym_pokemon, ataque_gym_pokemon))
                            vida_pikachu -= 10
                        # ataque 2
                        elif ataque_random_gym_pokemon == 1:
                            ataque_gym_pokemon = lista_ataques_gym_pokemon[1]
                            print("{} ataca con {}\n".format(gym_pokemon, ataque_gym_pokemon))
                            vida_pikachu -= 11
                        # ataque 3
                        elif ataque_random_gym_pokemon == 2:
                            ataque_gym_pokemon = lista_ataques_gym_pokemon[2]
                            print("{} ataca con {}\n".format(gym_pokemon, ataque_gym_pokemon))
                            vida_pikachu -= 9
                        # ataque 4
                        elif ataque_random_gym_pokemon == 3:
                            ataque_gym_pokemon = lista_ataques_gym_pokemon[3]
                            print("{} ataca con {}\n".format(gym_pokemon, ataque_gym_pokemon))
                            vida_pikachu -= 8
                        # ataque 5
                        elif ataque_random_gym_pokemon == 4:
                            print("{} no atacó\n".format(gym_pokemon))

                        # Barra de vida
                        if vida_pikachu <= 0:
                            vida_pikachu = 0
                        if vida_gym_pokemon <= 0:
                            vida_gym_pokemon = 0

                        puntos_pikachu = int((vida_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU)
                        puntos_gym_pokemon = int((vida_gym_pokemon * TAMANO_BARRA_VIDA) / VIDA_INICIAL_GYM_POKEMON)

                        print("Pikachu  {} [{}{}] {} \n".format(vida_pikachu, puntos_pikachu * "#",
                                                                (TAMANO_BARRA_VIDA - puntos_pikachu) * "-",
                                                                VIDA_INICIAL_PIKACHU))
                        print("{} {} [{}{}] {}\n".format(gym_pokemon, vida_gym_pokemon, puntos_gym_pokemon * "#",
                                                         (TAMANO_BARRA_VIDA - puntos_gym_pokemon) * "-",
                                                         VIDA_INICIAL_GYM_POKEMON))
                        input(print("\n Enter para continuar...\n"))
                        os.system("cls")

                    if vida_pikachu > 0 and vida_gym_pokemon > 0:
                        # TURN OF PIKACHU
                        print("Turno de Pikachu")
                        ataque_pikachu = None
                        while ataque_pikachu != "j" and ataque_pikachu != "k" and ataque_pikachu != "l":
                            ataque_pikachu = input(
                                "Elige un ataque: (l) bola voltio, (j) onda trueno, (k) rayo (i) No atacar \n")

                            # ataque bola voltio
                            if ataque_pikachu == "l":
                                print("Pikachu ataca con bola voltio")
                                vida_gym_pokemon -= 10
                            # ataque onda trueno
                            elif ataque_pikachu == "j":
                                print("Pikachu ataca con onda trueno")
                                vida_gym_pokemon -= 12
                            # ataque rayo
                            elif ataque_pikachu == "k":
                                print("Pikachu ataca con rayo")
                                vida_gym_pokemon -= 9
                            # no atacar
                            elif ataque_pikachu == "i":
                                print("Pikachu no ataca")

                            # Barras de vida
                            if vida_pikachu <= 0:
                                vida_pikachu = 0
                            if vida_gym_pokemon <= 0:
                                vida_gym_pokemon = 0

                            puntos_pikachu = int((vida_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU)
                            puntos_gym_pokemon = int(
                                (vida_gym_pokemon * TAMANO_BARRA_VIDA) / VIDA_INICIAL_GYM_POKEMON)

                            print("Pikachu  {} [{}{}] {} \n".format(vida_pikachu, puntos_pikachu * "#",
                                                                    (TAMANO_BARRA_VIDA - puntos_pikachu) * "-",
                                                                    VIDA_INICIAL_PIKACHU))
                            print(
                                "{} {} [{}{}] {}\n".format(gym_pokemon, vida_gym_pokemon, puntos_gym_pokemon * "#",
                                                           (TAMANO_BARRA_VIDA - puntos_gym_pokemon) * "-",
                                                           VIDA_INICIAL_GYM_POKEMON))
                            input(print("Enter para continuar...\n"))
                            os.system("cls")
                    elif vida_pikachu > vida_gym_pokemon or vida_gym_pokemon == 0:
                        print("Pikachu gana")
                        map_trainers.remove(object_in_cell)
                        trainers -= 1
                        medals.remove(gym)
                        print("----- Has ganado la medalla {} -----".format(gym))
                    elif vida_pikachu == 0:
                        print("----- {} gana ----- ".format(gym_pokemon))
                        experience += 1
                        print("----- Suerte para la próxima -----")
                        os.system("cls")

                            # BATTLE OF WILD POKÉMON
                elif object_in_cell in map_wild_pokemons:
                    os.system("cls")
                    wild_pokemon = random.choice(
                        water_pokemon or fire_pokemon or grass_pokemon or electric_pokemon or psychic_pokemon)
                    print("======== {} pokémon salvaje ========\n".format(wild_pokemon))
                    print("{} está listo para atacar, ¿lo lográs vencer?".format(wild_pokemon))
                    input(print("Enter para continuar...\n"))
                    while vida_pikachu >= 0 and vida_wild_pokemon >= 0:

                        # TURN OF WILD POKEMON
                        print("Turno de {}".format(wild_pokemon))
                        if wild_pokemon in water_pokemon:
                            type_attack = water_attacks
                        elif wild_pokemon in fire_pokemon:
                            type_attack = fire_attacks
                        elif wild_pokemon in grass_pokemon:
                            type_attack = grass_attacks
                        elif wild_pokemon in electric_pokemon:
                            type_attack = electric_attacks
                        elif wild_pokemon in psychic_pokemon:
                            type_attack = psychic_attacks

                        ataque_wild_pokemon = random.randint(0, 4)

                        # attack wild pokemon
                        if ataque_wild_pokemon == 0:
                            attack_wild_pokemon = type_attack[0]
                            print("{} ataca con {} \n".format(wild_pokemon, attack_wild_pokemon))
                            vida_pikachu -= 10
                        elif ataque_wild_pokemon == 1:
                            attack_wild_pokemon = type_attack[1]
                            print("{} ataca con {} \n".format(wild_pokemon, attack_wild_pokemon))
                            vida_pikachu -= 11
                        elif ataque_wild_pokemon == 2:
                            attack_wild_pokemon = type_attack[2]
                            print("{} ataca con {} \n".format(wild_pokemon, attack_wild_pokemon))
                            vida_pikachu -= 12
                        elif ataque_wild_pokemon == 3:
                            attack_wild_pokemon = type_attack[3]
                            print("{} ataca con {} \n".format(wild_pokemon, attack_wild_pokemon))
                            vida_pikachu -= 13
                        elif ataque_wild_pokemon == 4:
                            print("{} no atacó".format(wild_pokemon))

                        puntos_pikachu = int((vida_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU)
                        puntos_wild_pokemon = int((vida_wild_pokemon * TAMANO_BARRA_VIDA) / VIDA_INICIAL_WILD_POKEMON)

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        if vida_wild_pokemon < 0:
                            vida_wild_pokemon = 0

                        print("Pikachu  {} [{}{}] {} \n".format(vida_pikachu, puntos_pikachu * "#",
                                                                (TAMANO_BARRA_VIDA - puntos_pikachu) * "-",
                                                                VIDA_INICIAL_PIKACHU))
                        print("{} {} [{}{}] {}\n".format(wild_pokemon, vida_wild_pokemon, puntos_wild_pokemon * "#",
                                                         (TAMANO_BARRA_VIDA - puntos_wild_pokemon) * "-",
                                                         VIDA_INICIAL_WILD_POKEMON))
                        input(print("Enter para continuar...\n\n"))


                        # TURN OF PIKACHU
                        print("Turno de Pikachu")
                        ataque_pikachu = None
                        while ataque_pikachu != "j" and ataque_pikachu != "k" and ataque_pikachu != "l":
                            ataque_pikachu = input(
                                "Elige un ataque: (l) bola voltio, (j) onda trueno, (k) rayo o (i) No atacar \n")
                            # ataque bola voltio
                            if ataque_pikachu == "l":
                                print("Pikachu ataca con bola voltio")
                                vida_wild_pokemon -= 10
                            # ataque onda trueno
                            elif ataque_pikachu == "j":
                                print("Pikachu ataca con onda trueno")
                                vida_wild_pokemon -= 12
                            # ataque rayo
                            elif ataque_pikachu == "k":
                                print("Pikachu ataca con rayo")
                                vida_wild_pokemon -= 9
                            # no atacar
                            elif ataque_pikachu == "i":
                                print("Pikachu no ataca")

                            puntos_pikachu = int((vida_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU)
                            puntos_wild_pokemon = int((vida_wild_pokemon * TAMANO_BARRA_VIDA) / VIDA_INICIAL_WILD_POKEMON)

                            if vida_pikachu < 0:
                                vida_pikachu = 0
                            if vida_wild_pokemon < 0:
                                vida_wild_pokemon = 0

                            print("Pikachu  {} [{}{}] {} \n".format(vida_pikachu, puntos_pikachu * "#",
                                                                    (TAMANO_BARRA_VIDA - puntos_pikachu) * "-",
                                                                    VIDA_INICIAL_PIKACHU))
                            print("{} {} [{}{}] {}\n".format(wild_pokemon, vida_wild_pokemon, puntos_wild_pokemon * "#",
                                                             (TAMANO_BARRA_VIDA - puntos_wild_pokemon) * "-",
                                                             VIDA_INICIAL_WILD_POKEMON))
                            input(print("Enter para continuar...\n\n"))
                            os.system("cls")

                    if vida_pikachu < vida_wild_pokemon:
                        print("========== {} gana ==========".format(wild_pokemon))
                        experience += 1
                        os.system("cls")
                    else:
                        print("========== Pikachu gana ==========")
                        map_wild_pokemons.remove(object_in_cell)
                        experience += 2
                        os.system("cls")
            # todo Tal vez estaría bien que no se desaparecieran los pokemons salvajes del all pero hay que ver al final del juego
            print("{}".format(char_to_draw), end="")

        print("¦")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # MOVE IN THE MAP WASD
    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break
    os.system("cls")
