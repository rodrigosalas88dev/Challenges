"""
#15
¿ES UN NÚMERO DE ARMSTRONG?
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */

1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

"""


def armstrong(numero):
    digitos = [int(digito) for digito in str(numero)]
    elevado = 0
    numero_elevado = 0

    for digito in digitos:
        elevado += 1

    for digito in digitos:
        numero_elevado = int(digito) ** elevado + numero_elevado
    print(numero_elevado)
    if numero_elevado == numero:
        print("Este es un numero Armstrong")
    else:
        print("Este no es un numero Armstrong")


if __name__ == "__main__":
    armstrong(153)

