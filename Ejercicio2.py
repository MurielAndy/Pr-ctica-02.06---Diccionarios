# Nombre,,Edad,Direccion  y Telefono 

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")

datos_del_usuario = {"nombre": nombre,"edad": edad,"direccion": direccion,"telefono": telefono}

print("{datos_del_usuario['nombre']} tiene {datos_del_usuario['edad']} años, vive en {datos_del_usuario['direccion']} y su número de teléfono es {datos_del_usuario['telefono']}.")
