import requests
import time
import os
from lxml import html

print("""
Эта программа предназначена для обработки списка идентификаторов Вконтакте, полученных в результате использования других парсинг-скриптов.
Она преобразует список id в читаемый вид - фамилию и имя пользователя.

Для работы потребуется список id формата http://vk.com/id.. в текстовом файле с кодировкой UTF-8.
Список доступных файлов:""")

files_list = os.listdir(os.getcwd())

for file_name in files_list:
        print(file_name,end=" ")

file_name_input = input("Укажите имя файла, в котором находится список пользователей:\n")

try:
    list = open(file_name_input, encoding='UTF-8') #Список id
except:
    print("Что-то пошло не так")
else:
    print("Файл загружен в память")

file_name_output = input("Укажите имя выходного файла, где будут указаны имена пользователей:\n")

try:
    parsed_list = open(file_name_output,'w',encoding='UTF-8') #Список id
except:
    print("Что-то пошло не так")
else:
    print("Файл создан и открыт на запись")

try:
    for line in list:
        #time.sleep(3)
        response = requests.get(line.rstrip('\r\n'))    
        parsed=html.fromstring(response.text)
        parsed_list.write(line.rstrip('\r\n') + ' | ' + parsed.xpath('//title/text()')[0] + '\n')
except:
    print("Не удалось распарсить имена, проверьте исходный файл")
else:
    print("Готово!")