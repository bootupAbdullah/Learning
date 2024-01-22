import csv

compromised_users = []

# 1. - #7.
with open('passwords.csv', newline='') as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = row
        compromised_users.append(password_row['Username'])

# 8. - 10.
with open('compromised_users.txt', 'w') as compromised_user_file:
    for users in compromised_users:
        compromised_user_file.write('users')

# 11. - # 15.
import json

with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {'recepient': "The Boss", 'message': "Mission Sucess"}
    json.dump(boss_message_dict, boss_message)

# json test:
# with open('boss_message.json') as message:
#   read_file = json.load(message)

# print(read_file)
# Prints '{recepient': 'The Boss', 'message': 'Mission Sucess'}'

# 16.
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/ 
'''
signature_writer = csv.DictWriter(new_passwords_obj, slash_null_sig)