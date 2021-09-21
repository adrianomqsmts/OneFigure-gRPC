from controller.login import login


def loginview(name, password):
    response = login(name, password)

    if response:
        print('Bem-vindo {}'.format(response['name']))
        if response['showcard'] == 1:
            print('\n ------------ Figurinha Adquirida no Sorteio díario ------------------')
            print("ID | NOME | RARIDADE | ")
            print(response['idFigure'], '|', response['figureName'], '|', response['rarity'],'\n')
        # print(response)
        return response
    else:
        print('Nome e/ou senha inválidos')
        return None
