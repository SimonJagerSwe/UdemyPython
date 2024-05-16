########## OOP ##########

# Example 1
'''
class PlayerCharacter:    
    membership = True               # Class object attribute, static
    def __init__(self, name, age):
        self.name = name            # Attribute
        self.age = age

    def run(self):
        print('Run')
        return 'Done'

    def shout(self):
        print(f'MY NAME IS {self.name}')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player2.membership)
print(player1.shout())
print(player2.shout())
'''

# Example 2, __init__
class PlayerCharacter:
    membership = True
    def __init__(self, name = 'Anonymous', age = 0):
        if (age > 18):
            self.name = name
            self.age = age
        
    def shout(self):
        print(f'MY NAME IS {self.name}')

player1 = PlayerCharacter('Tom', 10)
print(player1.shout())