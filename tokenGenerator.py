from random import choice
import string
abcdario = string.ascii_letters + string.digits
token = ''
for i in range(16):
    item = choice(abcdario)
    token += item
print(token)