# 66
# ADIVINA LA PALABRA
# /*
# * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
# * - El juego comienza proponiendo una palabra aleatoria incompleta
# *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
# * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
# *   la palabra a adivinar)
# *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
# *     uno al número de intentos
# *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
# *     al número de intentos
# *   - Si el contador de intentos llega a 0, el jugador pierde
# * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
# *   ocultando más del 60%
# * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
# */


#--------------------------------FALTA REMPLAZAR EL _ POR LA LETRA CORRESPONDIENTE------------------------
import random
from random import randint
from string import ascii_letters


def adivina(texto):
	intentos = 3
	rand = random.choice(texto)
	rand2 = random.choice(texto)
	rand3 = random.choice(texto)
	texto_incompleto = texto.replace(rand, "_")
	print(texto_incompleto)
	texto_incompleto2 = texto_incompleto.replace(rand2, "_")
	print(texto_incompleto2)
	texto_incompleto3 = texto_incompleto2.replace(rand3, "_")
	print(texto_incompleto3)
	input_usuario = None

	while input_usuario != "Q" and intentos >= 1:

		input_usuario = input(f"La palabra a adivinar es {texto_incompleto3}. Adivina una palabra o una letra, tienes {intentos} intentos) / (Q) para salir:  ")

		if input_usuario == texto:
			print(f"Adivinaste! Intentos: {intentos}")
			break
		# --------------------------------FALTA REMPLAZAR EL _ POR LA LETRA CORRESPONDIENTE------------------------
		elif input_usuario == rand:

			texto_incompleto3 = texto_incompleto.replace("_", input_usuario)

			if texto == texto_incompleto3:
				print(f"Adivinaste! Palabra completada! Intentos: {intentos}")
				break
			elif texto != texto_incompleto3:
				print(f"Adivinaste! Letra completada! Intentos: {intentos}")
				pass

		elif input_usuario == rand2:

			texto_incompleto3 = texto_incompleto2.replace("_", input_usuario)

			if texto == texto_incompleto3:
				print(f"Adivinaste! Palabra completada! Intentos: {intentos}")
				break
			elif texto != texto_incompleto3:
				print(f"Adivinaste! Letra completada! Intentos: {intentos}")
				pass

		elif input_usuario == rand3:

			texto_incompleto3 = texto_incompleto3.replace("_", input_usuario)

			if texto == texto_incompleto3:
				print(f"Adivinaste! Palabra completada! Intentos: {intentos}")
				break
			elif texto != texto_incompleto3:
				print(f"Adivinaste! Letra completada! Intentos: {intentos}")
				pass

		elif input_usuario != rand or input_usuario != rand2 or input_usuario != rand3:
			intentos -= 1
			print(f"No adivinaste! Intentos: {intentos}")
			if intentos == 0:
				print("Te quedaste sin intentos! Has perdido!")
				break
			else:
				pass


def main():
	adivina("Rodrigo salas")


if __name__ == "__main__":
	main()
