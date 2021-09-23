import json
import controller.client as clt


def anunciarview():
    response = _anunciar()
    if response:
        print("--------------------- LISTA DE TROCAS -------------------")
        for trade in response:
            print("Usuário {", trade['name'], '} - Código da Troca: {', trade['idTrade'], '}')
            print("Oferece -> ID figura: ", trade['offerID'], '- Nome: ', trade['offerName'], ' - Raridade: ',
                  trade['offerRarity'])
            print("Deseja <- ID figura: ", trade['takingID'], '- Nome: ', trade['takingName'], ' - Raridade: ',
                  trade['takingRarity'])
            print('--------------------- ------*----- -------------------')
    else:
        print('Lamentamos, mas não foi possível exibir as trocas')
        return None


def _anunciar():
    data = {
        'function': 8
    }

    response = clt.client(data=data)

    if 'response' in response:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return False
    else:
        return response
