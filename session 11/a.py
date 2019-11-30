set = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}
print(set['MACBOOK'])
a = input ('enter your preferred number?')
if a == 'HP':
    print('quantity stored',set['HP'])
if a == 'DELL':
    print('quantity stored',set['DELL'])
if a == 'ASUS':
    print('quantity stored',set['ASUS'])


else:
    print('not included this')
