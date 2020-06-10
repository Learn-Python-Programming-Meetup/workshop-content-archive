import os
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey1234#'
chat_app = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


def ack():
    print('message was received!!!')


@chat_app.on('message_event', namespace='/chat')
def handle_message(json):
    print('message received' + str(json))
    chat_app.emit('my response', json, namespace='/chat', callback=ack)


@chat_app.on('connect', namespace='/chat')
def handle_connect():
    print('Client connected')
    chat_app.emit('my response', {'data': 'Connected'}, namespace='/chat')


@chat_app.on('disconnect', namespace='/chat')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    chat_app.run(app, port=int(os.environ.get('PORT', '5000')))
