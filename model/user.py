import controller.connect as conn
from datetime import datetime
from random import randint
import sqlite3


def login(name, password):
    result = []
    day = str(datetime.today().day)
    mounth = str(datetime.today().month)
    if int(day) < 10:
        day = '0' + day
    if int(mounth) < 10:
        mounth = '0' + mounth
    now = str(datetime.today().year) + '-' + mounth + '-' + str(
        day)
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()

    sql = "SELECT * FROM Usuario WHERE name = ? and password = ?"
    var = (name, password,)
    mycursor.execute(sql, var)
    temp = mycursor.fetchone()
    if temp:
        value = showBalance(temp['idUser'])
        result.append(temp)
        date = str(result[0]['login'])
        date = date.split(" ")[0]
        if date != now:
            idcard = dailySummon(result[0]['idUser'])
            result.append(show(idcard))
            showcard = {'showcard': 1}
            result.append(showcard)
        else:
            showcard = {'showcard': 0}
            result.append({'name': '',
                           'idFigure': '',
                           'rarity': '',
                           'path': ''
                           })
            result.append(showcard)
        registerDateLogin(name, now)
        temp = result
        temp.append(value)
    return temp


def create(name, password):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    try:
        sql = "INSERT INTO usuario (name, password) VALUES (?, ?)"
        val = [(name, password)]
        mycursor.executemany(sql, val)
        mydb.commit()
        return 1
    except Exception as e:
        return 0


def update(name, password):
    return 0


def registerDateLogin(name, now):
    hour = datetime.today().hour
    minute = datetime.today().minute
    if minute < 10:
        minute = '0' + str(minute)
    if hour < 10:
        hour = '0' + str(hour)
    clock = str(hour) + ':' + str(minute) + ':00'
    now = now + ' ' + clock
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "UPDATE usuario SET login = ? WHERE name = ?"
    var = (now, name,)
    mycursor.execute(sql, var)
    mydb.commit()


def dailySummon(id_user):
    idcard = randint(1, 50)
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM album WHERE idFigure = ? and idUser = ?"
    var = (idcard, id_user)
    mycursor.execute(sql, var)
    ver = mycursor.fetchone()
    if ver:
        sql = "UPDATE album SET quantity = ? WHERE idUser = ? and idFigure = ?"
        var = (ver['quantity'] + 1, id_user, idcard)
        mycursor.execute(sql, var)
    else:
        sql = "INSERT INTO album (idUser,idFigure,quantity) VALUES (?, ?, ?)"
        var = (id_user, idcard, 1)
        mycursor.execute(sql, var)
    mydb.commit()
    return idcard


def show(idcard):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM figure WHERE idFigure = ?"
    var = (idcard,)
    mycursor.execute(sql, var)
    data = mycursor.fetchone()
    return data


def showBalance(id_user):
    mydb = conn.connect()
    mydb.row_factory = sqlite3.Row
    mycursor = mydb.cursor()
    sql = "SELECT * FROM usuario WHERE idUser = ?"
    var = (id_user,)
    mycursor.execute(sql, var)
    result = mycursor.fetchone()
    value = result['balance']
    return value