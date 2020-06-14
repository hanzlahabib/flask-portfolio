import sqlite3
connection = sqlite3.connect('flask.db')
cursor = connection.cursor()
def show_game(username):
    connection = sqlite3.connect('flask.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT fav_game FROM USERS where username='{username}' ORDER BY pk DESC;'''.format(username = username))
    game = cursor.fetchone()[0]
    message = '{username}\'s Fav Game is {game}.'.format(username = username, game = game) 
    connection.commit()
    cursor.close()
    connection.close()
    return message


def check_pwd(username, password):
    connection = sqlite3.connect('flask.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;'''.format(username = username))
    db_password = cursor.fetchone()[0]
    print(db_password)
    connection.commit()
    cursor.close()
    connection.close()
    
    
    if(db_password == password):
        return True
    else:
        return False


def check_user_exist(username):
    connection = sqlite3.connect('flask.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT username from users where username = '{username}' order by pk desc;'''.format(username=username))
    isExist = cursor.fetchone()

    connection.commit()
    cursor.close()
    connection.close()

    if isExist == None:
        return False
    else:
        return True


def create_user(username, password):
    connection = sqlite3.connect('flask.db')
    cursor = connection.cursor()
    cursor.execute('''insert into users (username, password) values ('{username}', '{password}');'''.format(username=username, password=password))
    isExist = check_user_exist(username)
    connection.commit()
    cursor.close()
    connection.close()
    if isExist == None:
        return False
    else:
        return True
