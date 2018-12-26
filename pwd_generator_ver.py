import random
NUMBERS = '0123456789'
LETTERS = 'abcdefghijklmnoprstuwxyz'
SPECIAL_KEYS = "!#$%&'()*+,-./:_<=>?@][`^{|}~"


def generate_pwd():
    for i in range(3):
        pwd_length_ratio = 2
        cadence_string = ''.join([random.choice(NUMBERS) +
                                  random.choice(LETTERS) +
                                  random.choice(SPECIAL_KEYS) +
                                  random.choice(LETTERS).upper()
                                  for i in range(pwd_length_ratio)])

    list_of_random_elements = random.sample(cadence_string, len(cadence_string))
    return ''.join(list_of_random_elements)
