#creando la base de datos SQLite3
import sqlite3

#conectando con la base de datos
datab = sqlite3.connect("datos.db")

cons = datab.cursor()
print("La base de datos se abrio correctamente")

#al crearse la tabla debe eliminar el codigo despues que se crea la tabla
cons.execute(''' CREATE TABLE Datos
    (ID INT PRIMARY KEY  NOT NULL,
    Nombre        text  NOT NULL,
    Apellido      text  NOT NULL,
    Edad          INT   NOT NULL) ''')

print("Tabla creada con exito..........")

cons.execute("INSERT INTO Datos (ID,Nombre, Apellido, Edad) VALUES (1,'Pedro', 'Gonzalez', 22)")
cons.execute("INSERT INTO Datos (ID, Nombre, Apellido, Edad) VALUES (2, 'Juan', 'Penaloza', 21)")
cons.execute("INSERT INTO Datos (ID, Nombre, Apellido, Edad) VALUES (3, 'Noriel', 'Camacho', 17)")

datab.commit() #guardando los datos de la tabla en la base de datos
print("datos fueron guardados")

#mostrar datos en pantalla
cons.execute("SELECT ID, Nombre, Apellido, Edad from Datos")
for i in cons:
    print("ID:" + str(i[0]) + "  Nombre:" + str(i[1]) + "  Apellido: " + str(i[2]) + "  Edad:" + str(i[3]))

print("impresion completada")

#cerrar la consulta
cons.close()
#cerrar la sesion de la base de datos
datab.close()





