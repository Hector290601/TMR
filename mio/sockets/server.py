# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:43:55 2020

@author: hrmha
"""

import socket

host = socket.gethostname()

port = 12345

bufferSize = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketTcp:
    socketTcp.bind((host, port))
    socketTcp.listen(5)
    conn, addr = socketTcp.accept()
    with conn:
        print('[*] Conexión establecida')
        while True:
            data = conn.recv(bufferSize)
            if not data:
                break
            else:
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8')))
            conn.send(data)
            