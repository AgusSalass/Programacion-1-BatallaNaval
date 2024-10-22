import json
import os
import re

diccionario_usuarios = {}

path_archivo = os.path.join(os.path.expanduser("~"), "Desktop", "usuarios.json")

if not os.path.exists(path_archivo):
    usuarios_JSON = json.dumps(diccionario_usuarios, indent=4)
    try:
        contenido = open(path_archivo, "w")
        contenido.write(usuarios_JSON)
        contenido.close()
    except:
         print("error de grabado")

nuevo_usuario = str(input("usuario (debe ser de 3 letras): "))
while not re.match("^[a-zA-Z]{3}$", nuevo_usuario):
	nuevo_usuario = str(input("usuario (debe ser de 3 letras): "))
nueva_contrasena = str(input("contraseña: "))

try:
	contenido = open(path_archivo,"r")
	cont_existente = contenido.read()
	contenido.close()
	usuarios = json.loads(cont_existente)

	while nuevo_usuario in usuarios:
		print("usuario ya existe")
		nuevo_usuario = str(input("usuario (debe ser de 3 letras): "))
		while not re.match("^[a-zA-Z]{3}$", nuevo_usuario):
			nuevo_usuario = str(input("usuario (debe ser de 3 letras): "))
		nueva_contrasena = str(input("contraseña: "))	
	else:
		usuarios[nuevo_usuario] = {
			"contrasena": nueva_contrasena,
			"puntaje": 0
		}

		usuarios_JSON = json.dumps(usuarios, indent=4)
		try:
			contenido = open(path_archivo, "w")
			contenido.write(usuarios_JSON)
			contenido.close()
		except:
			print("error de grabado de cambios")

except:
	print("error de lectura:")