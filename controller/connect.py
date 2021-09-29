def connect():
    import sqlite3
    conn = sqlite3.connect('oneFigure.db')
    return conn

# Fonte: http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
