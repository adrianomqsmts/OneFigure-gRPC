from controller.client import Client


def singinview(name, password):
    response = _singin(name, password)
    if response:
        print('Conta criada com sucesso.')
    else:
        print('Não foi possível criar a conta, possívelmente o nome já existe')
    return response


def _singin(name, password):
    client = Client()
    response = client.create(name=name, password=password)
    isvalid = response.response

    return isvalid
