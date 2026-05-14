def es_segura(password):
  
    if len(password) < 8:
        return False

    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_numero = any(c.isdigit() for c in password)

    if tiene_mayuscula and tiene_numero:
        return True
    else:
        return False
