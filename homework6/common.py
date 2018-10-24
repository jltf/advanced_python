import random
import string


def generate_string(size=8, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
