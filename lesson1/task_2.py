# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


def second():
    snd_byte = [b'class', b'function', b'method']
    for i in snd_byte:
        print('{}, тип: {}, длина : {}'.format(i, type(i), len(i)))


if __name__ == '__main__':
    second()
