########## EXERCISE: TRANSLATOR ##########
from translate import Translator

translator = Translator(to_lang = 'es')
try:
    with open('test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('Check your filepath, you silly puppy!')