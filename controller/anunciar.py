import json
from controller.client import Client


def anunciar():
    data = {
        'function': 8
    }

    client = Client()
    message = json.dumps(data)
    result = client.get_url(message=message)
    response = json.loads(result.message)

    if 'response' in response:  # Se tiver o campo responde dentro da resposta, então houve algum tipo de erro
        return False
    else:
        return response
