from flask import Flask,render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "srinivaspadhy"
socketio = SocketIO(app)

@app.route("/")
def home_page():
    return render_template("index.html")

@socketio.on('message')
def handle_message(message):
    return socketio.emit('notification', {'data': 'Your New Update is '+message})

if __name__ == "__main__":
    socketio.run(app)


