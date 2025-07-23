class User:
    def __init__(self, first_name, last_name):
        self.userFirstName = first_name
        self.userLastName = last_name

    def sayFirstName(self):
        print("Меня зовут ", self.userFirstName)
    
    def sayLastName(self):
        print("Моя фамилия ", self.userLastName)

    def sayFullName(self):
        print("Мои имя и фамилия ", self.userFirstName, self.userLastName)
