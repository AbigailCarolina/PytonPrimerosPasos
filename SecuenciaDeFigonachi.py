def tres(lista):
    m = (len(lista))-1
    e = len(lista) - 2
    c = lista[e]+lista[m]
    if c <= 1000:
        dos(c, lista)


def dos(c, lista):
    lista.append(c)
    tres(lista)


def uno(lista):
    if lista:
        print("entro al if de uno")
        tres(lista)
    else:
        lista = [0]
        c = lista[0]+1

    print(lista)
    if c <= 100:
        dos(c, lista)


def main():
    uno([0, 1, 1])


if __name__ == "__main__":
    main()
