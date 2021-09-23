import json
import controller.client as clt


def tradeview(user, idTrade):
    response = _trade(user['idUser'], idTrade)
    if response:
       print('A troca ocorreu com sucesso')
    else:
        print('Lamentamos, mas não foi possível finalizar a troca, verifique suas cartas')


def _trade(idUser, idTrade):
    data = {
        'function': 3,
        'idUser': idUser,
        'idTrade': idTrade
    }

    response = clt.client(data=data)

    if response['response']:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return True
    else:
        return False
