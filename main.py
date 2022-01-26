import os
import json
import requests


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
        self.my_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc0YTcwMGExLTU3OWYtNGUxNS1iZmRiLTA5YmNkYjA0YjYyYyIsImlhdCI6MTY0MzE0OTg0Miwic3ViIjoiZGV2ZWxvcGVyLzU4YTViNTllLTM3MGUtZmM0NC1mOGEyLWIwNjgyN2Q3NzhkYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODcuMTQwLjEuMjI0Il0sInR5cGUiOiJjbGllbnQifV19.AXcf5yyTf89JV6wYOgUJhZ1NwZMZVXXn6WzwS2NrEZWjAT1DDMUFxCZTxaJEqKwlhdV2hyhekgPYfGpF8xTKDQ'


    def getData(self, url):
        head = {f'authorization': f'Bearer {self.my_token}'}
        resp = requests.get(url=url, headers=head)
        data = json.loads(resp.text)
        return data


    def getPlayerName(self):
        """Obtiene el nombre del jugador mediante el tag"""
        url = 'https://api.clashroyale.com/v1/players/' + '%23' + self.tag
        data = self.getData(url)
        return data['name']


    def getFavoriteCard(self):
        """Obtiene la carta favorita del jugador mediante el tag"""
        url = 'https://api.clashroyale.com/v1/players/' + '%23' + self.tag
        data = self.getData(url)
        return data['currentFavouriteCard']['name']


    def getWinsLosses(self):
        """Obtiene la cantidad de wins/losses del jugador mediante el tag"""
        url = 'https://api.clashroyale.com/v1/players/' + '%23' + self.tag
        data = self.getData(url)
        return f"Tienes {data['wins']} victorias y {data['losses']} derrotas al dia de hoy"


    def getNextChest(self):
        """Obtiene el siguiente cofre"""
        url = 'https://api.clashroyale.com/v1/players/' + '%23' + self.tag + '/upcomingchests'
        data = self.getData(url)
        for data['items'] in data['items']:
            return f"En tu siguente cofre te saldra {(data['items']['name'])}"
        #     print(f"Dentro de {(data['items']['index'])} cofres te saldra {(data['items']['name'])}")

    
    def checkplayertag(self):
        """Valida la etiqueta para continuar con los procesos"""
        url = 'https://api.clashroyale.com/v1/players/' + '%23' + self.tag
        head = {f'authorization': f'Bearer {self.my_token}'}
        resp = requests.get(url=url, headers=head)
        if resp.status_code == 200:
            return True
        else:
            return False


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
