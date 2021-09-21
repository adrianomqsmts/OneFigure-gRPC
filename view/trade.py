from controller.trade import trade


def tradeview(user, idTrade):
    response = trade(user['idUser'], idTrade)
    if response:
       print('A troca ocorreu com sucesso')
    else:
        print('Lamentamos, mas não foi possível finalizar a troca, verifique suas cartas')

