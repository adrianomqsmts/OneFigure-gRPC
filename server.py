from controller.server import server

if __name__ == '__main__':
    try:
        print('Iniciando o Servidor...')
        server()
    except Exception as e:
        print("Erro ao conectar o servidor: ", e)
