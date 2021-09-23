import json

from controller.client import Client

import controller.client as clt
from tkinter import *
import view.login as vl
import view.singin as vs
import view.album as al
import view.figura as fg
import view.offer as of
import view.anunciar as va
import view.trade as vt

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    user = None
    print('Iniciando a aplicação...')
    while True:  # WHILE LOGIN
        option = input("1 - login | 2 - Criar conta | 0 - Sair: ")
        if option == '1':
            name = input('Nome: ')
            password = input('Password: ')
            response = vl.loginview(name=name, password=password)
            if response:
                user = response  # Armazenar os dados do usuário
                while True:  # WHILE menu principal
                    option = input("1 - Álbum | 2 - Comprar | 3 - Vender | 4 - Menu de Trocas | 0 - Sair: ")
                    if option == '1':
                        response = al.albumview(user)
                        pass
                    elif option == '2':
                        opt = int(input("Você deseja confirmar a compra ? (custo 25 moedas)\n"
                                    "              1 - SIM | 2 - NÃO\n"))

                        if opt != 1:
                            continue
                        response = fg.figureview(user)
                    elif option == '3':
                        id = input("Digite o ID da figurinha que deseja vender: ")
                        if id.isnumeric() and 1 <= int(id) <= 50:
                            id = int(id)
                            opt = int(input("Você deseja confirmar a venda ? 1 - SIM | 2 - NÃO: "))
                            if opt != 1:
                                continue
                            response = fg.figuresellview(user, id)
                        else:
                            print('ID invalído')
                        pass
                    elif option == '4':
                        while True:
                            opt = int(input("1 - Anunciar | 2 - Ver Trocas | 3 - Trocar | 0 - Voltar: "))
                            if opt == 1:
                                offer = int(input("ID da figurinha oferecida: "))
                                taking = int(input("ID da carta que quer receber em troca: "))
                                of.offerview(user, offer, taking)
                            elif opt == 2:
                                va.anunciarview()
                            elif opt == 3:
                                id = input("Digite o código da troca: ")
                                if id.isnumeric():
                                    id = int(id)
                                    opt = int(input("Você deseja confirmar a troca ?  1 - SIM | 2 - NÃO: "))

                                    if opt != 1:
                                        continue
                                    vt.tradeview(user, id)
                                else:
                                    print('Opção inválida')
                            elif opt == 0:
                                break
                            else:
                                print('Opção inválida')

                    elif option == '0':
                        user = None  # limpar os dados do usuário
                        break
                    else:
                        print('Opção inválida, tente novamente...')
        elif option == '2':
            name = input('Nome: ')
            password = input('Password: ')
            vs.singinview(name=name, password=password)
        else:
            break

# if __name__ == '__main__':
#     client = Client()
#     name = 'fulano'
#     password = 'fulano'
#     result = client.login(name=name, password=password)
#     response = result.response
#     user = result.user
#     print(user.idUser)
