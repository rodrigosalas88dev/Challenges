# /*
# * Crea una función que sea capaz de encriptar y desencriptar texto
# * utilizando el algoritmo de encriptación de Karaca
# * (debes buscar información sobre él).
# */

def karaca(texto):
	texto_reves = ""
	a = "a"
	e = "e"
	i = "i"
	o = "o"
	u = "u"

	for char in texto:
		texto_reves = char + texto_reves

	for char in texto_reves:

		if char == a:
			texto_reves = texto_reves.replace(char, "O")
		if char == e:
			texto_reves = texto_reves.replace(char, "1")
		if char == i:
			texto_reves = texto_reves.replace(char, "2")
		if char == o:
			texto_reves = texto_reves.replace(char, "2")
		if char == u:
			texto_reves = texto_reves.replace(char, "3")

	print(texto_reves)
	texto_reves = texto_reves + "aca"
	print(texto_reves)


def main():
	karaca("rodrigo salas delgado")


if __name__ == "__main__":
	main()
