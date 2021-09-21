from controller.anunciar import anunciar


def anunciarview():
    response = anunciar()
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