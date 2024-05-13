# 67
# OCTAL Y HEXADECIMAL
# /*
# * Crea una función que reciba un número decimal y lo trasforme a Octal
# * y Hexadecimal.
# * - No está permitido usar funciones propias del lenguaje de programación que
# * realicen esas operaciones directamente.
# */
"""
¿Cómo saber si es un número octal?
Decimal. Para poder convertir un número en base decimal a base octal se divide dicho número entre 8,
dejando el residuo y dividiendo el cociente sucesivamente entre 8
hasta obtener cociente 0, luego los restos de las divisiones leídos en
orden inverso indican el número en octal.
"""


def octal(numero):
	octal = ""
	while numero > 0:
		restos = numero % 8
		octal = str(restos) + octal
		numero = numero // 8

	print(f"El numero en octal es: {octal}")


def hexadecimal(numero):
	hexadecimal = ""
	while numero > 0:
		restos = numero % 16

		if restos == 10:
			restos = "A"
		if restos == 11:
			restos = "B"
		if restos == 12:
			restos = "C"
		if restos == 13:
			restos = "D"
		if restos == 14:
			restos = "E"
		if restos == 15:
			restos = "F"

		hexadecimal = str(restos) + hexadecimal
		numero = numero // 16

	print(f"El numero en hexadecimal es: {hexadecimal}")


def main():
	octal(100)
	hexadecimal(100)


if __name__ == "__main__":
	main()
