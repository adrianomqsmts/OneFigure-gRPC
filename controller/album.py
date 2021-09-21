import json
from controller.client import Client


def album(user):
    data = {
        'function': 7,
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
