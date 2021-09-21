from controller.figura import figure
from controller.figura import figuresell


def figureview(user):
    response = figure(user)
    if response:
        balance = response[3]
        del response[3]
        print('\n ------------ Figurinhas Adquiridas ------------------')
        print("ID | NOME | RARIDADE | ")
        for fig in response:
            print(fig['idFigure'], '|', fig['name'], '|', fig['rarity'])
        print('\nseu novo saldo é de', balance, "moedas")
        print()
        return response
    else:
        print('Não foi possivel fazer a compra saldo insuficiente')
        return None


def figuresellview(user, opt):
    response = figuresell(user, opt)
    fig = response

    if response:
        print('\n ------------ Figurinhas Vendidas ------------------')
        print(fig['name'], 'por', fig['price'], 'moedas')
        print('seu novo saldo é de', fig['balance'], "moedas")
        print()
        return response
    else:
        print('Não foi possivel fazer a venda, você não possui uma ou mais cópias dessa figurinha')
        return None
