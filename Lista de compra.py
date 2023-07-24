print("Lista de compra")
lista_de_compra = []
articulo_compra = None
carrito = lista_de_compra

while articulo_compra != "Q":
    articulo_compra = input("¿Qué deseas comprar? ([Q] para salir)")

    lista_de_compra.append(articulo_compra)
    while carrito != "S" and carrito != "N":
        carrito = input(print("Seguro que quieres comrar {} [S] para añadir al carrito [N] para omitir"
                              .format(articulo_compra)))
    if carrito == "S":
        print("{} ha sido añadido a la lista de compra. \n".format(articulo_compra))

    elif carrito == "N":
        lista_de_compra.pop()
        print(lista_de_compra)

if articulo_compra in lista_de_compra:
    print("{} ya ha sido agregado a la lista de compra con anterioridad")

print("La lista de compra es {}, ¡Hasta pronto!".format(lista_de_compra))
