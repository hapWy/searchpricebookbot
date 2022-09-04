import csv
from aiogram import types

def grableRequest(message: types.Message):
    with open('requests.csv','a', newline='') as file:
        csv.writer(file, delimiter=';').writerow((message.from_user.username, message.text))
    return message.text


