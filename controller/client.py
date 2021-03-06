import grpc
import proto.message_pb2_grpc as pb2_grpc
import proto.message_pb2 as pb2


class Client(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # Instanciando o Canal
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        # Ligando o cliente e o Servidor
        self.stub = pb2_grpc.MessageStub(self.channel)

    def login(self, name, password):
        message = pb2.MessageClient(name=name, password=password)
        return self.stub.Login(message)

    def create(self, name, password):
        message = pb2.MessageClient(name=name, password=password)
        return self.stub.Create(message)

    def album(self, idUser):
        message = pb2.MessageClient(idUser=idUser)
        return self.stub.Album(message)

    def buy(self, idUser):
        message = pb2.MessageClient(idUser=idUser)
        return self.stub.Buy(message)

    def sell(self, idUser, idFigure):
        message = pb2.MessageClient(idUser=idUser, idFigure=idFigure)
        return self.stub.Sell(message)

    def createTrade(self, idUser, offer, taking):
        message = pb2.MessageClient(idUser=idUser, offer=offer, taking=taking)
        return self.stub.CreateTrade(message)

    def listTrade(self):
        message = pb2.MessageClient()
        return self.stub.ListTrade(message)

    def trade(self, idUser, idTrade):
        message = pb2.MessageClient(idUser=idUser, idTrade=idTrade)
        return self.stub.Trade(message)
