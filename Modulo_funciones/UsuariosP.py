import json
import os
import re

def sign_up(usuario):
	path_archivo = os.path.dirname(os.path.abspath(__file__))
	try:
		arch_div = os.path.join(path_archivo, f"Usuarios.json")
		contenido = open(arch_div,"r")
		cont_existente = contenido.read()
		contenido.close()
		diccionario_usuarios = json.loads(cont_existente)

		if usuario in diccionario_usuarios:
			while usuario in diccionario_usuarios:
				print("usuario ya existe")
				usuario = str(input("usuario (maximo 12 caracteres, solo letras y numeros): "))
				while not re.match("^[a-zA-Z0-9]{5,12}$", usuario):
					usuario = str(input("usuario invalido, ingrese uno nuevo (maximo 12 caracteres, solo letras y numeros): "))
		
		contrasena = str(input("contraseña: "))
		while not re.match("^[a-zA-Z0-9]{5,12}$", contrasena):
			contrasena = str(input("contraseña invalida, ingrese una nueva (maximo 12 caracteres, solo letras y numeros): "))

		diccionario_usuarios[usuario] = {
			"contrasena": contrasena,
			"puntaje": 0
		}
		usuarios_JSON = json.dumps(diccionario_usuarios, indent=4)

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

def log_in():
	pass

#programa principal
repetir = True
while repetir:
	os.system("cls")
	print ("6-Sign Up")
	print ("7-Log In")
	op=int(input("Eliga una opcion: "))
	if op == 6:
		nuevo_usuario = str(input("usuario (maximo 12 caracteres, solo letras y numeros): "))
		while not re.match("^[a-zA-Z0-9]{5,12}$", nuevo_usuario):
			nuevo_usuario = str(input("usuario invalido, ingrese uno nuevo (maximo 12 caracteres, solo letras y numeros): "))
		sign_up(nuevo_usuario)

	elif op == 7:
		log_in()