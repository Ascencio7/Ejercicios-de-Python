def usuario(correo, password):
    correo_correcto = "ascencio3.1417@gmail.com"
    password_correcta = "wirtaryen17"
    
    if correo_correcto == correo and password_correcta == password:
        return "Usuario Existente: Acceso Concedido"
    else:
        return "Usuario No Existente: Acceso Denegado"
    
correo = input("\nCorreo: ")
password = input("Password: ")

print("\n", usuario(correo, password))
print("\n")