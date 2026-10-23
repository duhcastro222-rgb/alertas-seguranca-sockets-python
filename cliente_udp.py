# Atividade Sockets - sensor que envia heartbeats por UDP

import socket
import time

HOST = "127.0.0.1"
PORTA = 5001

sensor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia 5 heartbeats, um a cada 2 segundos
for numero in range(1, 6):
    mensagem = f"SENSOR-01 vivo (heartbeat {numero})"
    # sendto nao abre conexao, so dispara o pacote
    sensor.sendto(mensagem.encode("utf-8"), (HOST, PORTA))
    print(f"Enviado: {mensagem}")
    time.sleep(2)

sensor.close()
