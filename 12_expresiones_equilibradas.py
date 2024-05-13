"""
#12
EXPRESIONES EQUILIBRADAS
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""


def expresiones_equilibradas(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    out1 = ""
    out2 = ""
    for letra in str1:
        if letra not in str2:
            out1 = out1 + letra
    print(out1)
    for letra in str2:
        if letra not in str1:
            out2 = out2 + letra
    print(out2)


expresiones_equilibradas("HOLA", "como")
