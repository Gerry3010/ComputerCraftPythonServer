# coding: utf-8
import json
import socket
from threading import Thread

from flask import Flask
from flask import request

s = socket.socket()
s.bind(('127.0.0.1', 4344))
s.listen(-1)
c = s.accept()
c = c[0]

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def req():
    if request.method == 'GET':
        received = c.recv(4096).decode('utf-8')
        print('Received:', received)
        json_string = json.loads(received)
        command = str(json_string['id']) + ',' + json_string['command']
        return command
    elif request.method == 'POST':
        print('Returned data: ' + str(request.form))

        data = request.form

        message = '{'
        if 'result' in data:
            message += '"result": "' + data['result'] + '",'
        if 'result2' in data:
            message += '"result2": "' + str(data['result2']) + '",'
        if 'error' in data:
            message += '"error": "' + str(data['error']) + '",'
        if 'id' in data:
            message += '"id": "' + str(data['id']) + '"'
        message += '}'

        c.send(message.encode('utf-8'))

    return ''


app.run(None, 4343)
