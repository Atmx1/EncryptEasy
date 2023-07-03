from eth_account import Account
from getpass import getpass
import json

# Получаем пароль от пользователя
password = getpass("Введите пароль: ")

# Читаем зашифрованные ключи из файла
with open('encrypted_keys.json', 'r') as file:
    encrypted_keys = file.readlines()

# Дешифруем каждый ключ и записываем в новый файл
with open('decrypted_keys.txt', 'w') as file:
    for encrypted_key in encrypted_keys:
        encrypted_key = json.loads(encrypted_key.strip())
        private_key = Account.decrypt(encrypted_key, password)
        file.write(private_key.hex() + '\n')
