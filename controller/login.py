import json
from controller.client import Client


def login(name, password):
    data = {
        'function': 0,
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
