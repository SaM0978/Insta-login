lb = '{'
rb = '}'
user_name = input('username: ')
password = input('password: ')
with open('Scam.py', 'a') as w:
                    w.write(f'\nUsers["{user_name}"] = {lb}"Password": "{password}"{rb}')