# Функции клиента:
#
# сформировать presence-сообщение;
# отправить сообщение серверу;
# получить ответ сервера;

# разобрать сообщение сервера;
# параметры командной строки скрипта+
# client.py <addr> [<port>]:+
# addr — ip-адрес сервера;+
# port — tcp-порт на сервере, по умолчанию 7777.+


from socket import *
import time
import argparse
import json


def cmd_args():  # обработка сообщений командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', type=str, default='localhost')
    parser.add_argument('port', nargs='?', type=int, default=7777)

    return parser.parse_args()


def presence_msg(username, status):  # сформировать presence-сообщение;
    return {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'username': username,
            'status': status,
        }
    }


def send_message(msg, s):  # отправить сообщение серверу;
    print("Sending message %s" % msg)
    s.send(msg.encode('utf-8'))


def get_msg(soc):  # получить ответ сервера;
    msg = soc.recv(1000000)
    parse_message(msg)


def parse_message(data):  # разобрать сообщение сервера;
    try:
        server_msg = json.loads(data.decode('utf-8'))
        if server_msg['response'] == 100:
            print("Сообщение доставлено на сервер, код возврата ", server_msg["response"], server_msg["alert"])
    except json.decoder.JSONDecodeError:
        print('Сообщение не распозноно, {}'.format(data))


def main():
    cmd_args()
    client_socket = socket(AF_INET, SOCK_STREAM)
    msg = json.dumps(presence_msg("Artem", "I'm home"))

    try:
        client_socket.connect((cmd_args().addr, cmd_args().port))
    except ConnectionRefusedError:
        print('Сервер {} недоступен по порту {}'.format(cmd_args().addr, cmd_args().port))

    send_message(msg, client_socket)
    get_msg(client_socket)

    client_socket.close()


if __name__ == '__main__':
    main()
