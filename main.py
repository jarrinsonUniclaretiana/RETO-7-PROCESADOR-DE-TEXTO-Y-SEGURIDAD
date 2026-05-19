import seguridad

password = input("Ingrese una contraseña: ")

if seguridad.es_segura(password):
    print(" Contraseña segura")
else:
    print(" Contraseña NO segura")  
