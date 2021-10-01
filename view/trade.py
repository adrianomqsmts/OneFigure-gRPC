from controller.client import Client


def tradeview(user, idTrade):
    isvalid = _trade(user.idUser, idTrade)
    if isvalid:
       print('A troca ocorreu com sucesso')
    else:
        print('Lamentamos, mas não foi possível finalizar a troca, verifique suas cartas')


def _trade(idUser, idTrade):
    client = Client()
    response = client.trade(idUser=idUser, idTrade=idTrade)
    isvalid = response.response

    return isvalid