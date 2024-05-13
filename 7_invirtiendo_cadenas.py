"""
#7
INVIRTIENDO CADENAS
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

texto = str(input("Introduce el texto a invertir: "))
texto_revez = ""

for letra in texto:
    texto_revez = letra + texto_revez

print(texto_revez)
