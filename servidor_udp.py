# Atividade Sockets - Etapa 5: servidor UDP de heartbeats

import socket
from datetime import datetime

HOST = "127.0.0.1"
PORTA = 5001

# UDP usa SOCK_DGRAM e nao precisa de listen() nem accept()
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORTA))
print(f"Servidor UDP ouvindo heartbeats em {HOST}:{PORTA}")

try:
    while True:
        # recvfrom devolve os dados e o endereco de quem enviou
        dados, endereco = servidor.recvfrom(1024)
        mensagem = dados.decode("utf-8")
        hora = datetime.now().strftime("%H:%M:%S")
        print(f"[HEARTBEAT {hora}] {endereco[0]} -> {mensagem}")

except KeyboardInterrupt:
    print("\nServidor UDP encerrado com Ctrl+C")
finally:
    servidor.close()
