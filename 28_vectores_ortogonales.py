"""
#28
VECTORES ORTOGONALES
/*
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 */

a1 = a1, a2
b1 = b1, b2
a * b = a1 * b1 + a2 * b2 = 0

v1 * v2 =
"""


def vectores_ortogonales(arg1, arg2):
    if arg1[0] * arg2[0] + arg1[1] * arg2[1] == 0:
        print("Estos son vectores ortogonales")
    if arg1[0] * arg2[0] + arg1[1] * arg2[1] != 0:
        print("Estos no son vectores ortogonales")


if __name__ == "__main__":
    vectores_ortogonales([0, 2, 5], [3, 0, 8])
