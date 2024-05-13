"""
#14
FACTORIAL RECURSIVO
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

# FACTORIAL DE 5
# 1    *    1
# 2    *    2       1 * 1 = 1 * 2 = 2 * 3 = 6 * 4 = 24 * 5 = 120
# 3    *    6           .       .       .       .        .
# 4    *    24
# 5    *    120     5! = 5x4x3x2x1 = 120

# f = n ( n − 1 )

# n = n * (n - 1) * (n - 1)

"""
def factorial(numero):  # metodo 1
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


print(factorial(5))
"""


def factorial1(numero):  # metodo 2
    f = 1
    for n in range(1, numero + 1):
        f *= n
        print(f)
    return f


factorial1(5)
