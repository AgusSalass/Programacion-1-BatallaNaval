import json
import os
import re

try:
	path_archivo = os.path.dirname(os.path.abspath(__file__))
	arch_div = os.path.join(path_archivo, f"Usuarios.json")
	contenido = open(arch_div,"r")
	cont_existente = contenido.read()
	contenido.close()
	usuarios = json.loads(cont_existente)
except TypeError:
	print(TypeError)
	print("Error de lectura:")

def sign_up(usuario, diccionario_usuarios):
	if usuario in diccionario_usuarios:
		while usuario in diccionario_usuarios:
			os.system("cls")
			print("Nombre de usuario ya existente")
			usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
			while not re.match("^[a-zA-Z0-9]{5,12}$", usuario):
				os.system("cls")
				print("Nombre de usuario invalido")
				usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
	
	contrasena = str(input("Ingrese una contraseña (5-12 Caracteres, solo letras y numeros): "))
	while not re.match("^[a-zA-Z0-9]{5,12}$", contrasena):
		os.system("cls")
		print("Contraseña invalida")
		contrasena = str(input("Ingrese una contraseña (5-12 Caracteres, solo letras y numeros): "))

	diccionario_usuarios[usuario] = {
		"contrasena": contrasena,
		"puntaje": 0
	}
	usuarios_JSON = json.dumps(diccionario_usuarios, indent=4)

	try:
		contenido = open(arch_div, "w")
		contenido.write(usuarios_JSON)
		contenido.close()
		print("Bienvenido", usuario, ". Presione 'Enter' para continuar: ")
		input()
	except TypeError:
		print(TypeError)
		print("Error de grabado")

def log_in(usuario, diccionario_usuarios):
	bucle = True
	if usuario in diccionario_usuarios:
		contrasena = str(input("Ingrese su contraseña (5-12 Caracteres, solo letras y numeros), o -1 para volver a menu: "))
		if contrasena == "-1":
			bucle = -1
		while contrasena != diccionario_usuarios[usuario]["contrasena"] and bucle != -1:
			os.system("cls")
			print("Contrasena incorrecta")
			contrasena = str(input("Ingrese su contraseña (5-12 Caracteres, solo letras y numeros), o -1 para volver a menu: "))
			if contrasena == "-1":
				bucle = -1
		if contrasena != "-1":
			print("Bienvenido", usuario, ". Presione 'Enter' para continuar: ")
			input()
	else:
		print("Nombre de usuario no existente. Presione 'Enter' para continuar: ")
		input()

#programa principal
repetir = True
while repetir:
	os.system("cls")
	print ("6-Sign Up")
	print ("7-Log In")
	op=int(input("Eliga una opcion: "))
	if op == 6:
		nuevo_usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
		while not re.match("^[a-zA-Z0-9]{5,12}$", nuevo_usuario):
			os.system("cls")
			print("Nombre de usuario invalido")
			nuevo_usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
		sign_up(nuevo_usuario, usuarios)

	elif op == 7:
		nuevo_usuario = str(input("Ingrese su nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
		log_in(nuevo_usuario, usuarios)