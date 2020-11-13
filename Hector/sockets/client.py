# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:49:29 2020

@author: hrmha
"""

import socket

host = socket.gethostname()
port = 12345
bufferSize = 1024
message = 'Hola mundo!'

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketTcp:
        socketTcp.connect((host, port))
        socketTcp.send(message.encode('utf-8'))
        data = socketTcp.recv(bufferSize)