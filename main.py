import random
import string

numbers = string.digits
letters_lower = string.ascii_lowercase
letters_upper = letters_lower.upper()
simbols = string.punctuation
char_types = [numbers, letters_upper, letters_lower, simbols]
all_chars = numbers + letters_upper + letters_lower + simbols


def is_type_exist_on_password(char_type, password):
    return min([0 if char in password else 1 for char in char_type])


while True:
    password = ''
    for i in range(32):
        password += all_chars[random.randint(0, len(all_chars) - 1)]
    if not max([is_type_exist_on_password(char_type, password) for char_type in char_types]):
        break
print(password)

