########## DUNDER METHODS ##########

class Toy():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age

    def __str__(self):
        return f'{self.colour}'

action_figure = Toy('Red', 0)
print(action_figure.__str__())
print(str(action_figure))