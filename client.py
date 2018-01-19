# coding: utf-8

# This is the main code that will need to be changed.
import socket

import sys
from threading import Thread

s = socket.socket()
s.connect(('127.0.0.1', 4344))
s.setblocking(0)

print('Server is ready, please type your commands:')


def check_incoming():
    while True:
        try:
            received = s.recv(4096).decode('utf-8')
            if received and not received.isspace():
                print('Received:', received)
        except BlockingIOError:
            # time.sleep(1)
            pass
        except KeyboardInterrupt:
            break


def send():
    sent_commands = 0
    while True:
        try:
            print('ID: ' + str(sent_commands) + ': ')
            data_in = sys.stdin.readline().strip('\n')
            message = '{"command": "' + data_in + '", "id": ' + str(sent_commands) + '}'
            s.send(message.encode('utf-8'))
            sent_commands += 1
        except KeyboardInterrupt:
            break


Thread(target=check_incoming).start()
Thread(target=send).start()
