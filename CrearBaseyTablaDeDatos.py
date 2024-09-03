import sqlite3

# Conectarse o crear la base de datos
conexion = sqlite3.connect('alumnos.db') #alumnos.db es el nombre de la base de datos

# Crear un cursor de la base de datos
cursor = conexion.cursor()


# Funcion para insertar datos para la base de datos
def insertar_estudiante(nombre, apellido, edad):
    cursor.execute("INSERT INTO estudiantes (Nombre, Apellido, Edad) VALUES (?,?,?)", (nombre, apellido, edad))
    conexion.commit()

# Se crea la base antes de insertar los datos
# Crear la tabla de alumnos
"""cursor.execute('''

CREATE TABLE IF NOT EXISTS estudiantes(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    #APELLIDO TEXT NOT NULL,
    #EDAD INTEGER NOT NULL
)
''')"""

# Solicitar los datos al usuario
nombre = input("\nNombre del estudiante: ")
apellido = input("Apellido del estudiante: ")
edad = int(input("Edad del estudiante: "))

# Insertar el estudiante a la tabla
insertar_estudiante(nombre, apellido, edad)

print("\nDatos registrados correctamente: ")

# Cerrar la conexión
conexion.close()

#Mensaje para confirmar el exito de la creacion de la base y tabla de datos
#print("Base de datos creada/actualizada con éxito")