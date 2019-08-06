import requests
import time
from lxml import html

list = open('D:\Downloads\парс\likes.txt', encoding='UTF-8') #Список id
parsed_list = open('D:\Downloads\парс\parsed_1.txt','w',encoding='UTF-8') #Место для списка id и пользователей

for line in list:
    #time.sleep(3)
    response = requests.get(line.rstrip('\r\n'))    
    parsed=html.fromstring(response.text)
    parsed_list.write(line.rstrip('\r\n') + ' | ' + parsed.xpath('//title/text()')[0] + '\n')
    