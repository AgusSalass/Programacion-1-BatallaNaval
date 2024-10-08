import os
import pygame
import keyboard
import copy

def mostrar_equipo():
    print("Este es nuestro equipo")
    for miembro in equipo:
        print(miembro)


def mostrar_proyecto():
    print("Nuestro proyecto se trata sobre el juego de mesa Batalla Naval:\n El mismo será realizado usando un formato via terminal en ASCII, y contará \n con un modo multijugador en linea, en el cual cada jugador podrá \n colocar a libertad sus barcos, bombardear el lado enemigo del tablero, y recibir \n feedback en tiempo real de los resultados de sus acciones en una partida por turnos.") #TODO revisar esta funcion

#menu
def menu():
    repetir = True
    while repetir:
        os.system("cls")
        print ("1-Equipo")
        print ("2-Proyecto")
        print ("4-Salir")
        try:
            op=int(input("Eliga una opcion: "))
            
            if op==1:
                mostrar_equipo()
            elif op==2:
                mostrar_proyecto()
            elif op==4:
                repetir=False
            elif op == 5:
                juego()
            else:
                print("Opcion invalida")
            input()
        except:
            print("Error, debe usar un numero")
            input()
            
def dibujar(tablero):
    for fila in tablero:
        for columna in fila:
            print(columna,end="")
        print()
        
def generar_tablero():
    pass

def movimiento_barco(direccion,barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for i in range(len(barcos[barco])):
        if posible:
            old_x,old_y = barcos[barco][i]
            tablero[old_x][old_y] = "~"
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
            tablero_barcos[coordenada[0]][coordenada[1]] = "≡"
            
def rotacion_vertical(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[0])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = "~"
            new_x = old_x + coordenada
            new_y = old_y - coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)
        
def rotacion_horizontal(barcos,barco,tablero):
    aux = copy.deepcopy(barcos[barco])
    posible = True
    for coordenada in range(len(barcos[0])):
        if posible:
            old_x,old_y = barcos[barco][coordenada]
            tablero[old_x][old_y] = "~"
            new_x = old_x - coordenada
            new_y = old_y + coordenada
            if new_x < 0 or new_x >= len(tablero)-1 or new_y <= 0 or new_y  >= len(tablero):
                posible = False
                barcos[barco] = copy.deepcopy(aux)
            else:
                barcos[barco][coordenada]=(new_x,new_y)
        
def juego():
    pygame.init()
    clock = pygame.time.Clock()
    barcosj1 = [[(1,1),(1,2),(1,3),(1,4)]]

    portaaviones ="≡"
    mulportaaviones = 5
    destructor = "≡"
    muldestructor = 4
    crucero1 = "destruido"
    mulcrucero1= 1
    crucero2 ="≡"
    mulcrucero2 = 3
    lancha="≡"
    mullancha = 2
    # ░≡¤
    j1_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗","portaaviones: ",portaaviones*mulportaaviones],
                         ["║","~","~","~","~","~","~","~","~","~","~","║","destructor: ",destructor*muldestructor],
                         ["║","~","░","~","~","~","~","~","~","~","~","║","crucero: ",crucero1*mulcrucero1],
                         ["║","~","~","~","~","~","~","~","~","░","~","║","crucero: ",crucero2*mulcrucero2],
                         ["║","~","~","~","~","~","~","~","~","~","~","║","lancha: ", lancha*mullancha],
                         ["║","~","~","~","¤","¤","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","░","░","░","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j1_tablerobarcos   = [
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    j2_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["║","~","~","~","~","~","~","~","~","~","~","║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j2_tablerobarcos   = [
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["║","~","~","~","~","~","~","~","~","~","~","║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    barcosj1 = [[(1,1),(1,2),(1,3)]]
    game = True
    while game ==  True:
        #Esta sección toma los inputs del teclado, en caso de querer agregar una nueva tecla, se añade otro
        #elif con la tecla deseada, y se usa el mismo formato con la bandera "presionado"
        estado = "posicionar barcos"
        if keyboard.is_pressed('w'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((-1,0),barcosj1,0,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('s'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((1,0),barcosj1,0,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('d'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((0,1),barcosj1,0,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('a'):
            if presionado == False:
                if estado == "posicionar barcos":
                    movimiento_barco((0,-1),barcosj1,0,j1_tablerobarcos)
            presionado = True
        elif keyboard.is_pressed('r'):
            if presionado == False:
                if estado == "posicionar barcos":
                    if barcosj1[0][0][0]==barcosj1[0][1][0]:
                        rotacion_vertical(barcosj1,0,j1_tablerobarcos)
                    else:
                        rotacion_horizontal(barcosj1,0,j1_tablerobarcos)
            presionado = True
        else:
            presionado = False
        visualizar_barco(barcosj1,j1_tablerobarcos)
        dibujar(j1_tablerodisparos)
        dibujar(j1_tablerobarcos)
        clock.tick(24)
        os.system("cls")
equipo = ["Diaz, German Ezequiel", "Nuñez Gagliano, Francisco Dario", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella Jazmín", "Trimarco, Tomas"]
#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir