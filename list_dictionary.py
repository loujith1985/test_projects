menu = [['Egg', 'Bagel', 'Coffee'],
        ['BLT', 'PBJ', 'Turkey Sandwich'],
        ['soup', 'rice', 'fruits'] ]

breakfast = menu[0]

print('nreakfast items are', breakfast)

my_fav = menu[0][1]
print('my favorite item is', menu[0][0])

menu = { 'Breakfast': ['Egg', 'Bagel', 'Coffee'],
        'Lunch': ['BLT', 'PBJ', 'Turkey Sandwich'],
        'Dinner': ['soup', 'rice', 'fruits'] }

print('breakfast Menu:\t', menu['Breakfast'])
print('lunch Menu:\t', menu['Lunch'])
print('Dinner Menu:\t', menu['Dinner'])