import json
import controller.client as clt


def offerview(user, offer, taking):
    response = _offer(user, offer, taking)
    if response:
        print('A troca foi anunciada')
    else:
        print('Lamentamos, mas não alguma coisa não está correta (quantidade insuficente ou ID incorreto)')
        return None


def _offer(user, offer, taking):
    data = {
        'function': 4,
        'idUser': user['idUser'],
        'offer': offer,
        'taking': taking
    }

    response = clt.client(data=data)

    if response['response']:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return True
    else:
        return False
