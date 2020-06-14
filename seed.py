import sqlite3

connection = sqlite3.connect('flask.db')

c = connection.cursor()

c.execute('''INSERT INTO users (username, password, fav_game) VALUES('hanzla', 'test', 'pubg');''')



connection.commit()
c.close()
connection.close()

