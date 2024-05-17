########## SUPER() ##########

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in!')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

wizard1 = Wizard('Merlin', 60)
print(wizard1.email)