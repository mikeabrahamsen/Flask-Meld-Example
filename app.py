from flask import Flask, render_template, current_app
from flask_meld import Meld

app = Flask(__name__)
app.config['SECRET_KEY'] = 'big!secret'
Meld(app)
socketio = app.socketio


@app.route('/')
def index():
    return render_template("base.html")

if __name__ == '__main__':
    socketio.run(app)
