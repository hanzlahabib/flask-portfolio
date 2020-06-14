import sqlite3

connection = sqlite3.connect('flask.db')
c = connection.cursor()

c.execute(
    	''' 
        CREATE TABLE users(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(16),
            password VARCHAR(32),
            fav_game VARCHAR(16)
        );
        '''
)

connection.commit()
connection.close()
c.close()