from source import source
from flask import Flask, redirect, url_for, request, session
from functools import wraps
#from flask_login

app = Flask(__name__)
app.secret_key = 'this is a secret key'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap
        
@app.route('/')
def index():
    return "HELLO WORLD"

@app.route('/login')
def login():
    return 'Login!'
    
@app.route('/on')
#@login_required
def on():
    socket_no = int(request.args.get('socket'))
    print(socket_no)
    return source.socket_on(socket_no)

@app.route('/off')
#@login_required
def off():
    socket_no = int(request.args.get('socket'))
    print(socket_no)
    return source.socket_off(socket_no)

def clean_gpio():
    return source.socket_clean()

def setup_gpio():
    return source.socket_setup()
    

if __name__ == '__main__':
    clean_gpio()
    setup_gpio()
    app.run(debug=True, host = '0.0.0.0')
