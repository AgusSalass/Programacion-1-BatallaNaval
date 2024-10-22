import json
import os
import re

path_archivo = os.path.dirname(os.path.abspath(__file__))

nuevo_usuario = str(input("usuario (maximo 12 caracteres, solo letras y numeros): "))
while not re.match("[a-zA-Z0-9]{5,12}", nuevo_usuario):
	nuevo_usuario = str(input("usuario invalido, ingrese uno nuevo (maximo 12 caracteres, solo letras y numeros): "))
nueva_contrasena = str(input("contraseña: "))
while not re.match("[a-zA-Z0-9]{5,12}", nueva_contrasena):
    nueva_contrasena = str(input("contraseña invalida, ingrese una nueva (maximo 12 caracteres, solo letras y numeros): "))

try:
	arch_div = os.path.join(path_archivo, f"Usuarios.json")
	contenido = open(arch_div,"r")
	cont_existente = contenido.read()
	contenido.close()
	usuarios = json.loads(cont_existente)

	while nuevo_usuario in usuarios:
		print("usuario ya existe")
		nuevo_usuario = str(input("usuario (maximo 12 caracteres, solo letras y numeros): "))
		while not re.match("[a-zA-Z0-9]{12}", nuevo_usuario):
			nuevo_usuario = str(input("usuario invalido, ingrese uno nuevo (maximo 12 caracteres, solo letras y numeros): "))
		nueva_contrasena = str(input("contraseña: "))
		while not re.match("[a-zA-Z0-9]{12}", nueva_contrasena):
			nueva_contrasena = str(input("contraseña invalida, ingrese una nueva (maximo 12 caracteres, solo letras y numeros): "))
	else:
		usuarios[nuevo_usuario] = {
			"contrasena": nueva_contrasena,
			"puntaje": 0
		}

		usuarios_JSON = json.dumps(usuarios, indent=4)
		try:
			contenido = open(arch_div, "w")
			contenido.write(usuarios_JSON)
			contenido.close()
		except TypeError:
			print(TypeError)
			print("error de grabado de cambios")
			

except TypeError:
    print(TypeError)
    print("error de lectura:")