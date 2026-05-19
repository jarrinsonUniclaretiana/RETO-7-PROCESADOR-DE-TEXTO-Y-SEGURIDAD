import unicodedata

def quitar_tilde(letra):
    letra_normalizada = unicodedata.normalize('NFD', letra)
    letra_sin_tilde = ''

    for caracter in letra_normalizada:
        if unicodedata.category(caracter) != 'Mn':
            letra_sin_tilde += caracter

    return letra_sin_tilde


def contar_frecuencia_vocales(texto):
    frecuencias = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    texto = texto.lower()

    for caracter in texto:
        caracter = quitar_tilde(caracter)

        if caracter in frecuencias:
            frecuencias[caracter] += 1

    return frecuencias


# Programa principal
texto = input("Ingrese un texto largo")

resultado = contar_frecuencia_vocales(texto)

print("\nFrecuencia de vocales:")
print("A:", resultado["a"])
print("E:", resultado["e"])
print("I:", resultado["i"])
print("O:", resultado["o"])
print("U:", resultado["u"])
