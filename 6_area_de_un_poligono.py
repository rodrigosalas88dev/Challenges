"""
#5
ÁREA DE UN POLÍGONO
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

# TRIANGULO: BASE X ALTURA / 2 = (a x b) / 2
# CUADRADO: LADO X LADO = a x b
# RECTANGULO: BASE X ALTURA = a x b


def area_poligono():

    while True:

        poligono = input("Elige un poligono para calcular su area: triangulo, cuadrado, rectangulo / (Q) para salir ")

        if poligono == "Q":
            break

        elif poligono != "Q":
            if poligono == "triangulo":
                a = float(input("introduce la base en CM: "))
                b = float(input("introduce la altura en CM: "))
                area = float((a * b) / 2)
                print(f"El area de este {poligono} es: {area} CM")

            elif poligono == "cuadrado":
                a = float(input("introduce un lado en CM: "))
                area = float(a * a)
                print(f"El área de este {poligono} es: {area} CM")

            elif poligono == "rectangulo":
                a = float(input("introduce la base en CM: "))
                b = float(input("introduce la altura en CM: "))
                area = float(a * b)
                print(f"El área de este {poligono} es: {area} CM")

            else:
                print("Introduccion incorrecta")
                pass


if __name__ == "__main__":
    area_poligono()
