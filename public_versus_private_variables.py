########## PRIVATE VERSUS PUBLIC VARIABLES ##########

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name           # UNDERSCORE CREATES LOCAL VARIABLE
        self._age = age

    def run(self):
        print('Run')

    def speak(self):
        print(f'My name is {self._name} and I am {self._age}')

player1 = PlayerCharacter('Simon', 34)

print(player1.speak())

# SINGLE UNDERSCORE MEANS LOCAL VARIABLE, DOUBLE MEANS GLOBAL, SIGNIFIES "DON'T TOUCH THIS!!!"