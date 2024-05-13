
# 56
# EL GENERADOR DE CONTRASEÑAS
# /*
# * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# * Podrás configurar generar contraseñas con los siguientes parámetros:
# * - Longitud: Entre 8 y 16.
# * - Con o sin letras mayúsculas.
# * - Con o sin números.
# * - Con o sin símbolos.
# * (Pudiendo combinar todos estos parámetros entre ellos)
# */

from random import randint
import random
import string


def contrasena():

	d = range(1, 9)
	c = []

	for n in d:
		b = random.choices(string.ascii_letters)
		a = [randint(1, 9)]
		b = str(b)
		a = str(a)
		cadena = a + b

		c += cadena
	contrasena1 = ""
	for char in c:
		if char != "" and char != " " and char != "[" and char != "]" and char != "," and char != "'":
			contrasena1 += char

	print(contrasena1)


def main():
	contrasena()


if __name__ == "__main__":
	main()
