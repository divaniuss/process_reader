import psutil
import json
import socket

IP = '127.0.0.1'
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))


listOfProc = list(psutil.process_iter())
output = []

for index, process in enumerate(listOfProc):
    try:
        output.append(
            {
                "index": index,
                "name": process.name(),
                "pid": process.__getattribute__('pid')
            })
    except Exception as e:
        print(f"Ошибка: {e}")

client.send(json.dumps(output).encode())
print("Sended")



client.close()