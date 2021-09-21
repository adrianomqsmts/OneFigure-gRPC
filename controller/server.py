import grpc
from concurrent import futures
import time
import grpc
import protos.message.message_pb2_grpc as pb2_grpc
import protos.message.message_pb2 as pb2
import json
import model.user as user
import model.album as album
import model.figure as figure


class Service(pb2_grpc.MessagesServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        # Recebe os dados do cliente
        message = request.message
        print("Solicitação ->", message)

        result = self._controller(message)
        # convertendo para o padrão do protocolo
        result = {'message': result}
        print("Resposta ->", f"{result}")
        return pb2.MessageResponse(**result)



    def _controller(self, message):
        msg = json.loads(message)
        function = msg['function']
        data = msg
        if function == 0:  # Login msg = (action, name, password, date) - Verificar sorteio diário
            name = data['name']
            password = data['password']
            # strdate = now.split(" ")[0]
            resp = self._login(name, password)
            return resp
        elif function == 1:  # Vender Cartas msg = (action, idUser, idCarta, quantidade)
            idUser = data['idUser']
            idFigure = data['idFigure']
            resp = self._sell(idUser, idFigure)
            return resp
        elif function == 2:  # Comprar Carta msg = (action, idUser, idCarta, quantidade)
            idUser = data['idUser']
            resp = self._buy(idUser)
            return resp
        elif function == 3:  # Trocar Carta msg = (action, idUser, IdTrade)
            idUser = data['idUser']
            idTrade = data['idTrade']
            resp = self._trade(idUser, idTrade)
            return resp
        elif function == 4:  # Anunciar Carta msg = (action, idUser, offer, taking)
            idUser = data['idUser']
            offer = data['offer']
            taking = data['taking']
            resp = self._createTrade(idUser, offer, taking)
            return resp
        elif function == '5':  # Atualiar Cadastro msg = (action, idUser, name, password)
            return 0
        elif function == 6:  # Criar Conta msg = (action, name, password)
            name = data['name']
            password = data['password']
            resp = self._create(name, password)
            return resp
        elif function == 7:  # Ver Album msg = (action, idUser)
            idUser = data['idUser']
            resp = self._album(idUser)
            return resp
        elif function == 8:  # Ver trocas disponíveis
            resp = self._listTrade()
            return resp
        else:  # Mensagem inválida
            return -1

    def _login(self, name, password):

        database = user.login(name=name, password=password)
        if database:
            result = {
                'response': True,
                'idUser': database[0]['idUser'],
                'name': database[0]['name'],
                'password': database[0]['password'],
                'figureName': database[1]['name'],
                'idFigure': database[1]['idFigure'],
                'rarity': database[1]['rarity'],
                'showcard': database[2]['showcard'],
                'balance': database[3],
                'path': database[1]['path']
                # 'idLastLogin': ''
            }
        else:
            result = {
                'response': False,
                'idUser': '',
                'name': '',
                'password': '',
                # 'idLastLogin': ''
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _create(self, name, password):
        database = user.create(name=name, password=password)
        if database:
            result = {
                'response': True,
            }
        else:
            result = {
                'response': False,
            }

        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _album(self, idUser):
        database = album.show(id_user=idUser)
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _buy(self, idUser):
        database = figure.buy(idUser)
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _createTrade(self, idUser, offer, taking):
        database = figure.createTrade(idUser=idUser, offer=offer, taking=taking)
        if database:
            result = {
                'response': True,
            }
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _listTrade(self):
        database = figure.listTrade()
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)
        return data

    def _sell(self, idUser, idFigure):
        database = figure.sell(idUser, idFigure)
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

    def _trade(self, idUser, idTrade):
        database = figure.trade(idUser, idTrade)
        if database:
            result = {
                'response': True,
            }
        else:
            result = {
                'response': False,
            }
        data = json.dumps(result)  # convertendo para dicionário
        return data

def server():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MessagesServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
