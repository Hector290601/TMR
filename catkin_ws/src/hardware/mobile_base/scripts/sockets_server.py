import socket
import time
import uuid

available_ports = list(range(5001, 5011))
devices = {}

def server_program(server_socket):
    global mac_address
    print('hearing')
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    data = conn.recv(1024).decode()
    print("from connected user: " + str(data))
    data = data.split('|')
    print(data)
    data2send = 'PWRL|' + mac_address + '|192.168.1.197'
    for port in available_ports:
        if port not in devices:
            data2send += str(port) + '|HELLO|'
            break
    conn.send(data2send.encode())
    conn.close()
    time.sleep(1)

if __name__ == '__main__':
    host = "192.168.1.197"
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    mac_int = uuid.getnode()
    mac_hex = format(mac_int, '012x')
    mac_address = ''.join(mac_hex[i:i+2] for i in range(0, 12, 2))
    while True:
        try:
            server_program(server_socket)
        except:
            break
    server_socket.close()
