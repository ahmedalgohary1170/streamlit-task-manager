import random

def generate_id(length=6):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))
