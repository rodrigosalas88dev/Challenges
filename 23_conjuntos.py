"""
#23
CONJUNTOS
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""


def conjuntos(arg1, arg2, boolean):
    if boolean:
        for char in arg1:
            if char == char in arg2:
                print(char)

    if not boolean:
        for char in arg1:
            if char == char not in arg2:
                print(char)
        for char in arg2:
            if char == char not in arg1:
                print(char)




if __name__ == "__main__":
    conjuntos([1, "hola", 3, 54, "besos"], ["a", 3, "besos", 2, 35, 54], True)
