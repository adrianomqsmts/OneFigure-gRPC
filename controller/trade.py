import json
from controller.client import Client


def trade(idUser, idTrade):
    data = {
        'function': 3,
        'idUser': idUser,
        'idTrade': idTrade
    }

    client = Client()
    message = json.dumps(data)
    result = client.get_url(message=message)
    response = json.loads(result.message)

    if response['response']:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return True
    else:
        return False
