########## SUPER() ##########

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in!')

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)        # OPTION 1
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)      # WILL THROW ERROR WITHOUT User.__init__(self, email) or super().__init__(self, email)