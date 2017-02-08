# coding: utf-8

import socket

from flask import Flask
from flask import request

s = socket.socket()
s.connect(('127.0.0.1', 4344))

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def req():
    if request.method == 'GET':
        return s.recv(4096).decode('utf-8')
    elif request.method == 'POST':
        # Send the client a message
        # res1 = request.form.get('result')
        # res2 = request.form.get('result2')
        print('Post return data: ' + str(request.values))#str(res1) + ", " + str(res2))

    return ''

app.run(None, 4343)
