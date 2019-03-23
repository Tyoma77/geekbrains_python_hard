from socket import *
import time
import argparse
import json
import logs.client_log_config
import logging
import inspect


def log(function):

    def call_function(*args, **kwargs):
        logger.info("функция {} была вызвана из {}".format(function.__name__, inspect.stack()[1][3]))
        r = function(*args, **kwargs)
        return r

    return call_function


def cmd_args():  # обработка сообщений командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', type=str, default='localhost')
    parser.add_argument('port', nargs='?', type=int, default=7777)

    return parser.parse_args()


def presence_msg(username, status):  # сформировать presence-сообщение;
    return {
        "action": "presence",
        "time": time.time(),
        "user": {
            "username": username,
            "status": status,
        }
    }


@log
def send_message(msg, s):  # отправить сообщение серверу;
    logger.info("Sending message %s" % msg)
    s.send(msg.encode('utf-8'))


@log
def get_msg(soc):  # получить ответ сервера;
    msg = soc.recv(1000000)
    parse_message(msg)

@log
def parse_message(data):  # разобрать сообщение сервера;
    try:
        server_msg = json.loads(data.decode('utf-8'))
        if server_msg['response'] == 100:
            print("Сообщение доставлено на сервер, код возврата ", server_msg["response"], server_msg["alert"])
    except json.decoder.JSONDecodeError:
        logger.error('Сообщение не распозноно, {}'.format(data))


def main():
    cmd_args()
    client_socket = socket(AF_INET, SOCK_STREAM)
    msg = json.dumps(presence_msg("Artem", "I'm home"))

    try:
        client_socket.connect((cmd_args().addr, cmd_args().port))
    except ConnectionRefusedError:
        logger.error('Сервер {} недоступен по порту {}'.format(cmd_args().addr, cmd_args().port))

    send_message(msg, client_socket)
    get_msg(client_socket)

    client_socket.close()


if __name__ == '__main__':
    logger = logging.getLogger('client')
    main()
