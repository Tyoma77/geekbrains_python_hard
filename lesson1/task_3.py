# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


def third():
    srd_lst = ['attribute', 'класс', 'функция', 'type']
    for item in srd_lst:
        try:
            bytes(item, encoding='ASCII')
        except UnicodeEncodeError:
            print(f'Слово \'{item}\' невозможно преобразовать.')


if __name__ == '__main__':
    third()
