from tkinter import *
import view.login as vl
import view.singin as vs
import view.album as al
import view.figura as fg
import view.offer as of
import view.anunciar as va
import view.trade as vt
import controller.client as clt


class Interface:
    def __init__(self, master=None):
        # FONT AND FRAMES
        self.font = ("Comic Sans MS", "12")
        self.frame = Frame(root, bg="#565656")
        self.frame.pack()
        self.frame2 = Frame(root, bg="#565656")
        self.frame2.pack()
        self.frame3 = Frame(root, bg="#565656")
        self.frame3.pack()
        self.frame4 = Frame(root, bg="#565656")
        self.frame4.pack()
        self.response = ''
        self.current = -1
        self.showed = 0
        self.image_list = []
        self.quantity_list = []
        # MENU 1
        self.mylabel = Label(self.frame, text="Menu", font=("Comic Sans MS", 15, "bold"), pady=10, fg="white",
                             bg="#565656")
        self.login = Button(self.frame, text="Login",
                            font=self.font, pady=10,
                            width=30, command=self.menuLogin,
                            bg="#f4a259")
        self.singin = Button(self.frame, text="Criar Conta",
                             font=self.font, pady=10,
                             width=30, command=lambda: self.menuSingin(),
                             bg="#ffd166")
        self.exit = Button(self.frame, text="Sair",
                           font=self.font, pady=10,
                           width=30, command=root.quit,
                           bg="#ff5c5c")
        self.openMenu1()
        # MENU 2
        self.usernametext = Label(self.frame, text="Username",
                                  font=("Comic Sans MS", 13), pady=10,
                                  fg="#dad7cd", bg="#565656")
        self.usernameinput = Entry(self.frame, width=30, font=("Arial", "12"))
        self.passwordtext = Label(self.frame2, text="Senha",
                                  font=("Comic Sans MS", 13), pady=10,
                                  fg="#dad7cd", bg="#565656")
        self.passwordinput = Entry(self.frame2, width=30, font=("Arial", "12"))
        self.loginsubmit = Button(self.frame3, text="Login",
                                  font=self.font, pady=10,
                                  width=10, command=lambda: self.submitLogin(),
                                  bg="#f4a259")
        self.back = Button(self.frame3, text="Voltar",
                           font=self.font, pady=10,
                           width=10, command=lambda: self.openMenu1(),
                           bg="#ff5c5c")
        self.msgerro = Label(self.frame4, text="Username ou Senha Inválidos", fg="red", font=self.font, bg="#565656")
        # MENU 3
        self.mylabel = Label(self.frame, text="Menu", font=("Comic Sans MS", 15, "bold"), pady=10, fg="white",
                             bg="#565656")
        self.album = Button(self.frame, text="Ver Album",
                            font=self.font, pady=10,
                            width=30, command=lambda: self.albumview(),
                            bg="#5b8e7d")
        self.buy = Button(self.frame, text="Comprar Figuras",
                          font=self.font, pady=10,
                          width=30, command=lambda: self.buyview(),
                          bg="#c1ddeb")
        self.sell = Button(self.frame, text="Vender Figuras",
                           font=self.font, pady=10,
                           width=30, command=lambda: self.sellview(),
                           bg="#8cb369")
        self.trade = Button(self.frame, text="Trocar Figuras",
                            font=self.font, pady=10,
                            width=30, command=self.tradeview,
                            bg="#f5be51")
        self.back2 = Button(self.frame, text="Sair",
                            font=self.font, pady=10,
                            width=30, command=lambda: self.openMenu1(),
                            bg="#ff5c5c")
        # MENU 4
        self.usernametext2 = Label(self.frame, text="Username",
                                   font=("Comic Sans MS", 13), pady=10,
                                   fg="#dad7cd", bg="#565656")
        self.usernameinput2 = Entry(self.frame, width=30, font=("Arial", "12"))
        self.passwordtext2 = Label(self.frame2, text="Senha",
                                   font=("Comic Sans MS", 13), pady=10,
                                   fg="#dad7cd", bg="#565656")
        self.passwordinput2 = Entry(self.frame2, width=30, font=("Arial", "12"))
        self.singinsubmit = Button(self.frame3, text="Cadastrar",
                                   font=self.font, pady=10,
                                   width=10, command=lambda: self.submitSingin(),
                                   bg="#f4a259")
        self.msgerro2 = Label(self.frame4, text="Username ja cadastrado.", fg="red", font=self.font, bg="#565656")
        self.msgerro3 = Label(self.frame4, text="Não deixe os campos em branco.", fg="red", font=self.font,
                              bg="#565656")
        self.msgaccept = Label(self.frame4, text="Usuário cadastrado com sucesso.", fg="green", font=self.font,
                               bg="#565656")
        self.inputid = Entry(self.frame2, width=5, font=("Arial", "12"))
        self.msginvalid = Label(self.frame4, text="Não foi possivel fazer a venda, você não possui uma ou mais "
                                                  "cópias dessa figurinha",
                                bg="#565656", font=self.font, fg="red")
        self.msgidinvalid = Label(self.frame4, text="ID Invalido", bg="#565656", font=self.font, fg="red")

    def menuLogin(self):
        self.openMenu2()

    def menuSingin(self):
        self.openMenu4()

    def albumview(self):
        self.clearMenu()
        self.current = -1
        self.image_list = []
        self.quantity_list = []
        response = al.albumview(self.response)
        for figure in response:
            self.image_list.append(figure['path'])
            self.quantity_list.append(str(figure['quantity']))
        self.move(+1)

    def move(self, delta):
        self.clearMenu()
        Button(root, text='Voltar Figuras', bg="#8cb369", font=self.font, command=lambda: self.move(-1)).place(x=650,
                                                                                                               y=750)
        Button(root, text='Proximas Figuras', bg="#f5be51", font=self.font).place(x=780, y=750)
        Button(root, text='Sair', bg="#ff5c5c", font=self.font, command=lambda: self.openMenu3(self.response)).place(
            x=930, y=750)
        if delta > 0:
            if len(self.image_list) - 1 > self.current:
                self.current += delta
                qtd = Label(root, text="Quantidade: " + self.quantity_list[self.current], bg='#565656', font=self.font,
                            fg="white")
                qtd.place(x=250, y=710)
                photo = PhotoImage(file="view/img/" + self.image_list[self.current])
                gimg1_label = Label(root, image=photo)
                gimg1_label.image = photo
                gimg1_label.place(x=50, y=20)
                self.showed = 1
            if len(self.image_list) - 1 > self.current:
                self.current += delta
                qtd2 = Label(root, text="Quantidade: " + self.quantity_list[self.current], bg='#565656', font=self.font,
                             fg="white")
                qtd2.place(x=750, y=710)
                photo2 = PhotoImage(file="view/img/" + self.image_list[self.current])
                gimg2_label = Label(root, image=photo2)
                gimg2_label.image = photo2
                gimg2_label.place(x=550, y=20)
                self.showed += 1
            if len(self.image_list) - 1 > self.current:
                self.current += delta
                qtd3 = Label(root, text="Quantidade: " + self.quantity_list[self.current], bg='#565656', font=self.font,
                             fg="white")
                qtd3.place(x=1250, y=710)
                photo3 = PhotoImage(file="view/img/" + self.image_list[self.current])
                gimg3_label = Label(root, image=photo3)
                gimg3_label.image = photo3
                gimg3_label.place(x=1050, y=20)
                self.showed += 1
        else:
            if self.current >= 3:
                self.current -= self.showed + 2
                qtd = Label(root, text="Quantidade: " + self.quantity_list[self.current], bg='#565656', font=self.font,
                            fg="white")
                qtd.place(x=250, y=710)
                photo = PhotoImage(file="view/img/" + self.image_list[self.current])
                gimg1_label = Label(root, image=photo)
                gimg1_label.image = photo
                gimg1_label.place(x=50, y=20)
                self.current -= delta
                qtd2 = Label(root, text="Quantidade: " + self.quantity_list[self.current], bg='#565656', font=self.font,
                             fg="white")
                qtd2.place(x=750, y=710)
                photo2 = PhotoImage(file="view/img/" + self.image_list[self.current])
                gimg2_label = Label(root, image=photo2)
                gimg2_label.image = photo2
                gimg2_label.place(x=550, y=20)
                self.current -= delta
                qtd3 = Label(root, text="Quantidade: " + self.quantity_list[self.current], bg='#565656', font=self.font,
                             fg="white")
                qtd3.place(x=1250, y=710)
                photo3 = PhotoImage(file="view/img/" + self.image_list[self.current])
                gimg3_label = Label(root, image=photo3)
                gimg3_label.image = photo3
                gimg3_label.place(x=1050, y=20)
                self.showed = 3
        if self.current - 3 < 0:
            Button(root, text='Voltar Figuras', bg="#8cb369", font=self.font).place(x=650, y=750)
        if len(self.image_list) - 1 > self.current:
            Button(root, text='Proximas Figuras', bg="#f5be51", font=self.font, command=lambda: self.move(+1)).place(
                x=780, y=750)

    def buyview(self):
        self.clearMenu()
        imagem1 = PhotoImage(file="view/img/booster.png")
        w = Label(self.frame, image=imagem1)
        w.imagem = imagem1
        w.pack(pady=50)
        buybuttom = Button(self.frame2, text="Comprar \n25 Coins", bg="#B8860B", pady=10, padx=30, font=self.font,
                           command=lambda: self.buyFigure())
        buybuttom.pack()
        back3 = Button(self.frame3, text="Voltar",
                       font=self.font, pady=10, padx=40, command=lambda: self.openMenu3(self.response),
                       bg="#ff5c5c")
        back3.pack()

    def sellview(self):
        self.clearMenu()
        msgtitle = Label(self.frame, text="Digite o ID da carta que deseja vender:", fg="white",
                         font=self.font, bg="#565656")
        msgtitle.pack(pady=30)
        self.inputid.pack()
        sellbuttom = Button(self.frame2, text="Vender", bg="#5b8e7d", pady=2, padx=2, font=self.font,
                            command=lambda: self.sellFigure())
        sellbuttom.pack(pady=15)
        back5 = Button(self.frame3, text="Voltar",
                       font=self.font, pady=5, padx=5, command=lambda: self.openMenu3(self.response),
                       bg="#ff5c5c")
        back5.pack()

    def tradeview(self):
        pass

    def sellFigure(self):
        id = self.inputid.get()
        if self.msgidinvalid or self.msginvalid:
            self.msgidinvalid.pack_forget()
            self.msginvalid.pack_forget()
        if id.isnumeric() and 1 <= int(id) <= 50:
            id = int(id)
            response = fg.figuresellview(self.response, id)
            if response:
                msgidvalid = Label(self.frame4,
                                   text="Figura " + response['name'] + " vendida por " + str(
                                       response['price']) + "Coins",
                                   bg="#565656", font=self.font, fg="#6AF117")

                msgidvalid.pack()
            else:

                self.msginvalid.pack()
        else:
            self.msgidinvalid.pack()

    def buyFigure(self):
        response = fg.figureview(self.response)
        self.clearMenu()
        if response:
            img1 = PhotoImage(file="view/img/" + response[0]['path'])
            img2 = PhotoImage(file="view/img/" + response[1]['path'])
            img3 = PhotoImage(file="view/img/" + response[2]['path'])
            img_list = [img1, img2, img3]
            msg_label = Label(root, text="Figurinhas adquiridas no sorteio:", font=("Comic Sans MS", 15, "bold"),
                              bg="#565656", fg="white")
            msg_label.place(x=650, y=10)
            msg2_label = Label(root, text="Figurinhas adquiridas no sorteio:", font=("Comic Sans MS", 15, "bold"),
                               bg="#565656", fg="white")
            msg2_label.place(x=650, y=10)
            img1_label = Label(root, image=img_list[0])
            img1_label.image = img_list[0]
            img1_label.place(x=75, y=50)
            img2_label = Label(root, image=img_list[1])
            img2_label.image = img_list[1]
            img2_label.place(x=575, y=50)
            img3_label = Label(root, image=img_list[2])
            img3_label.image = img_list[2]
            img3_label.place(x=1075, y=50)
            back4 = Button(self.frame3, text="Voltar",
                           font=self.font, pady=10, padx=40,
                           command=lambda: self.processLogin(self.response['name'],
                                                             self.response['password']),
                           bg="#ff5c5c")
            back4.pack()
        else:
            msgerro4 = Label(self.frame3, text="Não foi possivel fazer a compra, saldo insuficiente", fg="red",
                             font=self.font, bg="#565656")
            msgerro4.pack(pady=5)

    def openMenu1(self):
        self.clearMenu()
        self.mylabel.pack(pady=10)
        self.login.pack(pady=10)
        self.singin.pack(pady=10)
        self.exit.pack(pady=10)

    def openMenu2(self):
        self.clearMenu()
        self.mylabel.pack(pady=10)
        self.usernametext.pack(padx=5, side="left")
        self.usernameinput.pack(padx=5, side="right", ipady=5)
        self.passwordtext.pack(padx=20, side="left")
        self.passwordinput.pack(padx=5, side="right", ipady=5)
        self.loginsubmit.pack(pady=20, ipadx=10, side="right")
        self.back.pack(padx=50, ipadx=10, side="left")

    def openMenu3(self, response):
        self.clearMenu()
        name = response['name']
        balance = response['balance']
        welcome = Label(self.frame, text="Bem-vindo " + name, fg="white",
                        font=("Comic Sans MS", 15, "bold"), bg="#565656")
        welcome.pack()
        welcome = Label(self.frame2, text="Saldo: " + str(balance) + " COINS", fg="#6AF117",
                        font=("Comic Sans MS", 15, "bold"), bg="#565656")
        welcome.pack(pady=10)
        self.album.pack(pady=10)
        self.buy.pack(pady=10)
        self.sell.pack(pady=10)
        self.trade.pack(pady=10)
        self.back2.pack(pady=10)

    def openMenu4(self):
        self.clearMenu()
        self.mylabel.pack(pady=10)
        self.usernametext2.pack(padx=5, side="left")
        self.usernameinput2.pack(padx=5, side="right", ipady=5)
        self.passwordtext2.pack(padx=20, side="left")
        self.passwordinput2.pack(padx=5, side="right", ipady=5)
        self.singinsubmit.pack(pady=20, ipadx=10, side="right")
        self.back.pack(padx=50, ipadx=10, side="left")

    def submitLogin(self):
        name = self.usernameinput.get()
        password = self.passwordinput.get()
        self.processLogin(name, password)

    def submitSingin(self):
        name = self.usernameinput2.get()
        password = self.passwordinput2.get()
        self.processSingin(name, password)

    def processLogin(self, name, password):
        if self.msgerro or self.msgerro3:
            self.msgerro.pack_forget()
            self.msgerro3.pack_forget()
        if (name == '') or (password == ''):
            self.msgerro3.pack(pady=10)
        else:
            response = vl.loginview(name, password)
            if response:
                if response:
                    self.response = response
                    if response['showcard'] == 1:
                        self.showfigure(response['path'])
                    else:
                        self.openMenu3(response)
            else:
                self.msgerro.pack(pady=10)

    def showfigure(self, path):
        self.clearMenu()
        text_label = Label(root, text="Figurinha Adquirida por login diario:", font=self.font, bg="#565656", fg="White")
        text_label.place(x=650, y=10)
        photo = PhotoImage(file="view/img/" + path)
        simg_label = Label(root, image=photo)
        simg_label.image = photo
        simg_label.place(x=550, y=50)
        backbtm = Button(root, text="Confirmar", font=self.font, bg="#c1ddeb", command=lambda : self.openMenu3(self.response))
        backbtm.place(x=750, y=740)

    def processSingin(self, name, password):
        if self.msgerro2 or self.msgerro3 or self.msgaccept:
            self.msgerro2.pack_forget()
            self.msgerro3.pack_forget()
            self.msgaccept.pack_forget()
        if (name == '') or (password == ''):
            self.msgerro3.pack(pady=10)
        else:
            response = vs.singinview(name, password)
            if response:
                self.msgaccept.pack(pady=10)
            else:
                self.msgerro2.pack(pady=10)

    def clearMenu(self):
        for widgets in self.frame.winfo_children():
            widgets.pack_forget()
        for widgets in self.frame2.winfo_children():
            widgets.pack_forget()
        for widgets in self.frame3.winfo_children():
            widgets.pack_forget()
        for widgets in self.frame4.winfo_children():
            widgets.pack_forget()
        for widgets in root.winfo_children():
            widgets.place_forget()


root = Tk()
root.geometry("1600x900")
photo = PhotoImage(file='view/img/icon.png')
root.iconphoto(False, photo)
root.configure(bg="#565656")
root.title("One Figure")
Interface(root)
root.mainloop()