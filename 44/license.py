import string
import secrets
def gen_key(parts:int=4,chars_per_part:int=8):
    alphabet = string.ascii_uppercase + string.digits
    key = '-'.join(''.join(secrets.choice(alphabet) for i in range(chars_per_part)) for i in range(parts))
    return key
