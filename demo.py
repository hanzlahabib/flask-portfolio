from flask import Flask, render_template,  request, session, redirect, url_for, g
import model
app = Flask(__name__)
app.secret_key = 'hanzla'

username = ''
user = model.check_users()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if 'username' in session:
        g.user = session['username']
        return render_template('index.html')
    return render_template('login.html', message="You need to login first")

@app.route('/about-us', methods = ['GET'])
def aboutus():
    if 'username' in session:
        g.user = session['username']
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('home'))
    else:
        session.pop('username', None)
        areyouuser = request.form['username']
        password = request.form['password']
        pwd = model.check_pwd(areyouuser, password)
        print(pwd)
        if pwd:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            message = "You entered invalid Credentials"
            return render_template('login.html', message=message)
    return ''

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port = 7000, debug = True) 
