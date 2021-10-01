import grpc
from concurrent import futures
import proto.message_pb2_grpc as pb2_grpc
import proto.message_pb2 as pb2
import model.user as user
import model.album as album
import model.figura as figure


class MessageService(pb2_grpc.MessageServicer):

    def __init__(self, *args, **kwargs):
        pass

    def Login(self, request, context):
        print('Login -> Name:',  request.name, ' - Password: ', request.password)

        name = request.name
        password = request.password
        database = user.login(name=name, password=password)
        if database:
            usuario = {
                'idUser': int(database[0]['idUser']),
                'name': database[0]['name'],
                'balance': float(database[3]),
                'password': database[0]['password'],
                'showcard': int(database[2]['showcard']),
            }

            if int(database[2]['showcard']):
                figure = {
                    'idFigure': database[1]['idFigure'],
                    'rarity': database[1]['rarity'],
                    'name': database[1]['name']
                }
            else:
                figure = None

            out = {'response': True, 'user': usuario, 'figure': figure}
        else:
            out = {'response': False, 'user': None, 'figure': None}
        print('Response <- ', f'{out}')
        return pb2.LoginResponse(**out)

    def Create(self, request, context):
        print('Create -> Name:', request.name, ' - Password: ', request.password)
        name = request.name
        password = request.password
        database = user.create(name=name, password=password)
        if database:
            result = {
                'response': True,
            }
        else:
            result = {
                'response': False,
            }
        print('Response <- ', f'{result}')
        return pb2.Response(**result)

    def Album(self, request, context):

        print('Album -> IdUser:', request.idUser)
        idUser = request.idUser
        database = album.show(id_user=idUser)
        if database:
            complete = int(database[1]['complete'])
            if complete:
                special = database[2]
            else:
                special = None
            figures = []
            for data in database[0]:
                figures.append({
                    'idFigure': data['idFigure'],
                    'name': data['name'],
                    'rarity': data['rarity'],
                    'path': data['path'],
                    'quantity': data['quantity']
                })
            out = {
                'response': True,
                'complete': complete,
                'special': special,
                'figures': figures,
            }
        else:
            out = {
                'response': False,
                'complete': 0,
                'special': None,
                'figures': None,
            }
        print('Response <- ', f'{out}')
        return pb2.AlbumResponse(**out)

    def Buy(self, request, context):
        print('Buy -> IdUser:', request.idUser)
        idUser = request.idUser
        database = figure.buy(idUser)
        result = []
        if database:
            balance = float(database[3])
            del database[3]
            for i in range(3):
                result.append({
                    'idFigure': database[i]['idFigure'],
                    'rarity': database[i]['rarity'],
                    'name': database[i]['name']
                })
            figures = result
            out = {
                'response': True,
                'balance': balance,
                'figures': figures,
            }
        else:
            out = {
                'response': False,
                'balance': None,
                'figures': None,
            }
        print('Response <- ', f'{out}')
        return pb2.AlbumResponse(**out)

    def CreateTrade(self, request, context):
        print('Create Trade -> IdUser:', request.idUser, ' - Offer ID:', request.offer, ' - Taking ID:', request.taking)
        idUser = request.idUser
        offer = request.offer
        taking = request.taking
        if (offer >= 0) and (taking >= 0) and (offer <= 50) and (taking <= 50):
            database = figure.createTrade(idUser=idUser, offer=offer, taking=taking)
            if database:
                out = {
                 'response': True,
                }
            else:
                out = {
                 'response': False,
                }
        else:
            out = {
                'response': False,
            }
        print('Response <- ', f'{out}')
        return pb2.Response(**out)

    def ListTrade(self, request, context):
        print('Listar Trocas -> ')
        database = figure.listTrade()
        if database:
            result = []
            for data in database:
                result.append({
                    'name': data['name'],
                    'idTrade': data['idTrade'],
                    'offerID': data['offerID'],
                    'offerName': data['offerName'],
                    'offerRarity': data['offerRarity'],
                    'takingID': data['takingID'],
                    'takingName': data['takingName'],
                    'takingRarity': data['takingRarity']
                })
            out = {
                'response': True,
                'list': result
            }
        else:
            out = {
                'response': False,
                'list': None
            }
        print('response <-', f'{result}')
        return pb2.ListTradeResponse(**out)

    def Sell(self, request, context):
        print('Sell -> ID User: ', request.idUser, ' - ID Figure: ', request.idFigure)
        database = figure.sell(request.idUser, request.idFigure)
        print(database)
        if database:
            name = database['name']
            price = float(database['price'])
            out = {
                'response': True,
                'price': price,
                'name': name
            }
        else:
            out = {
                'response': False,
                'price': None,
                'name': None
            }
        print('Response <- ', out)
        return pb2.SellResponse(**out)

    def Trade(self, request, context):
        print('Trade -> ID User: ', request.idUser, ' - ID Trade: ', request.idTrade)
        idUser = request.idUser
        idTrade = request.idTrade
        database = figure.trade(idUser, idTrade)
        if database:
            out = {
             'response': True
            }
        else:
            out = {
             'response': False
            }
        print('Responde <- ', out)
        return pb2.Response(**out)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MessageServicer_to_server(MessageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('SERVER..')
    server.wait_for_termination()
