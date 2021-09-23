import json
from controller.client import Client


def loginview(name, password):
    isvalid, user, figure = _login(name, password)
    if isvalid:
        print('Bem-vindo {}'.format(user.name))
        if user.showcard:
            print('\n ------------ Figurinha Adquirida no Sorteio díario ------------------')
            print("ID | NOME | RARIDADE | ")
            print(figure.idFigure, '|', figure.name, '|', figure.rarity, '\n')
        return user
    else:
        print('Nome e/ou senha inválidos')
        return None


def _login(name, password):
    client = Client()
    response = client.login(name=name, password=password)
    isvalid = response.response
    user = response.user
    figure = response.figure

    return isvalid, user, figure
