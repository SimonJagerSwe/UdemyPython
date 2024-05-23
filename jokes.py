########## JOKES ##########
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)
# dirty_joke = pyjokes.get_joke('en', 'explicit')
# print(dirty_joke)
chuck_joke = pyjokes.get_joke('en', 'chuck')
print(chuck_joke)