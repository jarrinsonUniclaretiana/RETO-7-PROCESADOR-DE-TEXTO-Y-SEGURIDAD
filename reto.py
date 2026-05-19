# titulo.py

def formato_titulo(texto):
    """
    Convierte un texto a "Formato Título"
    
    Ejemplo:
    "hola mundo desde bogotá" => "Hola Mundo Desde Bogotá"
    """
    return ' '.join(
        palabra.capitalize()
        for palabra in texto.lower().split()
    )


# ===== Ejemplo de uso =====

texto = "este es un ejemplo"

print(formato_titulo(texto))
# Resultado: "Este Es Un Ejemplo"