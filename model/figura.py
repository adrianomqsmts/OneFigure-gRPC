import controller.connect as conn
from random import randint
import sqlite3


def buy(id_user):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM usuario WHERE idUser = ?"
    var = (id_user,)
    mycursor.execute(sql, var)
    result = mycursor.fetchone()
    value = result['balance']
    if value >= 25:
        cards = buyAction(id_user, value)
        addCard(id_user, cards)
        result = []
        show(cards, result)
        result.append(str(value - 25))
    else:
        result = None
    return result


def buyAction(id_user, value):
    cards = []
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "UPDATE usuario SET balance = ? WHERE idUser = ?"
    var = (value - 25, id_user)
    mycursor.execute(sql, var)
    mydb.commit()
    summon(cards)
    return cards


def summon(cards):
    for i in range(3):
        x = randint(1, 50)
        cards.append(x)


def addCard(id_user, cards):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    for i in range(3):
        sql = "SELECT * FROM album WHERE idFigure = ? and idUser = ?"
        var = (cards[i], id_user)
        mycursor.execute(sql, var)
        ver = mycursor.fetchone()
        if ver:
            sql = "UPDATE album SET quantity = ? WHERE idUser = ? and idFigure = ?"
            var = (ver['quantity'] + 1, id_user, cards[i])
            mycursor.execute(sql, var)
        else:
            sql = "INSERT INTO album (idUser,idFigure,quantity) VALUES (?, ?, ?)"
            var = (id_user, cards[i], 1)
            mycursor.execute(sql, var)
    mydb.commit()


def addFigure(idUser, idFigure):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()

    sql = "SELECT * FROM album WHERE idFigure = ? and idUser = ?"
    var = (idFigure, idUser)
    mycursor.execute(sql, var)
    ver = mycursor.fetchone()
    if ver:
        sql = "UPDATE album SET quantity = ? WHERE idUser = ? and idFigure = ?"
        var = (ver['quantity'] + 1, idUser, idFigure)
        mycursor.execute(sql, var)
    else:
        sql = "INSERT INTO album (idUser,idFigure,quantity) VALUES (?, ?, ?)"
        var = (idUser, idFigure, 1)
        mycursor.execute(sql, var)
    mydb.commit()


def show(cards, result):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    for i in range(3):
        sql = "SELECT * FROM figure WHERE idFigure = ?"
        var = (cards[i],)
        mycursor.execute(sql, var)
        result.append(mycursor.fetchone())


def showone(cards, result):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM figure WHERE idFigure = ?"
    var = (cards,)
    mycursor.execute(sql, var)
    result.append(mycursor.fetchone())


def verifyQuantity(idUser, idFigure):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    try:
        sql = "SELECT quantity FROM usuario INNER JOIN album ON usuario.idUser = ? AND" \
              " album.idUser = ? AND idFigure = ?;"
        val = (idUser, idUser, idFigure)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        value = result['quantity']
        if value > 1:
            return 1
        else:
            return 0
    except Exception as e:
        print('Erro: ', e)
        return 0


def createTrade(idUser, offer, taking):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    if verifyQuantity(idUser, offer):  # Verificar a quantidade de cartas se pode trocar
        try:
            valid = _offer(idUser, offer)
            if valid:
                sql = "INSERT INTO trade (idUser, offer, taking) VALUES (?, ?, ?)"
                val = [(idUser, offer, taking)]
                mycursor.executemany(sql, val)
                mydb.commit()
                return 1
            else:
                return 0
        except Exception as e:
            print("Erro: ", e)
            return 0
    else:
        return 0


def _offer(idUser, offer):
    try:
        mydb = conn.connect()
        mydb.row_factory = sqlite3.Row
        mycursor = mydb.cursor()
        sql = "SELECT * FROM album WHERE idFigure = ? and idUser = ?"
        var = (offer, idUser)
        mycursor.execute(sql, var)
        result = mycursor.fetchone()
        value = int(result['quantity']) - 1
        if result:
            sql = "UPDATE album SET quantity = ? WHERE idUser = ? AND idFigure = ?"
            var = (value, idUser, offer)
            mycursor.execute(sql, var)
            mydb.commit()
            return 1
    except Exception as e:
        print('Erro: ', e)
        return 0


def listTrade():
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()

    sql = "SELECT u.name, t.idTrade, offer.idFigure as offerID, offer.name as offerName, offer.rarity as offerRarity," \
          " taking.idFigure as takingID, taking.name as takingName, taking.rarity as takingRarity " \
          "FROM usuario as u INNER JOIN trade as t ON u.idUser = t.idUser " \
          "INNER JOIN figure as offer ON t.offer = offer.idFigure INNER JOIN" \
          " figure as taking ON t.taking = taking.idFigure"

    mycursor.execute(sql)
    result = mycursor.fetchall()

    return result


def findTrade(idTrade):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()

    sql = "SELECT * FROM Trade WHERE idTrade = ?"
    var = (idTrade,)

    mycursor.execute(sql, var)
    result = mycursor.fetchone()

    return result


def deleteTrade(idTrade):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()

    sql = "DELETE FROM trade WHERE idTrade = ?"
    var = (idTrade,)

    mycursor.execute(sql, var)
    mydb.commit()


def trade(idUser, idTrade):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    trade = findTrade(idTrade)
    if trade:
        if verifyQuantity(idUser, trade['taking']) and trade:
            # OFFER
            sql = "SELECT * FROM album WHERE idFigure = ? and idUser = ?"
            var = (trade['taking'], idUser)
            mycursor.execute(sql, var)
            result = mycursor.fetchone()
            if result:
                sql = "UPDATE album SET quantity = ? WHERE idUser = ? and idFigure = ?"
                var = (result['quantity'] - 1, idUser, trade['taking'])
                mycursor.execute(sql, var)
                mydb.commit()
                addFigure(idUser, trade['offer'])
                deleteTrade(idTrade)
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def sell(id_user, id_figure):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM album WHERE idFigure = ? and idUser = ?"
    var = (id_figure, id_user)
    mycursor.execute(sql, var)
    data = mycursor.fetchone()
    if data:
        quantity = data['quantity']
        if quantity > 1:
            result = sellAction(id_user, id_figure, quantity)
        else:
            result = None
    else:
        result = None
    return result


def sellAction(id_user, id_figure, quantity):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "UPDATE album SET quantity = ? WHERE idUser = ? and idFigure = ?"
    var = (quantity - 1, id_user, id_figure)
    mycursor.execute(sql, var)
    mydb.commit()
    data = addBalance(id_user, id_figure)
    return data


def addBalance(id_user, id_figure):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM usuario WHERE idUser = ?"
    var = (id_user,)
    mycursor.execute(sql, var)
    data1 = mycursor.fetchone()
    balance = data1['balance']
    sql = "SELECT * FROM figure WHERE idFigure = ?"
    var = (id_figure,)
    mycursor.execute(sql, var)
    data2 = mycursor.fetchone()
    rarity = data2['rarity']
    price = getPrice(rarity)
    sql = "UPDATE usuario SET balance = ? WHERE idUser = ?"
    var = (balance + price, id_user,)
    mycursor.execute(sql, var)
    mydb.commit()
    result = {'name': data2['name'],
              'price': price,
              'balance': data1['balance'] + price
              }
    return result


def getPrice(rarity):
    if rarity.upper() == "COMUM":
        return 5
    elif rarity.upper() == "RARA":
        return 15
    elif rarity.upper() == "ÉPICA":
        return 25


def verifyComplet(id_user):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM album WHERE idUser = ?"
    var = (id_user,)
    mycursor.execute(sql, var)
    data = mycursor.fetchall()
    if len(data) == 50:
        return 1
    else:
        return 0


def addSpecialCard(id_user):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "INSERT INTO album (idUser,idFigure,quantity) VALUES (?, ?, ?)"
    var = (id_user, 51, 1)
    mycursor.execute(sql, var)
    data = mycursor.fetchone()
    mydb.commit()
    return data
