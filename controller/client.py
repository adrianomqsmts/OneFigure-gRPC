import grpc
import protos.message.message_pb2_grpc as pb2_grpc
import protos.message.message_pb2 as pb2


class Client(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # Instanciar o canal
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        # Conectar o cliente e o servidor
        self.stub = pb2_grpc.MessagesStub(self.channel)

    def get_url(self, message):
        # Prototipando a mensagem
        message = pb2.Message(message=message)
        # Recebendo e retornando a resposta
        return self.stub.GetServerResponse(message)
