import yaml
import os

DATA = {
    'one': [1, 2, 3],
    'two': 1,
    'three': {'1€': 1, '2€': 2, '3€': 3}
}


def write_to_yaml():
    with open(os.path.join('yaml', 'data.yaml'), 'w') as file:
        yaml.dump(DATA, file, default_flow_style=False, allow_unicode=True)


def check_data():
    with open(os.path.join('yaml', 'data.yaml')) as file:
        file_data = yaml.load(file)

    if file_data == DATA:
        return True
    else:
        return False


def main():
    write_to_yaml()
    if check_data():
        print('Данные идентичны')
    else:
        print('Данные различны')


main()
