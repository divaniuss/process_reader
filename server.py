import socket
import json

IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

conn, addr = server.accept()
print(f"Подключение от: {addr}")


request = json.loads(conn.recv(99999).decode())


print("Result:")
for proc in request:
    print(proc)


conn.close()
server.close()