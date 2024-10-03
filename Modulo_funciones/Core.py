import os
import pygame
import keyboard
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
def juego():
    pygame.init()
    clock = pygame.time.Clock()
    j1_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j1_tablerobarcos   = [
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    j2_tablerodisparos= [["╔","═","═","═","═","═","═","═","═","═","═","╗"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["║","░","░","░","░","░","░","░","░","░","░","║"],
                         ["╠","═","═","═","═","═","═","═","═","═","═","╣"]]
    j2_tablerobarcos   = [
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["║","░","░","░","░","░","░","░","░","░","░","║"],
                          ["╚","═","═","═","═","═","═","═","═","═","═","╝"]]
    game = True
    while game ==  True:
        if keyboard.is_pressed('w'):
            print("w")
        if keyboard.is_pressed('s'):
            print("s")
        if keyboard.is_pressed('d'):
            print("d")
        if keyboard.is_pressed('a'):
            print("a")
        # dibujar(j1_tablerobarcos)
        # dibujar(j1_tablerodisparos)
        clock.tick(30)
        os.system("cls")
equipo = ["Diaz, German Ezequiel", "Nuñez Gagliano, Francisco Dario", "Ragagnin, Nicolas",
          "Salas, Agustin Ezequiel", "Sandoval, Marianella", "Trimarco, Tomas"]
#menu de inicio,2 proyecto, 1 equipo, y 4 ejecutar para salir
