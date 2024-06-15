def validarCorreo():
    while True:
        correo = input("\nIngresa tu correo: ")
        if correo == "jonathan.ascencio23@itca.edu.sv":
            return "\nUsuario correcto"
        elif correo.isdigit():
            print("\nEl correo no puede ser solo números. Inténtalo de nuevo.")
        else:
            print("\nEl usuario no es válido.")

print(validarCorreo())