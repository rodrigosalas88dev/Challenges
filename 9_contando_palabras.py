"""
#9
CONTANDO PALABRAS
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */

25 ÷ 2 = 12 con un residuo de 1
12 ÷ 2 = 6 con un residuo de 0
6 ÷ 2 = 3 con un residuo de 0
3 ÷ 2 = 1 con un residuo de 1
1 ÷ 2 = 0 con un residuo de 1

binario de 25 = 11001

"""

def binario():
    numero = int(input("Elije un numero decimal: "))
    NUMERO_FIJO = numero
    binario_completo = ""
    while numero != 0:
        modulo = int(numero % 2)
        numero = int(numero / 2)

        binario_completo = str(modulo) + binario_completo

    binario_completo = int(binario_completo)
    print(f"El equivalente al numero decimal {NUMERO_FIJO} es el siguiente numero binario: {binario_completo}")


binario()

