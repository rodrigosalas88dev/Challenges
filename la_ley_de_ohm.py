"""
#42
LA LEY DE OHM
/*
 * Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
 */

 V=I×R
V es la diferencia de potencial en voltios (V).
I es la corriente eléctrica en amperios (A).
R es la resistencia eléctrica en ohmios (R)

"""

def ley_ohm():

    while True:
        v = input("Introduce el valor del potencial en Voltios / (x) valor a calcular: ")
        i = input("Introduce el valor de la corriente electrica en Amperios / (x) valor a calcular: ")
        r = input("Introduce el valor de la resistencia electrica en Ohmios / (x) valor a calcular: ")

        if v != "x" and i != "x" and r != "x":
            print("Invalid values")
        else:
            if v == "x":
                v = float(i) * float(r)
                v = int(v)
            print(f"El valor del potencial en Voltios es: {v}")
            if i == "x":
                i = float(v) / float(r)
                i = int(i)
            print(f"El valor del potencial de la corriente electrica en Amperios es: {i}")
            if r == "x":
                r = float(v) / float(i)
                r = int(r)
            print(f"El valor del potencial de la resistencia electrica en Ohmios es: {r}")
            break

def main():
    ley_ohm()


if __name__ == '__main__':
    main()
