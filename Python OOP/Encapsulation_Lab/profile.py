class Profile:
    username_min_length = 5
    username_max_length = 15

    min_uppercase_letters_count = 1
    password_min_length = 8
    min_digits_counts = 1

    def __init__(self, username, password):
        self.username = username # stava properti ?
        self.password = password

    def __validate_password(self, password):
        if len(password) < self.password_min_length:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        if len([x for x in password if x.isupper()]) < self.min_uppercase_letters_count:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if len([x for x in password if x.isdigit()]) < self.min_digits_counts:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __valid_username(self, username):
        username_len = len(username)
        if self.username_min_length > username_len \
                or self.username_max_length < username_len :
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def username(self):
        return self.__username


    @username.setter
    def username(self, value):
        self.__valid_username(value)
        self.__username = value

    @property
    def password(self):
        return ''.join('*' * len(self.__password))


    @password.setter
    def password(self, new_pass):
        self.__validate_password(new_pass)
        self.__password = new_pass

    def __str__(self):

        result = f'"You have a profile with username: "{self.username}" and password: {self.password}.'
        return result


profile_with_invalid_password = Profile('My_username', 'My-password')