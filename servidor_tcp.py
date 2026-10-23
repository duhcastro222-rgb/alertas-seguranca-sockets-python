# Atividade Sockets - Servidor TCP de alertas (Etapas 1 a 5)

import socket
from datetime import datetime

HOST = "127.0.0.1"
PORTA = 5000

arquivo_log = "log_alertas.txt"
arquivo_relatorio = "relatorio_final.txt"


# devolve a data e a hora de agora em texto
def data_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# Etapa 3: grava o alerta no arquivo de log
def gravar_log(mensagem):
    with open(arquivo_log, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora()}] {mensagem}\n")


# Etapa 4: monta o relatorio final da sessao
def gerar_relatorio(inicio, fim, cliente, alertas):
    with open(arquivo_relatorio, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATORIO FINAL DA SESSAO DE MONITORAMENTO\n")
        arquivo.write(f"Inicio: {inicio}\n")
        arquivo.write(f"Fim: {fim}\n")
        arquivo.write(f"Cliente conectado: {cliente}\n")
        arquivo.write(f"Total de alertas: {len(alertas)}\n")
        arquivo.write("\nAlertas recebidos:\n")
        numero = 1
        for alerta in alertas:
            arquivo.write(f"{numero}. {alerta}\n")
            numero = numero + 1


# Etapa 1: cria o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inicio = data_hora()
cliente = "nenhum"
alertas = []

# Etapa 5: a logica do servidor fica dentro do try/except/finally
try:
    servidor.bind((HOST, PORTA))
    servidor.listen(1)
    print(f"Servidor TCP ouvindo em {HOST}:{PORTA}")

    conexao, endereco = servidor.accept()
    cliente = f"{endereco[0]}:{endereco[1]}"
    print(f"Cliente conectado: {cliente}")

    # Etapa 2: recebe alertas ate o cliente enviar FIM
    while True:
        dados = conexao.recv(1024)
        if not dados:
            break
        mensagem = dados.decode("utf-8").strip()
        if mensagem.upper() == "FIM":
            break
        print(f"[ALERTA RECEBIDO] {mensagem}")
        alertas.append(mensagem)
        gravar_log(mensagem)

    conexao.close()

except KeyboardInterrupt:
    print("\nServidor encerrado com Ctrl+C")
except socket.error as erro:
    print(f"Erro de socket: {erro}")
finally:
    servidor.close()
    gerar_relatorio(inicio, data_hora(), cliente, alertas)
    print(f"Relatorio gravado em {arquivo_relatorio}")
