########## MULTIPLE INHERITANCE ##########

class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
        
    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left: {self.num_arrows}')

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def run(self):
        print('Ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)

HyBo1 = HybridBorg('Borgie', 50, 100)
print(HyBo1.run())
print(HyBo1.check_arrows())
print(HyBo1.sign_in())