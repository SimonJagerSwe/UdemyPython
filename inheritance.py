########## INHERITANCE ##########

# Users can be:
# - Wizards
# - Archers
# - Ogres
# - Etc


class User:
    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack():
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack():
        print(f'Attacking with arrows: arrows left: {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
print(wizard1.sign_in())