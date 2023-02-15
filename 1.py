import re

conf_pass = r'[a-zA-Z0-9_@-]{6,18}'
pas = input("Введите ваш пароль: ")
print(re.findall(conf_pass, pas))
dlin = len(pas)

if 6 <= len(pas) <= 18:
    print("Пароль удовлетворяет условиям")
else:
    print("Пароль не удовлетворяет условиям")