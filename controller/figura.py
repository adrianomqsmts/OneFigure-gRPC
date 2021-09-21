import json
from controller.client import Client


def figure(user):
    data = {
        'function': 2,
        'idUser': user['idUser']
    }

    client = Client()
    message = json.dumps(data)
    result = client.get_url(message=message)
    response = json.loads(result.message)

    if 'response' in response:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return 0
    else:
        return response


def figuresell(user, opt):
    data = {
        'function': 1,
        'idUser': user['idUser'],
        'idFigure': opt
    }

    client = Client()
    message = json.dumps(data)
    result = client.get_url(message=message)
    response = json.loads(result.message)

    if 'response' in response:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return 0
    else:
        return response
