import controller.connect as conn
import model.figure as figure


def show(id_user):
    result = []
    mydb = conn.connect()
    mycursor = mydb.cursor(dictionary=True)

    sql = "SELECT * FROM album INNER JOIN figure ON idUser = %s AND album.idFigure = figure.idFigure;"
    var = (id_user, )

    mycursor.execute(sql, var)
    data = mycursor.fetchall()
    if data:
        result.append(data)
        verify = figure.verifyComplet(id_user)
        special = []
        if verify == 1:
            result.append({'complete': 1})
            figure.addSpecialCard(id_user)
            figure.showone(51, result)
        else:
            result.append({'complete': 0})
            result.append(special)
    else:
        result.append('')
        result.append({'complete': 0})
        result.append('')
        print()
    return result