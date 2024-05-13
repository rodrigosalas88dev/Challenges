"""
#62
HETEROGRAMA, ISOGRAMA Y PANGRAMA
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
"""

import string


def heterograma(texto):
	texto = texto.replace(" ", "")
	contador = 0

	for n in texto:
		contador = texto.count(n)

		if contador >= 2:
			break
	if contador == 1:
		print("Es heterograma")

	isograma(contador)
	panagrama(texto)
	return texto


def isograma(contador):

	if contador >= 2:
		print("Es isograma")


def panagrama(texto):
	texto = texto.replace(" ", "")
	char = string.ascii_lowercase
	on_off = None
	for n in char:
		if n not in texto:
			print("No es panagrama")
			break
	else:
		print("Es panagrama")


def main():
	heterograma("Rodrigo Salas Delgado")


if __name__ == "__main__":
	main()
