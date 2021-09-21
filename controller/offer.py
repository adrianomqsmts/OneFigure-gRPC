import json
from controller.client import Client


def offer(user, offer, taking):
    data = {
        'function': 4,
        'idUser': user['idUser'],
        'offer': offer,
        'taking': taking
    }

    client = Client()
    message = json.dumps(data)
    result = client.get_url(message=message)
    response = json.loads(result.message)

    if response['response']:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return True
    else:
        return False
