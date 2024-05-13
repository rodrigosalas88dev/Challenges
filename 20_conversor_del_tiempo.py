"""
#20
CONVERSOR TIEMPO
/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */
"""


def conversor(dia, hora, minuto, segundo):
    dia = int(dia) * 86400000
    hora = int(hora) * 3600000
    minuto = int(minuto) * 60000
    segundo = int(segundo) * 1000
    total_milisegundos = dia + hora + minuto + segundo
    print(total_milisegundos)


if __name__ == "__main__":
    conversor(0, 0, 0, 0)
