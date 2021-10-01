import json
from controller.client import Client


def anunciarview():
    isvalid, trades = _anunciar()
    if isvalid:
        print("--------------------- LISTA DE TROCAS -------------------")
        for trade in trades:
            print("Usuário {", trade.name, '} - Código da Troca: {', trade.idTrade, '}')
            print("Oferece -> ID figura: ", trade.offerID, '- Nome: ', trade.offerName, ' - Raridade: ',
                  trade.offerRarity)
            print("Deseja <- ID figura: ", trade.takingID, '- Nome: ', trade.takingName, ' - Raridade: ',
                  trade.takingRarity)
            print('--------------------- ------*----- -------------------')
    else:
        print('Lamentamos, mas não foi possível exibir as trocas')
        return None


def _anunciar():

    client = Client()
    response = client.listTrade()
    isvalid = response.response
    trades = response.list

    return isvalid, trades
