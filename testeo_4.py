import funciones as func

# Caso de prueba 1: Archivo con contenido válido
contenido_prueba_1 = "usuario1@example.com\ncontrasenia123\n"
with open("ruta_dummy1.txt", 'w') as archivo:
    archivo.write(contenido_prueba_1)

mail, contrasenia = func.usuario_constrasenia("ruta_dummy1.txt")
resultado_1 = mail == "usuario1@example.com" and contrasenia == "contrasenia123"
print("Caso 1:", "Exitoso" if resultado_1 else "Falló")

# Caso de prueba 2: Archivo vacío (Rompe el codigo)
# contenido_prueba_2 = ""
# with open("ruta_dummy2.txt", 'w') as archivo:
#     archivo.write(contenido_prueba_2)

# mail, contrasenia = func.usuario_constrasenia("ruta_dummy2.txt")
# resultado_2 = mail == "" and contrasenia == ""
# print("Caso 2:", "Exitoso" if resultado_2 else "Falló")

# Caso de prueba 3: Archivo con líneas adicionales
contenido_prueba_3 = "usuario3@example.com\ncontrasenia123\nlinea_extra\n"
with open("ruta_dummy3.txt", 'w') as archivo:
    archivo.write(contenido_prueba_3)

mail, contrasenia = func.usuario_constrasenia("ruta_dummy3.txt")
resultado_3 = mail == "usuario3@example.com" and contrasenia == "contrasenia123"
print("Caso 3:", "Exitoso" if resultado_3 else "Falló")

# Caso de prueba 4: Archivo con dirección de correo electrónico inválida
contenido_prueba_4 = "usuario4@ejemplo@.com\ncontrasenia456\n"
with open("ruta_dummy4.txt", 'w') as archivo:
    archivo.write(contenido_prueba_4)

mail, contrasenia = func.usuario_constrasenia("ruta_dummy4.txt")
resultado_4 = mail == "usuario4@ejemplo@.com" and contrasenia == "contrasenia456"
print("Caso 4:", "Exitoso" if resultado_4 else "Falló")
