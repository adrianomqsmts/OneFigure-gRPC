import json
from controller.client import Client


def offerview(user, offer, taking):
    isvalid = _offer(user, offer, taking)
    if isvalid:
        print('A troca foi anunciada')
        return isvalid
    else:
        print('Lamentamos, mas não alguma coisa não está correta (quantidade insuficente ou ID incorreto)')
        return None


def _offer(user, offer, taking):
    client = Client()
    response = client.createTrade(idUser=user.idUser, offer=offer, taking=taking)
    isvalid = response.response

    return isvalid
