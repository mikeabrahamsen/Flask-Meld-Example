from flask import Flask, render_template, redirect, url_for, request
from flask_meld import Meld
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'big!secret'
Meld(app)
socketio = app.socketio


@app.route('/')
def index():
    return render_template("base.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for(request.url))
    return render_template("register_page.html")


if __name__ == '__main__':
    socketio.run(app)
