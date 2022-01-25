import os


if __name__ == "__main__":
    ok = False
    bye = 1
    oktag = ''
    while not ok:
        tag = input('          Hola \n Teclea tu etiqueta de ClashRoyale\n')
        tag = tag.upper().replace('O', '0')
        tag = list(tag)
        if tag[0] == '#':
            tag = tag[1:]
        oktag = oktag.join(tag)

        crplayer = ClashRoyale(oktag)

        if crplayer.checkplayertag() == True:
            print(f'Tu etiqueta es {oktag}\n')
        else:
            print('Tu etiqueta tiene un error, presiona 0 para corregir')
            os.system('exit')
        ok = int(input('¿Es correcto? \n 1 = SI \n 0 = No, Corregir\n '))
    clearConsole()
    while bye != 0:
        print('Hola ' + crplayer.getPlayerName() + ' bienvenido')
        bye = int(input('¿Que deseas hacer?\n\n'
                        '1.- Saber tu siguente cofre \n'
                        '2.- Saber tu carta favorita \n'
                        '3.- Victorias y derrotas \n'
                        '0.- Salir\n'))
        if bye == 1:
            print(crplayer.getNextChest())
        elif bye == 2:
            print(crplayer.getFavoriteCard())
        elif bye == 3:
            print(crplayer.getWinsLosses())
        else:
            bye = 0
