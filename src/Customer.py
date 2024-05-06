class Customer:

    first_name_position = 1
    last_name_position = 2
    email_position = 0
    password_position = 3

    def __init__(self, raw_customer):
        self.first_name = raw_customer[self.first_name_position]
        self.last_name = raw_customer[self.last_name_position]
        self.email = raw_customer[self.email_position]
        self.password = raw_customer[self.password_position]

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_email(self):
        return self.email

    def compare_password(self, password):
        return password == self.password