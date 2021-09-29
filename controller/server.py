import grpc
from concurrent import futures
import time

import proto.message_pb2
import proto.message_pb2_grpc as pb2_grpc
import proto.message_pb2 as pb2
import model.user as user
import model.album as album
import model.figura as figure
import json
import socket
from threading import Thread
from datetime import datetime


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
                figure = database[2]
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
            figures = database[0]
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
        print(f'{database}')
        if database:
            result = database
        else:
            result = {
                'response': False,
            }
        out = {
            'response': False,
            'complete': 0,
            'special': None,
            'figures': None,
        }
        return pb2.AlbumResponse(**out)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MessageServicer_to_server(MessageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('SERVER..')
    server.wait_for_termination()
