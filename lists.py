########## LISTS ##########
# li = [1, 2, 3, 4, 5]          # LIST WITH INTEGERS
# li_2 = ['a', 'b', 'c']        # LIST WITH STRINGS
# li_3 = [1, 2.5, 'a', True]    # MIXED LIST

# amazon_cart = ['Notebooks', 'Sunglasses']
# print(amazon_cart)
# print(amazon_cart[0])
# print(amazon_cart[1])


##### LIST SLICING #####
amazon_cart = [
    'Notebooks',
    'Sunglasses',
    'Toys',
    'Grapes'
]

print(amazon_cart[0::2])

amazon_cart[0] = 'Laptop'
print(amazon_cart)

new_cart = amazon_cart[0:3]
new_cart[0] = 'Gum'
print(new_cart)
print(amazon_cart)