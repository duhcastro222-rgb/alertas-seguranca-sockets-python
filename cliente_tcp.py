# Atividade Sockets - Cliente TCP que envia alertas

import socket

HOST = "127.0.0.1"
PORTA = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORTA))
print("Conectado ao servidor. Digite FIM para encerrar.")

while True:
    mensagem = input("Alerta> ")
    if mensagem == "":
        continue
    cliente.send(mensagem.encode("utf-8"))
    if mensagem.upper() == "FIM":
        break

cliente.close()
print("Conexao encerrada")
