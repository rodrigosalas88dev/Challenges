"""
#33
EL SEGUNDO
/*
 * Dado un listado de números, encuentra el SEGUNDO más grande
 */
"""


def el_segundo(*args):
    lista = sorted(args)
    print(lista)
    print(lista[1])


def main():
    el_segundo(7, 38, 24, 20)


if __name__ == '__main__':
    main()
