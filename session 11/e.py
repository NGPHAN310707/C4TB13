import random
set = {
    'name' : 'Light',  
    'age' : 17,
    'strength' : 8,
    'defense' : 10,
    'HP' : 100,
    'backpack' : ['shield','bread loaf'],
    'gold' : 100,
    'level' : 2
}
set['gold'] + 50
adventure['backpack'].append('flight stone')
adventure['pocket'] = ['monstersdex','flashlight']
skill = {
    'skill' : {
        'name' : 'tackle',        
        'minimum level' : 1,
        'damage' : 5,
        'hit rate' : 0.3        
    },
    'skill2' : {
        'name' : 'qick attack',        
        'minimum level' : 2,
        'damage' : 3,
        'hit rate' : 0.5        
    },
    'skill3' : {
        'name' : 'strong kick',        
        'minimum level' : 4,
        'damage' : 9,
        'hit rate' : 0.2        
    }
}
for i,a in enumerate(skill):
    print(i+1,skill[a])
c = random.randint(0,1)    
b = input('ban muon dung skill nao: ')
    pass
