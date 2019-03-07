import csv
import os
import re


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    files = os.listdir(path='txt')
    for f in files:
        with open(os.path.join('txt', f)) as reader:
            for line in reader.readlines():

                if re.findall(r'(?<=\bИзготовитель системы:\s).+(?=\s)', re.sub(r'\s+', ' ', line)):
                    os_prod_list.append(re.findall(r'(?<=\bИзготовитель системы:\s).+(?=\s)',
                                                   re.sub(r'\s+', ' ', line))[0])

                if re.findall(r'(?<=\bНазвание ОС:\s).+(?=\s)', re.sub(r'\s+', ' ', line)):
                    os_name_list.append(re.findall(r'(?<=\bНазвание ОС:\s).+(?=\s)', re.sub(r'\s+', ' ', line))[0])

                if re.findall(r'(?<=\bКод продукта:\s).+(?=\s)', re.sub(r'\s+', ' ', line)):
                    os_code_list.append(re.findall(r'(?<=\bКод продукта:\s).+(?=\s)', re.sub(r'\s+', ' ', line))[0])

                if re.findall(r'(?<=\bТип системы:\s).+(?=\s)', re.sub(r'\s+', ' ', line)):
                    os_type_list.append(re.findall(r'(?<=\bТип системы:\s).+(?=\s)', re.sub(r'\s+', ' ', line))[0])

    for i in range(len(os_code_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv():
    tmp_data = get_data()
    with open(os.path.join('csv', 'data.csv'), 'w') as csv_data:
        data_writer = csv.writer(csv_data)
        data_writer.writerows(tmp_data)


write_to_csv()
