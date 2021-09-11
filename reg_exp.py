import re
from pprint import pprint









# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
contacts_list_new = list()
for line in contacts_list:
    new_contact = list()
    fullname = ','.join(line[:3])
    res = re.findall(r'(\w+)', fullname)
    if len(res) < 3:
        res.append('')
    new_contact += res
    new_contact.append(line[3])
    new_contact.append(line[4])
    pattern = re.compile(r"(\+7|8)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*"
                         r"(\d{2})[\s\(]*([а-я]+\.)*[\s]*(\d+)*\)*")
    correct_phone = pattern.sub(r"8(\2)\3-\4-\5 \6\7", line[-2])
    new_contact.append(correct_phone)
    new_contact.append(line[6])
    contacts_list_new.append(new_contact)

final_contacts_list = []
for i in range(len(contacts_list_new)):
    for j in range(len(contacts_list_new)):
        if contacts_list_new[i][0] == contacts_list_new[j][0] and contacts_list_new[i][1] == contacts_list_new[j][1]:
            contacts_list_new[i] = [x or y for x, y in zip(contacts_list_new[i], contacts_list_new[j])]
    if contacts_list_new[i] not in final_contacts_list:
        final_contacts_list.append(contacts_list_new[i])
pprint(final_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(final_contacts_list)
