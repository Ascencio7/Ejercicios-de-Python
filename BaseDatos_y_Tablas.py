import sqlite3

# Conectarse o crear la base de datos
conexion = sqlite3.connect('alumnos.db')  # alumnos.db es el nombre de la base de datos

# Crear un cursor de la base de datos
cursor = conexion.cursor()

# Función para insertar datos en la base de datos
def insertar_estudiante(nombres, apellidos, edad):
    cursor.execute("INSERT INTO estudiantes (Nombres, Apellidos, Edad) VALUES (?, ?, ?)", (nombres, apellidos, edad))
    conexion.commit()

# Crear la tabla de estudiantes
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   Nombres TEXT NOT NULL,
   Apellidos TEXT NOT NULL,
   Edad INTEGER NOT NULL
)
''')

# Mensaje para confirmar el éxito de la creación de la base y tabla de datos
print("\nBase de datos creada/actualizada con éxito")

# Solicitar los datos al usuario
nombres = input("\nNombre del estudiante: ")
apellidos = input("Apellido del estudiante: ")
edad = int(input("Edad del estudiante: "))

# Insertar el estudiante en la tabla
insertar_estudiante(nombres, apellidos, edad)

print("\nDatos registrados correctamente.")

# Cerrar la conexión
conexion.close()
