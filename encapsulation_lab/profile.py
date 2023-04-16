class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_len_valid = len(value) >= 8
        is_letter_valid = any([True for char in value if char.isupper()])
        is_digit_valid = any([True for digit in value if digit.isdigit()])

        if is_len_valid and is_letter_valid and is_digit_valid:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")


    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
