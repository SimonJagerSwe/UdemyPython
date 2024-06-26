########## @classmethod and @staticmethod ##########


class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'MY NAME IS {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls ('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Tom', 20)
player3 = PlayerCharacter.adding_things(2, 3)

print(player1.shout())
print(player3.age)

print(player1.adding_things2(4, 6))