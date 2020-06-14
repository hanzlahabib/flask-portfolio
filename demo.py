from flask import Flask, render_template,  request
import model
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message="Welcome!!")
    else:
        username = request.form['username']
        password = request.form['password']
        if model.check_pwd(username, password):
            message = model.show_game(username)
            return render_template('index.html', message=message)
        else:
            return render_template('index.html', message="Hint: He curses alot")

@app.route('/about-us', methods = ['GET'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/sign-up', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        isExist = model.check_user_exist(username)
        print(isExist)
        if not isExist:
            isSuccess = model.create_user(username, password)
        else:
            isSuccess = False
        if isSuccess:
            message = 'User created successfully'
        else:
            message = 'User failed to create'
        
        return render_template('signup.html', message=message)


if __name__ == '__main__':
    app.run(port = 7000, debug = True) 
