# Alertas de Segurança com Sockets TCP e UDP

Atividade de programação de rede com o módulo `socket` do Python: um servidor TCP que recebe alertas de segurança e um servidor UDP que recebe heartbeats de sensores.

## Arquivos

| Arquivo | Papel |
| --- | --- |
| `servidor_tcp.py` | Recebe alertas, grava cada um em `log_alertas.txt` e gera o `relatorio_final.txt` ao fim da sessão |
| `cliente_tcp.py` | Envia alertas digitados até receber `FIM` |
| `servidor_udp.py` | Escuta heartbeats sem conexão (`SOCK_DGRAM`, `recvfrom`) |
| `cliente_udp.py` | Simula um sensor que envia 5 heartbeats a cada 2 segundos |
| `respostas.txt` | Discussão sobre socket bloqueante, TCP x UDP e tratamento de encerramento |

## Conceitos praticados

- TCP (orientado a conexão) e UDP (sem conexão)
- `bind`, `listen`, `accept`, `recv` e `sendto`/`recvfrom`
- Socket bloqueante, encerramento limpo com `finally` e `KeyboardInterrupt`
- Log em arquivo e relatório de sessão

## Como executar

Só usa a biblioteca padrão do Python. Abra dois terminais:

```bash
# TCP
python servidor_tcp.py
python cliente_tcp.py

# UDP
python servidor_udp.py
python cliente_udp.py
```

> Os IPs que aparecem nos logs são dados fictícios de laboratório.
