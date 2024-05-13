"""
#10
CÓDIGO MORSE
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */

A	· —	 	N	— ·	 	0	— — — — —
B	— · · ·	 	Ñ	— — · — —	 	1	· — — — —
C	— · — ·	 	O	— — —	 	2	· · — — —
CH	— — — —	 	P	· — — ·	 	3	· · · — —
D	— · ·	 	Q	— — · —	 	4	· · · · —
E	·	 	R	· — ·	 	5	· · · · ·
F	· · — ·	 	S	· · ·	 	6	— · · · ·
G	— — ·	 	T	—	 	7	— — · · ·
H	· · · ·	 	U	· · —	 	8	— — — · ·
I	· ·	 	V	· · · —	 	9	— — — — ·
J	· — — —	 	W	· — —	 	.	· — · — · —
K	— · —	 	X	— · · —	 	,	— — · · — —
L	· — · ·	 	Y	— · — —	 	?	· · — — · ·
M	— —	 	Z	— — · ·	 	"	· — · · — ·	 	/	— · · — ·

"""


def codigo_morse(text):
    morse_code = {"A": ".—", "N": "—.", "0": "—————",
                  "B": "—...", "Ñ": "——.——", "1": ".————",
                  "C": "—.—.", "O": "———", "2": "..———",
                  "CH": "————", "P": ".——.", "3": "...——",
                  "D": "—..", "Q": "——.—", "4": "....—",
                  "E": ".", "R": ".—.", "5": ".....",
                  "F": "..—.", "S": "...", "6": "—....",
                  "G": "——.", "T": "—", "7": "——...",
                  "H": "....", "U": "..—", "8": "———..",
                  "I": "..", "V": "...—", "9": "————.",
                  "J": ".———", "W": ".——", ".": ".—.—.—",
                  "K": "—.—", "X": "—..—", ",": "——..——",
                  "L": ".—..", "Y": "—.——", "?": "..——..",
                  "M": "——", "Z": "——..", "//": ".—..—.", "/": "—..—."}
    encode = ""

    for char in text:
        if char.upper() in morse_code.keys():
            encode += morse_code[char.upper()]
        else:
            encode += char

    return encode


print(codigo_morse("hola como estas"))
