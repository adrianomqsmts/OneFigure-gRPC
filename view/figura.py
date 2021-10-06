import json
from controller.client import Client


def figureview(user):
    isvalid, balance, figures = _figure(user)
    if isvalid:
        print('\n ------------ Figurinhas Adquiridas ------------------')
        print("ID | NOME | RARIDADE | ")
        for figure in figures:
            print(figure.idFigure, '|', figure.name, '|', figure.rarity)
        print('\nseu novo saldo é de', balance, "moedas")
        print()
        return figures
    else:
        print('Não foi possivel fazer a compra saldo insuficiente')
        return None


def _figure(user):
    client = Client()
    response = client.buy(idUser=user.idUser)
    isvalid = response.response
    balance = response.balance
    figures = response.figures
    return isvalid, balance, figures


def figuresellview(user, figure):
    isvalid, price, name = _figuresell(user, figure)

    if isvalid:
        print('\n ------------ Figurinhas Vendidas ------------------')
        print(name, 'por', price, 'moedas')
        print()
        return isvalid, name, price
    else:
        print('Não foi possivel fazer a venda, você não possui uma ou mais cópias dessa figurinha')
        return None, None, None


def _figuresell(user, idFigure):
    client = Client()
    response = client.sell(idUser=user.idUser, idFigure=int(idFigure))
    isvalid = response.response
    price = response.price
    name = response.name
    return isvalid, price, name
