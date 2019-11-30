pricechart = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 1200,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000    
}
brands = {
    'HP' : 20,
    'DELL' : 60,
    'MACBOOK' : 10,
    'ASUS' : 30,
    'TOSHIBA' : 10,
    'FUJITSU' : 15,
    'ALIENWARE' : 5
}
print('price of MACBOOK: ',pricechart['MACBOOK'])
a = input('preferred computer brand: ')
if a in pricechart:
    print('pricechart you choose: ',pricechart[a])
else:
    print('cannot found')    
print('3 MACBOOK computers have a total amount of:',pricechart['MACBOOK'] * 3)  
uwant = input('preferred brad and quantity:')
filter = uwant.split(':')
if filter[0] in pricechart and filter[1].isalpha:
    print('computer brand: ',filter[0],'quantity: ',filter[1], 'total: ',pricechart[filter[0]]*int(filter[1]))
    uwant[filter[0]] =  uwant[filter[0]] - int(filter[1]) 
    print('left-overs:',uwant)
else:
    print('inappropriate!') 
