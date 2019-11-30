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
set['TOSHIBA'] = 10
b = input('add item ')
c = input('number adding ')
set[b] = c
set['DELL'] = 10
set['MACBOOK'] = 2
print('number of MACBOOKs:',set['MACBOOK'])
e = 0
for i in set.values():
    e += int(i)
print('total: ',e)
set['FUJITSU'] = 15
set['ALIENWARE'] = 5
g = 0
for f in set.values():
    g += int(f)
print('total: ',g)  
