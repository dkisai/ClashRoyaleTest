import os


# PlayerTags
# 2G00P0QJU Diego
# Y9QPJP8 Gerardo
# RPY9QYU0J Iker

def clearConsole():
    """Borra la consola independientemente del SO"""
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

    
class ClashRoyale:
    
    def __init__(self, tag):
        self.tag = tag
        self.my_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3' \
                        'MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE0NmNlNmQ1LWU4NWEtNDhhNC04MGQzLTk1ZTM0ODY4MjllYSIsI' \
                        'mlhdCI6MTYzOTI3MzEwOCwic3ViIjoiZGV2ZWxvcGVyLzU4YTViNTllLTM3MGUtZmM0NC1mOGEyLWIwNjgyN2Q3NzhkYSIsInNjb3BlcyI6WyJyb3lh' \
                        'bGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODkuMTY5LjExMi4' \
                        '4MyIsIjE4Ny4xNDAuMjA2LjE5NSJdLCJ0eXBlIjoiY2xpZW50In1dfQ._faEftsh-F-P0QGCkUfpc_s653X1H9gPXjJ-RSW0ySTTOXlX9d1N7GqMGYw' \
                        'tVUPe3D1ZVKe7JKw1gu0esNVHjg'



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
