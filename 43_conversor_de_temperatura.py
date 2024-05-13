"""
#43
CONVERSOR DE TEMPERATURA
/*
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 */


F= 9/5 * C + 32
C = 5/9 * (F -32)

f = 9 / 5 * c + 32
"""


def conversor():
    input_usuario = input("Que valor desea obtener? (C) Celcius o (F) Farenheit: ")

    if input_usuario == "C":
        f = input("Introduzca el valor Farenheit con el simbolo ""º"": ")
        for n in f:
            n = "º"
            if n not in f:
                print("caracter incorrecto")
                exit()
        f = int(f[:-1])
        c = float(5 / 9 * (f - 32))
        c = str(c) + "º"
        print(f"El valor Celcius es {c}")

    elif input_usuario == "F":
        c = input("Introduzca el valor Celcius con el simbolo ""º"": ")
        for n in c:
            n = "º"
            if n not in c:
                print("caracter incorrecto")
                exit()
        c = int(c[:-1])
        f = float(9 / 5 * c + 32)
        f = str(f) + "º"
        print(f"El valor Farenheit es {f}")


def main():
    conversor()


if __name__ == '__main__':
    main()
