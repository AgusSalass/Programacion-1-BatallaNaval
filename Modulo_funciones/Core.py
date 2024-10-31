import os
import pygame
import keyboard
import copy
import cursor
import json
import sys

def mostrar_equipo():
    print("Este es nuestro equipo")
    for miembro in equipo:
        print(miembro)


def mostrar_proyecto():
    print("Nuestro proyecto se trata sobre el juego de mesa Batalla Naval:\n El mismo será realizado usando un formato via terminal en ASCII, y contará \n con un modo multijugador en linea, en el cual cada jugador podrá \n colocar a libertad sus barcos, bombardear el lado enemigo del tablero, y recibir \n feedback en tiempo real de los resultados de sus acciones en una partida por turnos.") #TODO revisar esta funcion

def menu():
    repetir = True
    while repetir:
        os.system("cls")
        print ("1-Equipo")
        print ("2-Proyecto")
        print ("4-Salir")
        try:
            op=int(input("Elija una opcion: "))
            
            if op == 1:
                mostrar_equipo()
            elif op == 2:
                mostrar_proyecto()
            elif op == 4:
                repetir=False
            elif op == 5:
                juego()
            else:
                print("Opcion invalida")
            input()
        except TypeError:
            print("Error, debe usar un numero")
            print(TypeError)
            input()
            
def dibujar(tablero):
    for fila in tablero:
        for columna in fila:
            print(columna,end="")
        print()
        
def generar_tablero():
    pass

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
            tablero[old_x][old_y] = (f"\033[36m ~\033[0m")
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
            tablero_barcos[coordenada[0]][coordenada[1]] = (f"\033[90m ≡\033[0m")
            
def rotacion_a_vertical(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = (f"\033[36m ~\033[0m")
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
            tablero[old_x][old_y] = (f"\033[36m ~\033[0m")
            new_x = old_x - coordenada
            new_y = old_y + coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)

def confirmar_barco(barcos,barco,partido,arch_tablero):
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
        print("Creando")
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
        tablero_disparos[coordenada[0]][coordenada[1]] = (f"\033[31m ¤\033[0m")
    tablero_disparos[disparo[0]][disparo[1]] = (f"\033[37m ¤\033[0m")

def movimiento_disparo(direccion,bomba,tablero):
    posible = True
    if posible:
        old_x,old_y = bomba
        tablero[old_x][old_y] = (f"\033[36m ~\033[0m")
        x,y = direccion
        new_x = old_x + x
        new_y = old_y + y
        if new_x <= 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero)-1:
            posible = False
        else:
            bomba = (new_x,new_y)
    return bomba

def confirmar_tiro(posicion_tiro,tiros,confirmable, partido):
#TODO el primer parámetro tiene que ser el nombre que le demos a la posición actual del disparo
    confirmable = True
    if tiros == []:
        print("1")
        return confirmable
    else:
        for tiro in range(len(tiros)):
            print("2")
            if tiros[tiro] == posicion_tiro:
                print("3")
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
                if not lista_barcos[i]:
                    del lista_barcos[i]
            j += 1
        i += 1

def juego():
    cursor.hide()
    pygame.init()
    clock = pygame.time.Clock()
    path_tableros = os.path.dirname(os.path.abspath(__file__))
    arch_tab = os.path.join(path_tableros, f"Tableros.json")
    o = (f"\033[36m ~\033[0m")
    b = (f"\033[90m ≡\033[0m")
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
        """
        
        Esta sección toma los inputs del teclado, en caso de querer agregar una nueva tecla, se añade otro
        elif con la tecla deseada, y se usa el mismo formato con la bandera "presionado"
        
        """
        if turno == miturno:
            if keyboard.is_pressed('w'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((-1,0),barcosj1,num_barco,partida["Jugador 1"]["tablero barcos"])
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((-1,0),pos_bomba,partida["Jugador 1"]["tablero disparos"])
                presionado = True
            elif keyboard.is_pressed('s'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((1,0),barcosj1,num_barco,partida["Jugador 1"]["tablero barcos"])
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((1,0),pos_bomba,partida["Jugador 1"]["tablero disparos"])
                presionado = True
            elif keyboard.is_pressed('d'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((0,1),barcosj1,num_barco,partida["Jugador 1"]["tablero barcos"])
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((0,1),pos_bomba,partida["Jugador 1"]["tablero disparos"])
                presionado = True
            elif keyboard.is_pressed('a'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        movimiento_barco((0,-1),barcosj1,num_barco,partida["Jugador 1"]["tablero barcos"])
                    elif estado == "posicionar disparos":
                        pos_bomba = movimiento_disparo((0,-1),pos_bomba,partida["Jugador 1"]["tablero disparos"])
                presionado = True
            elif keyboard.is_pressed('r'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        if barcosj1[num_barco][0][0]==barcosj1[num_barco][1][0]:
                            rotacion_a_vertical(barcosj1,num_barco,j1_tablerobarcos)
                        else:
                            rotacion_a_horizontal(barcosj1,num_barco,j1_tablerobarcos)#TODO cuando se pone la direccion con el diccionario se rompe
                presionado = True
            elif keyboard.is_pressed('enter'):
                if presionado == False:
                    if estado == "posicionar barcos":
                        num_barco = confirmar_barco(barcosj1,num_barco, partida, arch_tab)
                    elif estado =="posicionar disparos":
                        confirmado = confirmar_tiro(pos_bomba,tirosj1,confirmado, partida, arch_tab)
                        print("6")
                        if confirmado:
                            print("7")
                            tirosj1.append(pos_bomba)
                            print("8")
                            pos_bomba = (1,1)
                presionado = True
            else:
                presionado = False
        else:
            print("Esperando oponente...")
        sys.stdin.flush()
        visualizar_barco(barcosj1,partida["Jugador 1"]["tablero barcos"])
        visualizar_disparos(pos_bomba,j1_tablerodisparos,tirosj1)
        dibujar(j1_tablerodisparos)
        dibujar(partida["Jugador 1"]["tablero barcos"])
        print(tirosj1)
        clock.tick(24)
        os.system("cls")
equipo = ["Diaz, German Ezequiel", "Nuñez Gagliano, Francisco Dario", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella Jazmín", "Trimarco, Tomas","McLovin"]
#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir