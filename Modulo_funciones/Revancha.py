import keyboard
import os
import pygame
import cursor

def menu():
    pass

def juego():
    pass

def revancha():
    cursor.hide()
    repetir = True
    op = 0
    pygame.init()
    clock = pygame.time.Clock()
    while repetir:
        print("\033[1;25H      ::::::::      :::       :::   :::   ::::::::::          ::::::::  :::     ::: :::::::::: ::::::::: ")
        print("\033[2;25H    :+:    :+:   :+: :+:    :+:+: :+:+:  :+:                :+:    :+: :+:     :+: :+:        :+:    :+: ")
        print("\033[3;25H   +:+         +:+   +:+  +:+ +:+:+ +:+ +:+                +:+    +:+ +:+     +:+ +:+        +:+    +:+  ")
        print("\033[4;25H  :#:        +#++:++#++: +#+  +:+  +#+ +#++:++#           +#+    +:+ +#+     +:+ +#++:++#   +#++:++#:    ")
        print("\033[5;25H +#+   +#+# +#+     +#+ +#+       +#+ +#+                +#+    +#+  +#+   +#+  +#+        +#+    +#+    ")
        print("\033[6;25H#+#    #+# #+#     #+# #+#       #+# #+#                #+#    #+#   #+#+#+#   #+#        #+#    #+#     ")
        print("\033[7;25H########  ###     ### ###       ### ##########          ########      ###     ########## ###    ###      ")
        clock.tick(24)
        os.system("cls")
        if op == 0:
            print("\033[9;70H\033[104m Revancha \033[0m")
            print("\033[10;70H Rendirse ")
        elif op == 1:
            print("\033[9;70H Revancha ")
            print("\033[10;70H\033[104m Rendirse \033[0m")
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
revancha()