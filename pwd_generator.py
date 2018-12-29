import random
import string


def generated(upper_let=string.ascii_uppercase, low_let=string.ascii_lowercase, num=string.digits):
    pwd_length_ratio = 3
    special_keys = ('!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                    '_', '<', '=', '>', '?', '@', ']', '[', '`', '^', '{', '|', '}', '~', '§')
    cadence_string = (''.join([random.choice(upper_let) +
                               random.choice(low_let) +
                               random.choice(num) +
                               random.choice(special_keys)
                               for i in range(pwd_length_ratio)]))
    list_of_random_elements = random.sample(cadence_string, len(cadence_string))
    return ''.join(list_of_random_elements)
