import os
import pygame
import keyboard
import copy
import cursor
import json
import sys
import re

def leer_archivo():
	try:
		path_archivo = os.path.dirname(os.path.abspath(__file__))
		arch_dic = os.path.join(path_archivo, f"Usuarios.json")
		contenido = open(arch_dic,"r")
		cont_existente = contenido.read()
		contenido.close()
		diccionario_usuarios = json.loads(cont_existente)
		return diccionario_usuarios
	except TypeError:
		print(TypeError)
		print("Error de lectura")

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
		path_archivo = os.path.dirname(os.path.abspath(__file__))
		arch_dic = os.path.join(path_archivo, f"Usuarios.json")
		contenido = open(arch_dic, "w")
		contenido.write(usuarios_JSON)
		contenido.close()
		print("Bienvenido", usuario, ". Presione 'Enter' para continuar: ")
		input()
	except TypeError:
		print(TypeError)
		print("Error de grabado")


def mostrar_equipo():
    os.system("cls")
    print("Este es nuestro equipo")
    for miembro in equipo:
        print(miembro)


def mostrar_proyecto():
    os.system("cls")
    print("Nuestro proyecto se trata sobre el juego de mesa Batalla Naval:\n El mismo será realizado usando un formato via terminal en ASCII, y contará \n con un modo multijugador en linea, en el cual cada jugador podrá \n colocar a libertad sus barcos, bombardear el lado enemigo del tablero, y recibir \n feedback en tiempo real de los resultados de sus acciones en una partida por turnos.") #TODO revisar esta funcion

def menu():
    cursor.hide()
    repetir = True
    op = 0
    submarino = ["⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡆",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣶",
                "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿",
                "⠀⣶⡄⢀⣀⣤⣴⡶⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣷⣶⣤⣀",
                "⣠⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⡇",
                "⠘⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃",
                "⠀⠛⠁⠀⠀⠉⠙⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠁"]
    x = 0
    pygame.init()
    clock = pygame.time.Clock()
    while repetir:
        # print("░"*4865)
        print("\033[0;25H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("\033[1;25H█████▄░▄████▄░████████░▄████▄░██░░░░░██░░░░░▄████▄░░░██████▄░▄████▄░██░░░██░▄████▄░██░░░░")
        print("\033[2;25H██░░██░██░░██░░░░██░░░░██░░██░██░░░░░██░░░░░██░░██░░░██░░░██░██░░██░██░░░██░██░░██░██░░░░")
        print("\033[3;25H█████░░██░░██░░░░██░░░░██░░██░██░░░░░██░░░░░██░░██░░░██░░░██░██░░██░██░░░██░██░░██░██░░░░")
        print("\033[4;25H██░░██░██████░░░░██░░░░██████░██░░░░░██░░░░░██████░░░██░░░██░██████░██░░██░░██████░██░░░░")
        print("\033[5;25H█████▀░██░░██░░░░██░░░░██░░██░██████░██████░██░░██░░░██░░░██░██░░██░▀███▀░░░██░░██░██████")
        print("\033[6;25H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        y = 7
        for i in range(len(submarino)):
            print(f"\033[{int(y+i)};{int(x)}H{submarino[i]}")
        x += 0.3
        if x >= 112 + len(submarino[4]):
            x = 0
        clock.tick(24)
        os.system("cls")
        if op == 0:
            print("\033[16;60H\033[104m     Juego     \033[0m")
            print("\033[17;60H Iniciar Sesión ")
            print("\033[18;60H  Registrarse  ")
            print("\033[19;60H     Equipo     ")
            print("\033[20;60H    Proyecto    ")
            print("\033[21;60H     Salir     ")
        elif op == 1:
            print("\033[16;60H     Juego     ")
            print("\033[17;60H\033[104m Iniciar Sesión \033[0m")
            print("\033[18;60H  Registrarse  ")
            print("\033[19;60H     Equipo     ")
            print("\033[20;60H    Proyecto    ")
            print("\033[21;60H     Salir     ")
        elif op == 2:
            print("\033[16;60H     Juego     ")
            print("\033[17;60H Iniciar Sesión ")
            print("\033[18;60H\033[104m  Registrarse  \033[0m")
            print("\033[19;60H     Equipo     ")
            print("\033[20;60H    Proyecto    ")
            print("\033[21;60H     Salir     ")
        elif op == 3:
            print("\033[16;60H     Juego     ")
            print("\033[17;60H Iniciar Sesión ")
            print("\033[18;60H  Registrarse  ")
            print("\033[19;60H\033[104m     Equipo     \033[0m")
            print("\033[20;60H    Proyecto    ")
            print("\033[21;60H     Salir     ")
        elif op == 4:
            print("\033[16;60H     Juego     ")
            print("\033[17;60H Iniciar Sesión ")
            print("\033[18;60H  Registrarse  ")
            print("\033[19;60H     Equipo     ")
            print("\033[20;60H\033[104m    Proyecto    \033[0m")
            print("\033[21;60H     Salir     ")
        elif op == 5:
            print("\033[16;60H     Juego     ")
            print("\033[17;60H Iniciar Sesión ")
            print("\033[18;60H  Registrarse  ")
            print("\033[19;60H     Equipo     ")
            print("\033[20;60H    Proyecto    ")
            print("\033[21;60H\033[104m     Salir     \033[0m")
        if keyboard.is_pressed('w'):
            if presionado == False:
                if op-1 != -1:
                    op-=1
            presionado = True
        elif keyboard.is_pressed('s'):
            if presionado == False:
                if op+1 != 6:
                    op += 1
            presionado = True
        elif keyboard.is_pressed('e'):
            if presionado == False:
                if op == 0:
                    repetir = False
                    juego()
                elif op == 1:
                    os.system("cls")
                    input("Presione 'Enter' para continuar: ")
                    nuevo_usuario = str(input("Ingrese su nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
                    usuarios = leer_archivo()
                    log_in(nuevo_usuario, usuarios)    
                elif op == 2:
                    os.system("cls")
                    input("Presione 'Enter' para continuar: ")
                    nuevo_usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
                    while not re.match("^[a-zA-Z0-9]{5,12}$", nuevo_usuario):
                        os.system("cls")
                        print("Nombre de usuario invalido")
                        nuevo_usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
                    usuarios = leer_archivo()
                    sign_up(nuevo_usuario, usuarios)
                elif op == 3:
                    mostrar_equipo()
                    print()
                    input("Presione 'Enter' para continuar: ")
                elif op == 4:
                    mostrar_proyecto()
                    print()
                    input("Presione 'Enter' para continuar: ")
                elif op == 5:
                    os.system("cls")
                    repetir = False
            presionado = True
        else:
            presionado = False
def dibujar(tablero):
    for fila in tablero:
        for columna in fila:
            print(columna,end="")
        print()
        
def convertir_a_numero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if  "≡" in tablero[i][j]:
                tablero[i][j] = "1"
            elif "¤" in tablero[i][j]:
                tablero[i][j] = "2"

def scoreboard():
    path=os.path.dirname(os.path.abspath(__file__))
    arch_div = os.path.join(path, f"Usuarios.json")
    tablas=open(arch_div, "r")
    contenido_tablas=json.load(tablas)
    tablas.close()
    tuplas_usuarios=[]
    for usuario in contenido_tablas:
        puntaje=contenido_tablas[usuario]["puntaje"]
        tuplas_usuarios.append((puntaje,usuario))
    print(tuplas_usuarios)
    tuplas_o=tuple(sorted(tuplas_usuarios,reverse=True))
    print(tuplas_o)

def movimiento_barco(direccion,barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for i in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][i]
            tablero[old_x][old_y] = "\033[36m ~\033[0m"
            x,y = direccion
            new_x = old_x + x
            new_y = old_y + y
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][i] = (new_x,new_y)
        
    
        
def visualizar_barco(barcos,tablero_barcos):
    for barco in barcos:
        for coordenada in barco:
            tablero_barcos[coordenada[0]][coordenada[1]] = "\033[90m ≡\033[0m"
            
def rotacion_a_vertical(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = "\033[36m ~\033[0m"
            new_x = old_x + coordenada
            new_y = old_y - coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)
        
def rotacion_a_horizontal(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = "\033[36m ~\033[0m"
            new_x = old_x - coordenada
            new_y = old_y + coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)

def confirmar_barco(barcos,barco,partido,arch_tablero,tablero,tablero_disparo):
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            for barco2 in range(len(barcos)):
                if barco2 != barco:
                    for coordenada2 in range(len(barcos[barco2])):
                        if barcos[barco][coordenada] == barcos[barco2][coordenada2]:
                            posible = False
    if posible:
        barco+=1
    if barco == 5:
        convertir_a_numero(tablero_disparo)
        convertir_a_numero(tablero)
        tableros = json.dumps(partido, indent=4)
        try:
            contenido = open(arch_tablero, "w")
            contenido.write(tableros)
            contenido.close()
            print("crado")
        except TypeError:
            print(TypeError)
            print("error de grabado de cambios")
    return barco

def visualizar_disparos(disparo,tablero_disparos,bombas):
    for coordenada in bombas:
        tablero_disparos[coordenada[0]][coordenada[1]] = "\033[31m ¤\033[0m"
    tablero_disparos[disparo[0]][disparo[1]] = "\033[37m ¤\033[0m"
def dibujar_radar(i):
    o = (f"\033[32m ▓\033[0m") #main
    p = (f"\033[32m ░\033[0m") #estela 1
    l= (f"\033[32m ▒\033[0m")  #estela 2
    m = (f"\033[32m ~\033[0m") #guiones
    radar0=f"   {m}{p}{m}  \n {m}{m}{l}{l}{m} \n {m}{m}{o}{o}{o} \n {m}{m}{m}{m}{m} \n   {m}{m}{m}"
    radar1=f"   {m}{m}{m}  \n {m}{m}{p}{p}{m} \n {m}{m}{o}{l}{l} \n {m}{m}{m}{o}{m} \n   {m}{m}{m}"
    radar2=f"   {m}{m}{m}  \n {m}{m}{m}{m}{m} \n {m}{m}{o}{p}{p} \n {m}{m}{o}{l}{m} \n   {m}{o}{m}"
    radar3=f"   {m}{m}{m}  \n {m}{m}{m}{m}{m} \n {m}{m}{o}{m}{m} \n {m}{o}{l}{p}{m} \n   {m}{l}{m}"
    radar4=f"   {m}{m}{m}  \n {m}{m}{m}{m}{m} \n {o}{o}{o}{m}{m} \n {m}{l}{p}{m}{m} \n   {m}{p}{m}"
    radar5=f"   {m}{m}{m}  \n {m}{o}{m}{m}{m} \n {l}{l}{o}{m}{m} \n {m}{p}{m}{m}{m} \n   {m}{m}{m}"
    radar6=f"   {m}{o}{m}  \n {m}{l}{o}{m}{m} \n {p}{p}{o}{m}{m} \n {m}{m}{m}{m}{m} \n   {m}{m}{m}"
    radar7=f"   {m}{l}{m}  \n {m}{p}{l}{o}{m} \n {m}{m}{o}{m}{m} \n {m}{m}{m}{m}{m} \n   {m}{m}{m}"
    radar = [radar0,radar1,radar2,radar3,radar4,radar5,radar6,radar7]
    print(radar[i])
def movimiento_disparo(direccion,bomba,tablero):
    posible = True
    if posible:
        old_x,old_y = bomba
        tablero[old_x][old_y] = "\033[36m ~\033[0m"
        x,y = direccion
        new_x = old_x + x
        new_y = old_y + y
        if new_x <= 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero)-1:
            posible = False
        else:
            bomba = (new_x,new_y)
    return bomba

def confirmar_tiro(posicion_tiro,tiros,confirmable):
#TODO el primer parámetro tiene que ser el nombre que le demos a la posición actual del disparo
    confirmable = True
    if tiros == []:
        return confirmable
    else:
        for tiro in range(len(tiros)):
            if tiros[tiro] == posicion_tiro:
                confirmable = False
        return confirmable
       
def deteccion_disparo(disparo, lista_barcos):
    i = 0
    encontrado = False
    while i < len(lista_barcos) and encontrado == False:
        j = 0
        while j < len(lista_barcos[i]) and encontrado == False:
            if disparo == lista_barcos[i][j] and encontrado == False:
                del lista_barcos[i][j]
                encontrado = True
            j += 1
        i += 1
    return encontrado

def juego():
    cursor.hide()
    pygame.init()
    clock = pygame.time.Clock()
    path_tableros = os.path.dirname(os.path.abspath(__file__))
    arch_tab = os.path.join(path_tableros, f"Tableros.json")
    o = "\033[36m ~\033[0m"
    b = "\033[90m ≡\033[0m"
    portaaviones = b
    mulportaaviones = 5
    destructor = b
    muldestructor = 4
    crucero1 = (f"\033[31mDestruido\033[0m")
    mulcrucero1= 1
    crucero2 = b
    mulcrucero2 = 3
    lancha = b
    mullancha = 2
    # ░≡¤

    
    j1_tablerodisparos= [["╔","══","══","══","══","══","══","══","══","══","══","═╗","portaaviones: ",portaaviones*mulportaaviones],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║","destructor: ",destructor*muldestructor],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║","crucero: ",crucero1*mulcrucero1],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║","crucero: ",crucero2*mulcrucero2],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║","lancha: ", lancha*mullancha],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["╠","══","══","══","══","══","══","══","══","══","══","═╣"]]
    j1_tablerobarcos   = [
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["╚","══","══","══","══","══","══","══","══","══","══","═╝"]]
    j2_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j2_tablerobarcos   = [
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["║",o,o,o,o,o,o,o,o,o,o," ║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    #TODO hacer un radar al costado del tablero
    num_barco = 0
    todos_barcos = [[(1,1),(1,2),(1,3),(1,4),(1,5)],[(1,1),(1,2),(1,3),(1,4)],[(1,1),(1,2),(1,3)],[(1,1),(1,2),(1,3)],[(1,1),(1,2)]]
    barcosj1 = [[], [], [], [], []]
    barcosj2 = [[], [], [], [], []]
    tirosj1 = []
    tirosj2 = []
    pos_bomba = (1,1)
    radar = 0
    turno = 1
    miturno = 1
    game = True
    estado = "posicionar barcos"
    confirmado = True
    partida = {"Jugador 1": {"tablero disparos": j1_tablerodisparos, "tablero barcos": j1_tablerobarcos}, "jugador 2": {"tablero disparos": j2_tablerodisparos,
                "tablero barcos": j2_tablerobarcos}, "turno": turno}
    #TODO chequear en vez de mandar todos los tableros se manda nada mas el tiro y el turno
    while game == True:
        if num_barco <=4 and barcosj1[num_barco] == []:
            barcosj1[num_barco] = todos_barcos[num_barco]
        elif num_barco == 5:
            estado = "posicionar disparos"
        if turno == miturno:
            if keyboard.is_pressed('w'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((-1,0),barcosj1,num_barco,j1_tablerobarcos)
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((-1,0),pos_bomba,j1_tablerodisparos)
                presionado = True
            elif keyboard.is_pressed('s'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((1,0),barcosj1,num_barco,j1_tablerobarcos)
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((1,0),pos_bomba,j1_tablerodisparos)
                presionado = True
            elif keyboard.is_pressed('d'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((0,1),barcosj1,num_barco,j1_tablerobarcos)
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((0,1),pos_bomba,j1_tablerodisparos)
                presionado = True
            elif keyboard.is_pressed('a'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((0,-1),barcosj1,num_barco,j1_tablerobarcos)
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((0,-1),pos_bomba,j1_tablerodisparos)
                presionado = True
            elif keyboard.is_pressed('r'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if barcosj1[num_barco][0][0]==barcosj1[num_barco][1][0]:
                            rotacion_a_vertical(barcosj1,num_barco,j1_tablerobarcos)
                        else:
                            rotacion_a_horizontal(barcosj1,num_barco,j1_tablerobarcos)#TODO cuando se pone la direccion con el diccionario se rompe
                presionado = True
            elif keyboard.is_pressed('e'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        num_barco = confirmar_barco(barcosj1,num_barco, partida, arch_tab,j1_tablerobarcos,j1_tablerodisparos)
                    elif estado =="posicionar disparos":
                        confirmado = confirmar_tiro(pos_bomba,tirosj1,confirmado)
                        if confirmado:
                            encontrar = deteccion_disparo(pos_bomba, barcosj1)
                            if encontrar:
                                print("TOCADO!")
                            elif not encontrar:
                                print("AGUA!")
                            tirosj1.append(pos_bomba)
                            convertir_a_numero(j1_tablerobarcos)
                            convertir_a_numero(j1_tablerodisparos)
                            tableros = json.dumps(partida, indent=4)
                            try:
                                contenido = open(arch_tab, "w")
                                contenido.write(tableros)
                                contenido.close()
                                print("crado")
                            except TypeError:
                                print(TypeError)
                                print("error de grabado de cambios")
                            pos_bomba = (1,1)
                presionado = True
            else:
                presionado = False
        else:
            print("Esperando oponente...")
        sys.stdin.flush()
        visualizar_barco(barcosj1,j1_tablerobarcos)
        visualizar_disparos(pos_bomba,j1_tablerodisparos,tirosj1)
        dibujar(j1_tablerodisparos)
        dibujar(j1_tablerobarcos)
        print(tirosj1)
        clock.tick(24)
        dibujar_radar(int(radar))
        radar +=0.1
        if radar >= 8:
            radar = 0
        os.system("cls")
equipo = ["Diaz, German Ezequiel", "Nuñez Gagliano, Francisco Dario", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella Jazmín", "Trimarco, Tomas","McLovin"]
#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir