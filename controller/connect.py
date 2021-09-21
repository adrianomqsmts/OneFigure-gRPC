def connect():
    import mysql.connector

    mydb = None

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="oneFigure"
        )
    except Exception as e:
        print("Ocorreu um erro ao conectar ao banco de dados")
    finally:
        return mydb
