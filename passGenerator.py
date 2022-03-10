import random

def password(n):
    password = []
    for i in range(n):
        password.append(chr(random.randint(33,127)))
    return ''.join(password)
