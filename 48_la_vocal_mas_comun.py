"""
#48
VOCAL MÁS COMÚN
/*
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
 */
 """

def vocal1(texto: str):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in texto:
        if char in vocales:
            vocales[char] += 1
        else:
            pass
    print(vocales)
    contados = sorted(vocales.items(), key=lambda key: key[1], reverse=True)
    print(contados)
    maximo = contados[0][1]
    print(maximo)
    maximo_encontrado = {}
    for char in contados:
        if maximo > char[1]:
            break
        maximo_encontrado[char[0]] = char[1]
    print(maximo_encontrado)


vocal1("holaa come")


"""

def vocal(texto):
    vocales = ["a", "e", "i", "o", "u"]
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for char in texto:
        if char in vocales and char == "a":
            a += 1
        if char in vocales and char == "e":
            e += 1
        if char in vocales and char == "i":
            i += 1
        if char in vocales and char == "o":
            o += 1
        if char in vocales and char == "u":
            u += 1
    contador = [a, e, i, o, u]
    print(a, e, i, o, u)
    print(max(contador))


def main():
    vocal("holaaaaa")


if __name__ == "__main__":
    main()

    
    """
