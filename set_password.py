#!/bin/python3

import string
import random
import os
import hashlib
import base64

#############################################################################
# 1. Ensure that the working directory is correct, such that the 
#    relative paths later work

file_path = os.path.realpath(__file__)
path = os.path.dirname(file_path)
os.chdir(path)


#############################################################################
# 2. generate a strong password

def generate_password():
    length = 30 + random.randrange(10)
    letters = string.ascii_letters + string.digits + string.digits
    return ''.join(random.choice(letters) for i in range(length))

password = generate_password()
print('The new password is:', password)

#############################################################################
# 3. Replace the password in the required files

def replace_line_in_file(filename, needle, new_line, if_does_not_contain=None):
    lines = []
    try:
        with open(filename, 'r') as file:
            found = False
            for line in file.readlines():
                if not (if_does_not_contain and if_does_not_contain in line):
                    if needle.replace(' ', '') in line.replace(' ', ''):
                        line = new_line + '\n'
                        found = True
                lines.append(line)
            if not found:
                lines.append(new_line + '\n')
    except FileNotFoundError:
        lines = new_line + '\n'

    with open(filename, 'w') as file:
        file.writelines(lines)

def md5_base64(password):
    return base64.b64encode(hashlib.md5(password.encode()).digest()).decode()


replace_line_in_file('.env', 'ADMIN_PASSWORD=', f'ADMIN_PASSWORD={password}')
#replace_line_in_file('./conf/gerrit/etc/secure.config', 'password = ', f'password = {password}')
replace_line_in_file('./ldap/bootstrap.ldif', 'userpassword:', 'userpassword: {MD5}'+md5_base64(password))
