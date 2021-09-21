from controller.offer import offer


def offerview(user, offer2, taking):
    response = offer(user, offer2, taking)
    if response:
        print('A troca foi anunciada')
    else:
        print('Lamentamos, mas não alguma coisa não está correta (quantidade insuficente ou ID incorreto)')
        return None
