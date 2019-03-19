# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> — TCP-порт для работы (по умолчанию использует 7777);
# -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

from socket import *
import time
import argparse
import json
import logs.server_log_config
import logging


def cmd_args():  # обработка сообщений командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest="port", type=int, default=7777)
    parser.add_argument("-a", dest="addr", type=str, default='')

    return parser.parse_args()


def get_msg(client):  # принимает сообщение клиента;
    data = client.recv(1024)
    json_msg = {}
    try:
        json_msg = json.loads(data.decode('utf-8'))
    except json.JSONDecodeError:
        logger.error("Сообщение от клиента не распознано", data)

    return json_msg


def resp_from_server(client_msg, client):  # формирует ответ клиенту;
    json_resp = {}
    if client_msg["action"] == 'presence':
        json_resp = {
            "response": 100,
            "time": time.time(),
            "alert": "Принято"
        }
    msg = json.dumps(json_resp)
    client.send(msg.encode('utf-8'))
    client.close()


def send_msg(s: socket):  # отправляет ответ клиенту;
    client, adr = s.accept()
    msg_from_client = get_msg(client)
    resp_from_server(msg_from_client, client)


def main():
    args = cmd_args()
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.bind(('', args.port))
    except OSError as e:
        logger.error(e)
        s.bind(('', 8888))
    s.listen(5)
    while True:
        send_msg(s)


if __name__ == '__main__':
    logger = logging.getLogger('server')
    logger.debug('Server started')
    main()
