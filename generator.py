'''
Basic program to generate a password.
Inspired by: https://www.lastpass.com/password-generator
'''

from random import randint

# Get the desired length of password:
passLen = input('Enter password length: ')
passLen = int(passLen)

# Pool of characters for password:
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%ˆ&*()'
charsLen = len(chars)

# Build the password by adding random characters:
password = ''
for _ in range(passLen):
    i = randint(0, charsLen - 1)
    password = password + chars[i]
    
print('Your password is: ' + password)
