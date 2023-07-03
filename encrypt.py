from eth_account import Account
from getpass import getpass
import json

# Получаем пароль от пользователя
password = getpass("Введите пароль: ")

# Читаем приватные ключи из файла
with open('private_keys.txt', 'r') as file:
    private_keys = file.readlines()

# Шифруем каждый приватный ключ и записываем в новый файл
with open('encrypted_keys.json', 'w') as file:
    for private_key in private_keys:
        private_key = private_key.strip()
        encrypted_key = Account.encrypt(private_key, password)
        file.write(json.dumps(encrypted_key) + '\n')

