import sql.user as sql_user

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class User(object):
        def __init__(self, name, username):
            self.name = name
            self.username = username


    import json

    j = json.loads('{"name": "Teste", "username": "username"}')
    u = User(**j)

    print(u.name)

    out = sql_user.login2('fulano', 'fulano')

    print(f"{out}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
