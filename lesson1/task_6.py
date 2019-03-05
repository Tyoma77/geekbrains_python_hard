# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести
# его содержимое.

WORDS = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as test_file:
    for word in WORDS:
        test_file.write(word + '\n')

print(test_file)

with open('test_file.txt', 'br') as test_file:
    file = test_file.read()

print(file.decode(encoding='utf-8', errors='replace'))
