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

    while True:
        # send the input as before
        c.send(input().encode('utf-8'))
        pass


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
        os._exit(0)
