"""
#30
ORDENA LA LISTA
/*
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 */
"""
# NO SE PUEDEN USAR FUNCIONES
"""

    
"""


def ordenando(lista: list, parametro: str):

    if parametro == "Asc":
        print(sorted(lista))
    elif parametro == "Desc":
        print(sorted(lista, reverse=True))


if __name__ == "__main__":
    ordenando([0, 2, 5, 9, 3], "Desc")
