from src.CustomerLoad import CustomerLoad
class LogIn:
    def get_password(self,email_address):
        customerLoad = CustomerLoad()
        customers = customerLoad.load_customers()
        password = ""
        counter = 0
        while password == "" and counter < len(customers):
            if email_address == customers[counter].get_email():
                password = customers[counter].password
            counter += 1
        return password

    def log_in(self):
        email_address = input("Enter your email address")
        password = self.get_password(email_address)
        if password == "":
            print("You are not a user")
        else:
            if input("Enter password") == password:
                print("You are logged in")
            else:
                print("Wrong password, no second chances")
