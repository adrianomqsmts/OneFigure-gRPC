import json
from controller.client import Client


def singin(name, password):
    data = {
        'function': 6,
        'name': name,
        'password': password
    }

    client = Client()
    message = json.dumps(data)
    result = client.get_url(message=message)
    response = json.loads(result.message)

    if response['response']:
        return response
    else:
        return 0
