import os
import pygame
import keyboard
import copy
import cursor
import json
import re
import socket
import time
import msvcrt

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

def escribir_archivo(usuarios_JSON):
    try:
        path_archivo = os.path.dirname(os.path.abspath(__file__))
        arch_dic = os.path.join(path_archivo, "Usuarios.json")
        contenido = open(arch_dic, "w")
        contenido.write(usuarios_JSON)
        contenido.close()
    except TypeError:
        print(TypeError)
        print("Error de grabado")

def log_in(usuario, diccionario_usuarios):
    bucle = True
    os.system("cls")
    if usuario in diccionario_usuarios:
        contrasena = str(input("Ingrese su contraseña (5-12 Caracteres, solo letras y numeros), o -1 para volver a menu: "))
        if contrasena == "-1":
            bucle = False
        while contrasena != diccionario_usuarios[usuario]["contrasena"] and bucle:
            os.system("cls")
            print("Contraseña incorrecta")
            contrasena = str(input("Ingrese su contraseña (5-12 Caracteres, solo letras y numeros), o -1 para volver a menu: "))
            if contrasena == "-1":
                bucle = False
        os.system("cls")
        if contrasena != "-1":
            print("Bienvenido", usuario, ". Presione 'Enter' para continuar: ")
            input()
            return usuario
    else:
        usuario = "None"
        print("Nombre de usuario no existente. Presione 'Enter' para continuar: ")
        input()
        return usuario

def sign_up(usuario, diccionario_usuarios):
    os.system("cls")
    if usuario not in diccionario_usuarios:
        alias = str(input("Ingrese un alias (3 Caracteres, solo letras): ")).upper()
        while not re.match("^[A-Z]{3}$", alias):
            os.system("cls")
            print("Alias invalido")
            alias = str(input("Ingrese un alias (3 Caracteres, solo letras): ")).upper()
        os.system("cls")
        contrasena = str(input("Ingrese una contraseña (5-12 Caracteres, solo letras y numeros): "))
        while not re.match("^[a-zA-Z0-9]{5,12}$", contrasena):
            os.system("cls")
            print("Contraseña invalida")
            contrasena = str(input("Ingrese una contraseña (5-12 Caracteres, solo letras y numeros): "))
        os.system("cls")

        diccionario_usuarios[usuario] = {
            "alias": alias,
            "contrasena": contrasena,
            "puntaje": 0
        }
        
        usuarios_JSON = json.dumps(diccionario_usuarios, indent=4)
        escribir_archivo(usuarios_JSON)
        print("Bienvenido", usuario, ". Presione 'Enter' para continuar: ")
        input()
        return usuario
    else:
        usuario = "None"
        print("Nombre de usuario ya existente. Presione 'Enter' para continuar: ")
        input()
        return usuario

def mostrar_leaderboard(diccionario_usuarios):
    os.system("cls")
    tuplas_usuarios = []
    print("\033[1;48H:::        ::::::::::     :::     :::::::::  :::::::::: :::::::::  :::::::::   ::::::::      :::     :::::::::  :::::::::")
    print("\033[2;48H:+:        :+:          :+: :+:   :+:    :+: :+:        :+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:    :+:")
    print("\033[3;48H+:+        +:+         +:+   +:+  +:+    +:+ +:+        +:+    +:+ +:+    +:+ +:+    +:+  +:+   +:+  +:+    +:+ +:+    +:+")
    print("\033[4;48H+#+        +#++:++#   +#++:++#++: +#+    +:+ +#++:++#   +#++:++#:  +#++:++#+  +#+    +:+ +#++:++#++: +#++:++#:  +#+    +:+")
    print("\033[5;48H+#+        +#+        +#+     +#+ +#+    +#+ +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+     +#+ +#+    +#+ +#+    +#+")
    print("\033[6;48H#+#        #+#        #+#     #+# #+#    #+# #+#        #+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#    #+# #+#    #+#")
    print("\033[7;48H########## ########## ###     ### #########  ########## ###    ### #########   ########  ###     ### ###    ### #########")
    for usuario in diccionario_usuarios:
        puntaje = diccionario_usuarios[usuario]["puntaje"]
        alias = diccionario_usuarios[usuario]["alias"]
        tuplas_usuarios.append((puntaje, alias))
    tuplas_usuarios = sorted(tuplas_usuarios, reverse=True)
    num = "9"
    for puntaje, usuario in tuplas_usuarios[:10]:
        print(f"\033[{num};106H{usuario}: {puntaje}")
        num = int(num)
        num += 1
        num = str(num)

def mostrar_equipo():
    os.system("cls")
    equipo = ["Diaz, German Ezequiel", "Nuñez Gagliano, Francisco Dario", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella Jazmín", "Trimarco, Tomas"]
    print("Este es nuestro equipo")
    for miembro in equipo:
        print(miembro)


def mostrar_proyecto():
    os.system("cls")
    path_proyecto = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(path_proyecto, f"El Proyecto.txt")
    proyecto = open(archivo,"r", encoding="utf8")
    proyec= proyecto.read()
    print (proyec)
    proyecto.close()

def mostrar_instrucciones():
    os.system("cls")
    path_instrucciones = os.path.dirname(os.path.abspath(__file__))
    archivo_dic = os.path.join(path_instrucciones, f"Instrucciones.txt")
    instrucciones = open(archivo_dic,"r", encoding="utf8")
    instrucc = instrucciones.read()
    print (instrucc)
    instrucciones.close()

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
    cuenta = "None"
    pygame.init()
    clock = pygame.time.Clock()
    presionado = True
    while repetir:
        print("\033[0;65H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("\033[1;65H█████▄░▄████▄░████████░▄████▄░██░░░░░██░░░░░▄████▄░░░██████▄░▄████▄░██░░░██░▄████▄░██░░░░")
        print("\033[2;65H██░░██░██░░██░░░░██░░░░██░░██░██░░░░░██░░░░░██░░██░░░██░░░██░██░░██░██░░░██░██░░██░██░░░░")
        print("\033[3;65H█████░░██░░██░░░░██░░░░██░░██░██░░░░░██░░░░░██░░██░░░██░░░██░██░░██░██░░░██░██░░██░██░░░░")
        print("\033[4;65H██░░██░██████░░░░██░░░░██████░██░░░░░██░░░░░██████░░░██░░░██░██████░██░░██░░██████░██░░░░")
        print("\033[5;65H█████▀░██░░██░░░░██░░░░██░░██░██████░██████░██░░██░░░██░░░██░██░░██░▀███▀░░░██░░██░██████")
        print("\033[6;65H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print(f"\033[25;101H Usuario: {cuenta}")
        y = 7
        for i in range(len(submarino)):
            print(f"\033[{int(y+i)};{int(x)}H{submarino[i]}")
        x += 0.3
        if x >= 194 + len(submarino[4]):
            x = 0
        clock.tick(24)
        os.system("cls")
        if op == 0:
            print("\033[16;101H\033[104m     Juego     \033[0m")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H     Salir     ")
        elif op == 1:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H\033[104m Iniciar Sesión \033[0m")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H     Salir     ")
        elif op == 2:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H\033[104m  Registrarse  \033[0m")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H     Salir     ")
        elif op == 3:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H\033[104m  Leaderboard  \033[0m")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H     Salir     ")
        elif op == 4:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H\033[104m     Equipo     \033[0m")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H     Salir     ")
        elif op == 5:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H\033[104m    Proyecto    \033[0m")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H     Salir     ")
        elif op == 6:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H\033[104m Instrucciones \033[0m")
            print("\033[23;101H     Salir     ")
        elif op == 7:
            print("\033[16;101H     Juego     ")
            print("\033[17;101H Iniciar Sesión ")
            print("\033[18;101H  Registrarse  ")
            print("\033[19;101H  Leaderboard  ")
            print("\033[20;101H     Equipo     ")
            print("\033[21;101H    Proyecto    ")
            print("\033[22;101H Instrucciones ")
            print("\033[23;101H\033[104m     Salir     \033[0m")
            
        if keyboard.is_pressed('w'):
            if presionado == False:
                if op-1 != -1:
                    op-=1
            presionado = True
        elif keyboard.is_pressed('s'):
            if presionado == False:
                if op+1 != 8:
                    op += 1
            presionado = True
        elif keyboard.is_pressed('e'):
            if presionado == False:
                while msvcrt.kbhit():
                    msvcrt.getch()
                if op == 0:
                    repetir = False
                    juego(cuenta)
                elif op == 1:
                    os.system("cls")
                    nuevo_usuario = str(input("Ingrese su nombre de usuario (5-12 Caracteres, solo letras y numeros): "))
                    usuarios = leer_archivo()
                    cuenta = log_in(nuevo_usuario, usuarios)   
                elif op == 2:
                    os.system("cls")
                    bucle = True
                    nuevo_usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros), o -1 para volver a menu: "))
                    if nuevo_usuario == "-1":
                        bucle = False
                    while not re.match("^[a-zA-Z0-9]{5,12}$", nuevo_usuario) and bucle:
                        os.system("cls")
                        print("Nombre de usuario invalido")
                        nuevo_usuario = str(input("Ingrese un nombre de usuario (5-12 Caracteres, solo letras y numeros), o -1 para volver a menu: "))
                        if nuevo_usuario == "-1":
                            bucle = False
                    if nuevo_usuario != "-1":
                        usuarios = leer_archivo()
                        cuenta = sign_up(nuevo_usuario, usuarios)
                elif op == 3:
                    usuarios = leer_archivo()
                    mostrar_leaderboard(usuarios)
                    print()
                    input("Presione 'Enter' para continuar: ")
                elif op == 4:
                    mostrar_equipo()
                    print()
                    input("Presione 'Enter' para continuar: ")
                elif op == 5:
                    mostrar_proyecto()
                    print()
                    input("Presione 'Enter' para continuar: ")
                elif op == 6:
                    mostrar_instrucciones()
                    print()
                    input("Presione 'Enter' para continuar: ")
                elif op == 7:
                    os.system("cls")
                    repetir = False
            presionado = True
        else:
            presionado = False
def dibujar(tablero,y):
    for fila in range(len(tablero)):
        x = 97
        for columna in range(len(tablero[fila])):
            print(f"\033[{y};{x}H{tablero[fila][columna]}")
            x += 2
        y += 1
    return y
        
def convertir_a_numero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if "\033[36m~ \033[0m" == tablero[i][j]:
                tablero[i][j] = "3"
            elif "\033[31m¤ \033[0m" == tablero[i][j]:
                tablero[i][j] = "2"
            elif "\033[90m≡ \033[0m" == tablero[i][j]:
                tablero[i][j] = "%"
            elif "══" == tablero[i][j]:
                tablero[i][j] = "4"
            elif "═╣" == tablero[i][j]:
                tablero[i][j] = "5"
            elif "╔═" == tablero[i][j]:
                tablero[i][j] = "6"
            elif  "═╗" == tablero[i][j]:
                tablero[i][j] = "7"
            elif "╚═" == tablero[i][j]:
                tablero[i][j] = "8"
            elif "╠═" == tablero[i][j]:
                tablero[i][j] = "9"
            elif "═╝" == tablero[i][j]:
                tablero[i][j] = "$"
            elif " ║" == tablero[i][j]:
                tablero[i][j] = "!"
            elif "║" == tablero[i][j]:
                tablero[i][j] = "#"
            elif "░" == tablero[i][j]:
                tablero[i][j] = "*"

def convertir_a_caracteres(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if "3" == tablero[i][j]:
                tablero[i][j] = "\033[36m~ \033[0m"
            elif "%" == tablero[i][j]:
                tablero[i][j] = "\033[90m≡ \033[0m"
            elif "2" == tablero[i][j]:
                tablero[i][j] = "\033[31m¤ \033[0m"
            elif "4" == tablero[i][j]:
                tablero[i][j] = "══"
            elif "5" == tablero[i][j]:
                tablero[i][j] = "╣"
            elif "6" == tablero[i][j]:
                tablero[i][j] = "╔═"
            elif "7" == tablero[i][j]:
                tablero[i][j] = "╗"
            elif "8" == tablero[i][j]:
                tablero[i][j] = "╚═"
            elif "9" == tablero[i][j]:
                tablero[i][j] = "╠═"
            elif "$" == tablero[i][j]:
                tablero[i][j] = "╝"
            elif "#" == tablero[i][j]:
                tablero[i][j] = "║"
            elif "!" == tablero[i][j]:
                tablero[i][j] = " ║"
            elif "*" == tablero[i][j]:
                tablero[i][j] = "\033[97m░ \033[0m"

def movimiento_barco(direccion,barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for i in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][i]
            tablero[old_x][old_y] = "\033[36m~ \033[0m"
            x,y = direccion
            new_x = old_x + x
            new_y = old_y + y
            if new_x < 1 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero)-1:
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][i] = (new_x,new_y)
        
    
        
def visualizar_barco(barcos,tablero_barcos):
    for barco in barcos:
        for coordenada in barco:
            tablero_barcos[coordenada[0]][coordenada[1]] = "\033[90m≡ \033[0m"
            
def rotacion_a_vertical(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = "\033[36m~ \033[0m"
            new_x = old_x + coordenada
            new_y = old_y - coordenada
            if new_x < 1 or new_x >= len(tablero)-1 or new_y <= 0 or new_y >= len(tablero)-1:
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
            tablero[old_x][old_y] = "\033[36m~ \033[0m"
            new_x = old_x - coordenada
            new_y = old_y + coordenada
            if new_x < 1 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero)-1:
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)

def confirmar_barco(barcos,barco,partido,arch_tab,tablero1,tablero_disparo1,tablero2,tablero_disparo2):
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
        convertir_a_numero(tablero_disparo1)
        convertir_a_numero(tablero1)
        convertir_a_numero(tablero_disparo2)
        convertir_a_numero(tablero2)
        tableros = json.dumps((partido["Jugador 1"], partido["Jugador 2"], partido["Datos"]))
        try:
            contenido = open(arch_tab, "w")
            contenido.write(tableros)
            contenido.close()
        except TypeError:
            print(TypeError)
            print("error de grabado de cambios")
        convertir_a_caracteres(tablero_disparo1)
        convertir_a_caracteres(tablero1)
        convertir_a_caracteres(tablero_disparo2)
        convertir_a_caracteres(tablero2)
    return barco

def visualizar_disparos(disparo,tablero_disparos,bombas_dadas,bombas_falladas,turno,miturno,estado):
    for coordenada in bombas_dadas:
        tablero_disparos[coordenada[0]][coordenada[1]] = "\033[31m¤ \033[0m"
    for coordenada in bombas_falladas:
        tablero_disparos[coordenada[0]][coordenada[1]] = "\033[97m░ \033[0m"
    if turno == miturno and estado == "posicionar disparos":
        tablero_disparos[disparo[0]][disparo[1]] = "\033[37m¤ \033[0m"

def dibujar_radar(i):
    '''luz principal'''
    o = (f"\033[32m ▓\033[0m")
    '''estela 1'''
    p = (f"\033[32m ░\033[0m")
    '''estela 2'''
    l= (f"\033[32m ▒\033[0m")
    '''guiones'''
    m = (f"\033[32m ~\033[0m")
    radar0=f"\033[11;84H   {m}{p}{m}  \n \033[12;84H {m}{m}{l}{l}{m} \n \033[13;84H {m}{m}{o}{o}{o} \n \033[14;84H {m}{m}{m}{m}{m} \n \033[15;84H   {m}{m}{m}"
    radar1=f"\033[11;84H   {m}{m}{m}  \n\033[12;84H {m}{m}{p}{p}{m} \n\033[13;84H {m}{m}{o}{l}{l} \n\033[14;84H {m}{m}{m}{o}{m} \n\033[15;84H   {m}{m}{m}"
    radar2=f"\033[11;84H   {m}{m}{m}  \n\033[12;84H {m}{m}{m}{m}{m} \n\033[13;84H {m}{m}{o}{p}{p} \n\033[14;84H {m}{m}{o}{l}{m} \n\033[15;84H   {m}{o}{m}"
    radar3=f"\033[11;84H   {m}{m}{m}  \n\033[12;84H {m}{m}{m}{m}{m} \n\033[13;84H {m}{m}{o}{m}{m} \n\033[14;84H {m}{o}{l}{p}{m} \n\033[15;84H   {m}{l}{m}"
    radar4=f"\033[11;84H   {m}{m}{m}  \n\033[12;84H {m}{m}{m}{m}{m} \n\033[13;84H {o}{o}{o}{m}{m} \n\033[14;84H {m}{l}{p}{m}{m} \n\033[15;84H   {m}{p}{m}"
    radar5=f"\033[11;84H   {m}{m}{m}  \n\033[12;84H {m}{o}{m}{m}{m} \n\033[13;84H {l}{l}{o}{m}{m} \n\033[14;84H {m}{p}{m}{m}{m} \n\033[15;84H   {m}{m}{m}"
    radar6=f"\033[11;84H   {m}{o}{m}  \n\033[12;84H {m}{l}{o}{m}{m} \n\033[13;84H {p}{p}{o}{m}{m} \n\033[14;84H {m}{m}{m}{m}{m} \n\033[15;84H   {m}{m}{m}"
    radar7=f"\033[11;84H   {m}{l}{m}  \n\033[12;84H {m}{p}{l}{o}{m} \n\033[13;84H {m}{m}{o}{m}{m} \n\033[14;84H {m}{m}{m}{m}{m} \n\033[15;84H   {m}{m}{m}"
    radar = [radar0,radar1,radar2,radar3,radar4,radar5,radar6,radar7]
    print(radar[i])

def movimiento_disparo(direccion,bomba,tablero):
    posible = True
    if posible:
        old_x,old_y = bomba
        tablero[old_x][old_y] = "\033[36m~ \033[0m"
        x,y = direccion
        new_x = old_x + x
        new_y = old_y + y
        if new_x <= 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero)-1:
            posible = False
        else:
            bomba = (new_x,new_y)
    return bomba

def confirmar_tiro(posicion_tiro,tiros,confirmable,tiros_fallados):
    confirmable = True
    if tiros == []:
        return confirmable
    else:
        for tiro in range(len(tiros)):
            if tiros[tiro] == posicion_tiro:
                confirmable = False
        for tiro in range(len(tiros_fallados)):
            if tiros_fallados[tiro] == posicion_tiro:
                confirmable = False
        return confirmable
       
def deteccion_disparo(disparo,tablero_disparo,tablerobarcos):
    x,y = disparo
    encontrado = False
    if  "≡" in tablerobarcos[x][y]:
        tablero_disparo[x][y] = "\033[31m¤ \033[0m"
        tablerobarcos[x][y] = "\033[31m¤ \033[0m"
        encontrado = True
    else:
        tablero_disparo[x][y] = "\033[97m░ \033[0m"
        tablerobarcos[x][y] = "\033[97m░ \033[0m"
    return encontrado

def actualizar_pantalla(barcos,tablerobarcos,pos_bomba,tablerodisparos,tiros_dados,radar,tiros_fallados,estado,turno,miturno):
    os.system("cls")
    if estado == "posicionar barcos":
        visualizar_barco(barcos,tablerobarcos)
    visualizar_disparos(pos_bomba,tablerodisparos,tiros_dados,tiros_fallados,turno,miturno,estado)
    y = 1
    y = dibujar(tablerodisparos,y)
    dibujar(tablerobarcos,y)
    dibujar_radar(int(radar))

def disparo(bomba,tiros_dados,confirmado,tiros_fallados,tablerodisparos,tablerobarcos):
    confirmado = confirmar_tiro(bomba,tiros_dados,confirmado,tiros_fallados)
    if confirmado:
        encontrar = deteccion_disparo(bomba,tablerodisparos,tablerobarcos)
        if encontrar:
            tiros_dados.append(bomba)
        elif not encontrar:
            print("AGUA!")
            tiros_fallados.append(bomba)
    return confirmado
    
def esperar_conex():
    '''
    crea un objeto socket
    '''
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    '''
    define la direccion y el puerto del server
    '''
    server_address = ('192.168.30.1', 8080)

    '''
    conecta al servidor
    '''
    client_socket.connect(server_address)
    print("Connected to the server.")
    
    return client_socket

def  enviar_mensaje(client_socket, mensaje, arch_tab):
    '''
    envia los datos al servidor
    '''
    data = json.dumps((mensaje["Jugador 1"], mensaje["Jugador 2"], mensaje["Datos"]))
    data=data+"FinDeMensaje"
    try:
        contenido = open(arch_tab, "w")
        contenido.write(data)
        contenido.close()
    except TypeError:
        print(TypeError)
        print("eBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    
    client_socket.sendall(data.encode('utf-8'))
    
def recibir_mensaje(client_socket):
    try:
        mensajeCompleto=False
        data=""
        while not mensajeCompleto:
            data = data + client_socket.recv(1048576).decode('utf-8')
            if data.endswith("FinDeMensaje"):
                data=data[0:len(data)-12]
                mensajeCompleto=True
    except socket.herror:
        print(socket.herror)
    return data

def juego(cuenta):
    conexion = esperar_conex()
    cursor.hide()
    pygame.init()
    clock = pygame.time.Clock()
    path_tableros = os.path.dirname(os.path.abspath(__file__))
    arch_tab = os.path.join(path_tableros, f"Tableros.json")
    o = "\033[36m~ \033[0m"
    b = "\033[90m≡ \033[0m"
    '''
    ░: caracter de disparo errado
    ≡: caracter de barco
    ¤: caracter de disparo pegado
    ~: caracter de agua
    '''
    j1_tablerodisparos= [["╔═","══","══","══","══","══","══","══","══","══","══","╗"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["╠═","══","══","══","══","══","══","══","══","══","══","╣"]]
    j1_tablerobarcos   = [["╠═","══","══","══","══","══","══","══","══","══","══","╣"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["╚═","══","══","══","══","══","══","══","══","══","══","╝"]]
    j2_tablerodisparos= [["╔═","══","══","══","══","══","══","══","══","══","══","╗"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                         ["╠═","══","══","══","══","══","══","══","══","══","══","╣"]]
    j2_tablerobarcos   = [["╠═","══","══","══","══","══","══","══","══","══","══","╣"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["║ ",o,o,o,o,o,o,o,o,o,o,"║"],
                          ["╚═","══","══","══","══","══","══","══","══","══","══","╝"]]
    num_barco = 0
    todos_barcos = [[(1,1),(1,2),(1,3),(1,4),(1,5)],[(1,1),(1,2),(1,3),(1,4)],[(1,1),(1,2),(1,3)],[(1,1),(1,2),(1,3)],[(1,1),(1,2)]]
    barcosj1 = [[], [], [], [], []]
    barcosj2 = [[], [], [], [], []]
    tirosj1_dados = []
    tirosj1_fallados = []
    tirosj2_dados = []
    tirosj2_fallados = []
    pos_bomba = (1,1)
    radar = 0
    turno = 1
    miturno = 2
    estado = "posicionar barcos"
    confirmado = True
    presionado = True
    j1_listo = False
    j2_listo = False
    jugador1gana = False
    jugador2gana = False
    radar_aux = 0
    partida = {"Jugador 1": {"tablero disparos": j1_tablerodisparos, "tablero barcos": j1_tablerobarcos, "lista barcos": barcosj1}, 
               "Jugador 2": {"tablero disparos": j2_tablerodisparos, "tablero barcos": j2_tablerobarcos, "lista barcos": barcosj2}, 
               "Datos": {"turno": turno, "j1_listo": j1_listo, "j2_listo": j2_listo, "jugador1gana": jugador1gana, "jugador2gana": jugador2gana}}
    if miturno == 1:
        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
    elif miturno == 2:
        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
    while not partida["Datos"]["jugador1gana"] and not partida["Datos"]["jugador2gana"]:
        fin_de_turno = False
        if turno == miturno:
            if miturno == 1:
                if num_barco <=4 and barcosj1[num_barco] == []:
                    barcosj1[num_barco] = todos_barcos[num_barco]
            elif miturno == 2:
                if num_barco <=4 and barcosj2[num_barco] == []:
                    barcosj2[num_barco] = todos_barcos[num_barco]
        if num_barco == 5 and miturno == turno:
            convertir_a_numero(j1_tablerodisparos)
            convertir_a_numero(j1_tablerobarcos)
            convertir_a_numero(j2_tablerodisparos)
            convertir_a_numero(j2_tablerobarcos)
            enviar_mensaje(conexion, partida, arch_tab)
            convertir_a_caracteres(j1_tablerodisparos)
            convertir_a_caracteres(j1_tablerobarcos)
            convertir_a_caracteres(j2_tablerodisparos)
            convertir_a_caracteres(j2_tablerobarcos)
            num_barco +=1
            try:
                mensaje = recibir_mensaje(conexion)
            except socket.herror:
                print(socket.herror)
            if mensaje:
                contenido = open(arch_tab, "w")
                contenido.write(mensaje)
                contenido.close()
                partida = json.loads(mensaje)
                j1_tablerodisparos = partida[0]["tablero disparos"]
                j1_tablerobarcos = partida[0]["tablero barcos"]
                j2_tablerodisparos = partida[1]["tablero disparos"]
                j2_tablerobarcos = partida[1]["tablero barcos"]
                turno = partida[2]["turno"]
                j1_listo = partida[2]["j1_listo"]
                j2_listo = partida[2]["j2_listo"]
                barcosj1 = partida[0]["lista barcos"]
                barcosj2 = partida[1]["lista barcos"]
                jugador1gana = partida[2]["jugador1gana"]
                jugador2gana = partida[2]["jugador2gana"]
                partida = {"Jugador 1": {"tablero disparos": j1_tablerodisparos, "tablero barcos": j1_tablerobarcos, "lista barcos": barcosj1}, 
                            "Jugador 2": {"tablero disparos": j2_tablerodisparos, "tablero barcos": j2_tablerobarcos, "lista barcos": barcosj2}, 
                            "Datos": {"turno": turno, "j1_listo": j1_listo, "j2_listo": j2_listo, "jugador1gana": jugador1gana, "jugador2gana": jugador2gana}}
                convertir_a_caracteres(j1_tablerodisparos)
                convertir_a_caracteres(j1_tablerobarcos)
                convertir_a_caracteres(j2_tablerodisparos)
                convertir_a_caracteres(j2_tablerobarcos)
                turno = partida["Datos"]["turno"]
            if miturno == 1:
                actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
            elif miturno == 2:
                actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
        if partida["Datos"]["j1_listo"] == True and partida["Datos"]["j2_listo"] == True:
            estado = "posicionar disparos"
        if turno == miturno:
            if keyboard.is_pressed('w'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if miturno == 1:
                            movimiento_barco((-1,0),barcosj1,num_barco,j1_tablerobarcos)
                        elif miturno == 2:
                            movimiento_barco((-1,0),barcosj2,num_barco,j2_tablerobarcos)
                    elif estado == "posicionar disparos":
                        if miturno == 1 and miturno == turno:
                            pos_bomba = movimiento_disparo((-1,0),pos_bomba,j1_tablerodisparos)
                        elif  miturno == 2 and miturno == turno:
                            pos_bomba = movimiento_disparo((-1,0),pos_bomba,j2_tablerodisparos)
                    if miturno == 1:
                        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
                    elif miturno == 2:
                        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
                presionado = True
            elif keyboard.is_pressed('s'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if miturno == 1:
                            movimiento_barco((1,0),barcosj1,num_barco,j1_tablerobarcos)
                        elif miturno == 2:
                            movimiento_barco((1,0),barcosj2,num_barco,j2_tablerobarcos)
                    elif estado == "posicionar disparos":
                        if miturno == 1 and miturno == turno:
                            pos_bomba = movimiento_disparo((1,0),pos_bomba,j1_tablerodisparos)
                        elif  miturno == 2 and miturno == turno:
                            pos_bomba = movimiento_disparo((1,0),pos_bomba,j2_tablerodisparos)
                    if miturno == 1:
                        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
                    elif miturno == 2:
                        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
                presionado = True
            elif keyboard.is_pressed('d'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if miturno == 1:
                            movimiento_barco((0,1),barcosj1,num_barco,j1_tablerobarcos)
                        elif miturno == 2:
                            movimiento_barco((0,1),barcosj2,num_barco,j2_tablerobarcos)
                    elif estado == "posicionar disparos":
                        if miturno == 1 and miturno == turno:
                            pos_bomba = movimiento_disparo((0,1),pos_bomba,j1_tablerodisparos)
                        elif  miturno == 2 and miturno == turno:
                            pos_bomba = movimiento_disparo((0,1),pos_bomba,j2_tablerodisparos)
                    if miturno == 1:
                        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
                    elif miturno == 2:
                        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
                presionado = True
            elif keyboard.is_pressed('a'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if miturno == 1:
                            movimiento_barco((0,-1),barcosj1,num_barco,j1_tablerobarcos)
                        elif miturno == 2:
                            movimiento_barco((0,-1),barcosj2,num_barco,j2_tablerobarcos)
                    elif estado == "posicionar disparos":
                        if miturno == 1 and miturno == turno:
                            pos_bomba = movimiento_disparo((0,-1),pos_bomba,j1_tablerodisparos)
                        elif  miturno == 2 and miturno == turno:
                            pos_bomba = movimiento_disparo((0,-1),pos_bomba,j2_tablerodisparos)
                    if miturno == 1:
                        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
                    elif miturno == 2:
                        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
                presionado = True
            elif keyboard.is_pressed('r'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if miturno == 1:
                            if barcosj1[num_barco][0][0]==barcosj1[num_barco][1][0]:
                                rotacion_a_vertical(barcosj1,num_barco,j1_tablerobarcos)
                            else:
                                rotacion_a_horizontal(barcosj1,num_barco,j1_tablerobarcos)
                        elif  miturno == 2:
                            if barcosj2[num_barco][0][0]==barcosj2[num_barco][1][0]:
                                rotacion_a_vertical(barcosj2,num_barco,j2_tablerobarcos)
                            else:
                                rotacion_a_horizontal(barcosj2,num_barco,j2_tablerobarcos)
                    if miturno == 1:
                        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
                    elif miturno == 2:
                        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
                presionado = True
            elif keyboard.is_pressed('e'):
                if presionado == False:
                    while msvcrt.kbhit():
                        msvcrt.getch()
                    if estado == "posicionar barcos":
                        if miturno == 1:
                            num_barco = confirmar_barco(barcosj1,num_barco, partida, arch_tab,j1_tablerobarcos,j1_tablerodisparos,j2_tablerobarcos,j2_tablerodisparos)
                        elif  miturno == 2:
                            num_barco = confirmar_barco(barcosj2,num_barco, partida, arch_tab,j1_tablerobarcos,j1_tablerodisparos,j2_tablerobarcos,j2_tablerodisparos)
                            partida["Jugador 2"]["tablero barcos"] = j2_tablerobarcos
                    if miturno == 1 and num_barco == 5:
                        partida["Datos"]["j1_listo"] = True
                    if  miturno == 2 and num_barco == 5:
                        partida["Datos"]["j2_listo"] = True
                    if estado == "posicionar disparos":
                        if miturno == 1 and miturno == turno:
                            confirmado = disparo(pos_bomba,tirosj1_dados,confirmado,tirosj1_fallados,j1_tablerodisparos,j2_tablerobarcos)
                        elif miturno == 2 and miturno == turno:
                            confirmado = disparo(pos_bomba,tirosj2_dados,confirmado,tirosj2_fallados,j2_tablerodisparos,j1_tablerobarcos)
                        if confirmado:
                            if miturno == 1:
                                encontrado = False
                                for barco in range(len(barcosj2)):
                                    if encontrado == False:
                                        for coordenada in range(len(barcosj2[barco])):
                                            if encontrado == False:
                                                if barcosj2[barco][coordenada][0] == pos_bomba[0] and barcosj2[barco][coordenada][1] == pos_bomba[1]:
                                                    encontrado = True
                                                    del barcosj2[barco][coordenada]
                                                    if barcosj2[barco] == []:
                                                        del barcosj2[barco]
                                                        print("\033[26;80H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                        print("\033[27;80H░██░░░██░██░░░░██░███░░░░██░██████░░██░██████░░░██████░░██░") 
                                                        print("\033[28;80H░██░░░██░██░░░░██░████░░░██░██░░░██░██░██░░░██░██░░░░██░██░") 
                                                        print("\033[29;80H░███████░██░░░░██░██░██░░██░██░░░██░██░██░░░██░██░░░░██░██░") 
                                                        print("\033[30;80H░██░░░██░██░░░░██░██░░██░██░██░░░██░██░██░░░██░██░░░░██░░░░") 
                                                        print("\033[31;80H░██░░░██░░██████░░██░░░████░██████░░██░██████░░░██████░░██░")
                                                        print("\033[32;80H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                        time.sleep(1)
                                if barcosj2 == []:
                                    partida["Datos"]["jugador1gana"] = True

                            elif miturno == 2:
                                encontrado = False
                                for barco in range(len(barcosj1)):
                                    if encontrado == False:
                                        for coordenada in range(len(barcosj1[barco])):
                                            if encontrado == False:
                                                if barcosj1[barco][coordenada][0] == pos_bomba[0] and barcosj1[barco][coordenada][1] == pos_bomba[1]:
                                                    encontrado = True
                                                    del barcosj1[barco][coordenada]
                                                    if barcosj1[barco] == []:
                                                        del barcosj1[barco]
                                                        print("\033[26;80H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                        print("\033[27;80H░██░░░██░██░░░░██░███░░░░██░██████░░██░██████░░░██████░░██░")
                                                        print("\033[28;80H░██░░░██░██░░░░██░████░░░██░██░░░██░██░██░░░██░██░░░░██░██░")
                                                        print("\033[29;80H░███████░██░░░░██░██░██░░██░██░░░██░██░██░░░██░██░░░░██░██░")
                                                        print("\033[30;80H░██░░░██░██░░░░██░██░░██░██░██░░░██░██░██░░░██░██░░░░██░░░░")
                                                        print("\033[31;80H░██░░░██░░██████░░██░░░████░██████░░██░██████░░░██████░░██░")
                                                        print("\033[32;80H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                                                        time.sleep(1)
                                if barcosj1 == []:
                                    partida["Datos"]["jugador2gana"] = True
                            convertir_a_numero(j1_tablerobarcos)
                            convertir_a_numero(j1_tablerodisparos)
                            convertir_a_numero(j2_tablerobarcos)
                            convertir_a_numero(j2_tablerodisparos)
                            enviar_mensaje(conexion, partida, arch_tab)
                            convertir_a_caracteres(j1_tablerodisparos)
                            convertir_a_caracteres(j1_tablerobarcos)
                            convertir_a_caracteres(j2_tablerodisparos)
                            convertir_a_caracteres(j2_tablerobarcos)
                            fin_de_turno = True
                            pos_bomba = (1,1)
                    if miturno == 1:
                        actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
                    elif miturno == 2:
                        actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
                presionado = True
            else:
                presionado = False
        if fin_de_turno or turno != miturno:
            if miturno == 1:
                actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
            elif miturno == 2:
                actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
            mensaje = recibir_mensaje(conexion)
            if mensaje:
                contenido = open(arch_tab, "w")
                contenido.write(mensaje)
                contenido.close()
                partida = json.loads(mensaje)
                j1_tablerodisparos = partida[0]["tablero disparos"]
                j1_tablerobarcos = partida[0]["tablero barcos"]
                j2_tablerodisparos = partida[1]["tablero disparos"]
                j2_tablerobarcos = partida[1]["tablero barcos"]
                turno = partida[2]["turno"]
                j1_listo = partida[2]["j1_listo"]
                j2_listo = partida[2]["j2_listo"]
                barcosj1 = partida[0]["lista barcos"]
                barcosj2 = partida[1]["lista barcos"]
                jugador1gana = partida[2]["jugador1gana"]
                jugador2gana = partida[2]["jugador2gana"]
                partida = {"Jugador 1": {"tablero disparos": j1_tablerodisparos, "tablero barcos": j1_tablerobarcos, "lista barcos": barcosj1}, 
                            "Jugador 2": {"tablero disparos": j2_tablerodisparos, "tablero barcos": j2_tablerobarcos, "lista barcos": barcosj2}, 
                            "Datos": {"turno": turno, "j1_listo": j1_listo, "j2_listo": j2_listo, "jugador1gana": jugador1gana, "jugador2gana": jugador2gana}}
                convertir_a_caracteres(j1_tablerodisparos)
                convertir_a_caracteres(j1_tablerobarcos)
                convertir_a_caracteres(j2_tablerodisparos)
                convertir_a_caracteres(j2_tablerobarcos)
                turno = partida["Datos"]["turno"]
        if int(radar) != radar_aux:
            if miturno == 1:
                actualizar_pantalla(barcosj1,j1_tablerobarcos,pos_bomba,j1_tablerodisparos,tirosj1_dados,radar,tirosj1_fallados,estado,turno,miturno)
            elif miturno == 2:
                actualizar_pantalla(barcosj2,j2_tablerobarcos,pos_bomba,j2_tablerodisparos,tirosj2_dados,radar,tirosj2_fallados,estado,turno,miturno)
            radar_aux += 1
            if radar >= 7:
                radar = 0
                radar_aux = 0
        radar +=0.1
        clock.tick(24)
    revancha(jugador1gana, jugador2gana, cuenta, miturno)

def revancha(jugador1gana, jugador2gana, cuenta, miturno):
    cursor.hide()
    repetir = True
    op = 0
    pygame.init()
    clock = pygame.time.Clock()
    if jugador1gana and cuenta != "None" and miturno == 1:
        os.system("cls")
        print("\033[0;65H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("\033[1;65H░██░░░██░░█████░░███████░░░░░░██████░░░█████░░███░░░░██░░█████░░██████░░░██████░░██░██") 
        print("\033[2;65H░██░░░██░██░░░██░██░░░░░░░░░░██░░░░░░░██░░░██░████░░░██░██░░░██░██░░░██░██░░░░██░██░██") 
        print("\033[3;65H░███████░███████░███████░░░░░██░░░███░███████░██░██░░██░███████░██░░░██░██░░░░██░██░██") 
        print("\033[4;65H░██░░░██░██░░░██░░░░░░██░░░░░██░░░░██░██░░░██░██░░██░██░██░░░██░██░░░██░██░░░░██░░░░░░") 
        print("\033[5;65H░██░░░██░██░░░██░███████░░░░░░██████░░██░░░██░██░░░████░██░░░██░██████░░░██████░░██░██")
        print("\033[6;65H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        time.sleep(1.5)
        diccionario_usuarios = leer_archivo()
        diccionario_usuarios[cuenta]["puntaje"] += 1
        usuarios_JSON = json.dumps(diccionario_usuarios, indent=4)
        escribir_archivo(usuarios_JSON)
    elif jugador2gana and cuenta != "None" and miturno == 2:
        os.system("cls")
        print("\033[0;65H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("\033[1;65H░██░░░██░░█████░░███████░░░░░░██████░░░█████░░███░░░░██░░█████░░██████░░░██████░░██░██") 
        print("\033[2;65H░██░░░██░██░░░██░██░░░░░░░░░░██░░░░░░░██░░░██░████░░░██░██░░░██░██░░░██░██░░░░██░██░██") 
        print("\033[3;65H░███████░███████░███████░░░░░██░░░███░███████░██░██░░██░███████░██░░░██░██░░░░██░██░██") 
        print("\033[4;65H░██░░░██░██░░░██░░░░░░██░░░░░██░░░░██░██░░░██░██░░██░██░██░░░██░██░░░██░██░░░░██░░░░░░") 
        print("\033[5;65H░██░░░██░██░░░██░███████░░░░░░██████░░██░░░██░██░░░████░██░░░██░██████░░░██████░░██░██")
        print("\033[6;65H░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        time.sleep(1.5)
        diccionario_usuarios = leer_archivo()
        diccionario_usuarios[cuenta]["puntaje"] += 1
        usuarios_JSON = json.dumps(diccionario_usuarios, indent=4)
        escribir_archivo(usuarios_JSON)
    os.system("cls")
    while repetir:
        print("\033[1;56H      ::::::::      :::       :::   :::   ::::::::::          ::::::::  :::     ::: :::::::::: ::::::::: ")
        print("\033[2;56H    :+:    :+:   :+: :+:    :+:+: :+:+:  :+:                :+:    :+: :+:     :+: :+:        :+:    :+: ")
        print("\033[3;56H   +:+         +:+   +:+  +:+ +:+:+ +:+ +:+                +:+    +:+ +:+     +:+ +:+        +:+    +:+  ")
        print("\033[4;56H  :#:        +#++:++#++: +#+  +:+  +#+ +#++:++#           +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:    ")
        print("\033[5;56H +#+   +#+# +#+     +#+ +#+       +#+ +#+                +#+    +#+  +#+   +#+  +#+        +#+    +#+    ")
        print("\033[6;56H#+#    #+# #+#     #+# #+#       #+# #+#                #+#    #+#   #+#+#+#   #+#        #+#    #+#     ")
        print("\033[7;56H########  ###     ### ###       ### ##########          ########      ###     ########## ###    ###      ")
        clock.tick(24)
        os.system("cls")
        if op == 0:
            print("\033[9;96H\033[104m Revancha \033[0m")
            print("\033[10;96H Salir ")
        elif op == 1:
            print("\033[9;96H Revancha ")
            print("\033[10;96H\033[104m Salir \033[0m")
        if keyboard.is_pressed('w'):
            if presionado == False:
                if op-1 != -1:
                    op-=1
            presionado = True
        elif keyboard.is_pressed('s'):
            if presionado == False:
                if op+1 != 2:
                    op += 1
            presionado = True
        elif keyboard.is_pressed('e'):
            while msvcrt.kbhit():
                msvcrt.getch()
            if presionado == False:
                if op == 0:
                    repetir = False
                    juego()
                elif op == 1:
                    repetir = False
                    menu()
            presionado = True
        else:
            presionado = False