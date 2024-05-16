########## PARAMETERS ##########

# Parameters
def say_hello(name = 'Darth Vader', emoji = '^_^'):
    print(f'Hellooooooo {name} {emoji}!')

# Arguments / Positional arguments
say_hello('Simon', ':)')
say_hello('Marie', ':)')
say_hello('Zara', ':)')

# Keyword arguments
say_hello(emoji=':)', name = 'Simon')       # Bad practice?
say_hello(name = 'Simon', emoji = ':)')
say_hello()
say_hello('Timmy')