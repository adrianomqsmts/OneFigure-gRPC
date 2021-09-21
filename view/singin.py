from controller.singin import singin


def singinview(name, password):
    response = singin(name, password)
    if response:
        print('Conta criada com sucesso.')
        return response
    else:
        print('Não foi possível criar a conta, possívelmente o nome já existe')
        return None
