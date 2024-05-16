########## LOGICAL OPERATORS ##########

print(4 < 5)
print(4 > 5)
print(4 == 5)

# OPERATORS:
# >
# <
# =<
# >=
# ==
# !=
# not

##### EXERCISE #####

is_magician = False
is_expert = False

# Check if magician AND expert print "you are a master magician"
if is_expert and is_magician:
    print('You\'re a master magician!' )

# Check if magician but not expert print "at least you're getting there"
elif is_magician:
    print('At least you\'re getting there!')

# If not a magician print "you need magic powers"
else:
    print('You need magic powers!')
