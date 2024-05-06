import random
import string

def create_promocode():
    return ''.join(random.choice(string.ascii_lowercase)).join(str(random.randint(1000, 9999))).title()