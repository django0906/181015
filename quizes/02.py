fruit_dict = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'melon',
}

b = 0
for a in fruit_dict:
    print('[ '+str(b)+']'+a.upper()+': '+fruit_dict[a])
    b += 1
