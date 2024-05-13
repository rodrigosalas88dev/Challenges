# 53
# EL FAMOSO "FIZZ BUZZ" (v2)
# /*
# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# */

from random import randint

def fizz():
	a = range(1, 101)

	for n in a:
		if n % 3 == 0 and n % 5 == 0:
			print(n, "fizzbuzz")
		if n % 3 == 0:
			print(n, "fizz")
		elif n % 5 == 0:
			print(n, "buzz")
		else:
			print(n)



def main():
	fizz()



if __name__ == "__main__":
	main()
