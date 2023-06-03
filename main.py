import random

import string

def generate_password(length, characters):

    password = ""

    for _ in range(length):

        password += random.choice(characters)

    return password

def recursive_password_generator(min_length, max_length, count, characters, prefix="", suffix="", separator=""):

    if count == 0:

        return []

    length = random.randint(min_length, max_length)

    password = generate_password(length, characters)

    password_with_prefix_suffix = prefix + separator + password + separator + suffix

    return [password_with_prefix_suffix] + recursive_password_generator(min_length, max_length, count - 1, characters, prefix, suffix, separator)

def validate_password(password, constraints):

    

    for constraint in constraints:

        if not constraint(password):

            return False

    return True

def generate_valid_password(min_length, max_length, constraints, characters, prefix="", suffix="", separator=""):

    length = random.randint(min_length, max_length)

    password = generate_password(length, characters)

    password_with_prefix_suffix = prefix + separator + password + separator + suffix

    if validate_password(password_with_prefix_suffix, constraints):

        return password_with_prefix_suffix

    else:

        return generate_valid_password(min_length, max_length, constraints, characters, prefix, suffix, separator)

def recursive_valid_password_generator(min_length, max_length, count, constraints, characters, prefix="", suffix="", separator=""):

    if count == 0:

        return []

    password = generate_valid_password(min_length, max_length, constraints, characters, prefix, suffix, separator)

    return [password] + recursive_valid_password_generator(min_length, max_length, count - 1, constraints, characters, prefix, suffix, separator)

def contains_uppercase(password):

    return any(char.isupper() for char in password)

def contains_lowercase(password):

    return any(char.islower() for char in password)

def contains_digit(password):

    return any(char.isdigit() for char in password)

constraints = [contains_uppercase, contains_lowercase, contains_digit]

characters = string.ascii_letters + string.digits + string.punctuation

passwords = recursive_valid_password_generator(8, 12, 5, constraints, characters, prefix="my", suffix="password", separator="_")  

for password in passwords:

    print("The Generated Password is :" +password)

