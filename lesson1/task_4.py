# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).


def fourth():
    ar_fth = ['разработка', 'администрирование', 'protocol', 'standard']
    for i in ar_fth:
        print(i.encode('utf-8'))
        print(i.encode('utf-8').decode('utf-8') + '\n')


if __name__ == '__main__':
    fourth()
