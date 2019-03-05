# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# тип на кириллице.

import subprocess


def fifth(res):
    ping_res = ['ping', res]
    sub_ping = subprocess.Popen(ping_res, stdout=subprocess.PIPE)
    for line in sub_ping.stdout:
        line = line.decode('cp866')
        print(line)


if __name__ == '__main__':
    fifth('yandex.ru')
    fifth('youtube.com')
