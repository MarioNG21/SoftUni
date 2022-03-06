def is_password_length_valid(password: str):
    if 6 <= len(password) <= 10:
        return True

    return False


def is_password_alphanumeric(password: str):
    is_alphanum = True

    for ch in password:
        if not (ch.isalpha() or ch.isdigit()):
            is_alphanum = False
            break
    return is_alphanum


def does_password_have_at_least_two_digits(password: str):
    digits_count = 0

    for ch in password:
        if ch.isnumeric():
            digits_count += 1

    if digits_count >= 2:
        return True
    else:
        return False


def validate_password(password: str):
    is_valid = True
    if not is_password_length_valid(password):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not is_password_alphanumeric(password):
        print("Password must consist only of letters and digits")
        is_valid = False
    if not does_password_have_at_least_two_digits(password):
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid :
        print("Password is valid")

pasword_input = input()

validate_password(pasword_input)