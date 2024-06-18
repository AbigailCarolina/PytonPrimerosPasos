import readchar
import os
import random

POS_X = 0   # width
POS_Y = 1   # height
MAP_WIDTH = 10      # ancho X
MAP_HEIGHT = 10     # alto Y

WILD_POKEMONS = 5
VIDA_INICIAL_SQUIRTLE = 30
VIDA_INICIAL_PIKACHU = 30
LIFE_POINTS = 50
EXPERIENCE = 0
TAMANO_BARRA_VIDA = 10

my_position = [1, 3]
trainers = 6
map_trainers = []
map_wild_pokemons = []
medals = ["Agua", "Fuego", "Planta", "Eléctrico", "Roca", "Psíquico"]
vida_squirtle = VIDA_INICIAL_SQUIRTLE
vida_pikachu = VIDA_INICIAL_PIKACHU

while True:
    while len(map_trainers) < trainers:
        new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

        if new_position not in map_trainers and new_position != my_position:
            map_trainers.append(new_position)

    while len(map_wild_pokemons) < WILD_POKEMONS:
        new_position = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

        if new_position not in map_wild_pokemons and new_position != my_position:
            map_wild_pokemons.append(new_position)
# DRAW MAP
    print("+"+"-"*MAP_WIDTH*3+"+")

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

                    map_trainers.remove(object_in_cell)

                elif object_in_cell in map_wild_pokemons:
                    map_wild_pokemons.remove(object_in_cell)

            print("{}".format(char_to_draw), end="")

        print("¦")

    print("+"+"-"*MAP_WIDTH*3+"+")

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
