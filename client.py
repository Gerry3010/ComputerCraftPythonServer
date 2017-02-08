# coding: utf-8

# This is the main code that will need to be changed.
import os
import socket

import sys
from threading import Thread

s = socket.socket()

s.bind(('127.0.0.1', 4344))
s.listen(-1)

c = s.accept()
c = c[0]

print('Server is ready, please type your commands:')


def main():
    def check_incoming():
        while True:
            # TODO Check for incoming messages and print them
            pass

    thread = Thread(target=check_incoming)
    thread.start()

    sent_commands = 0

    while True:
        print('ID: ' + str(sent_commands) + ': ', end='')
        message = '{"command": "' + input() + '", "id": ' + str(sent_commands) + '}'
        c.send(message.encode('utf-8'))
        sent_commands += 1


try:
    main()
except KeyboardInterrupt:
    try:
        c.close()
    finally:
        pass

    try:
        sys.exit(0)
    except SystemExit:
        pass
