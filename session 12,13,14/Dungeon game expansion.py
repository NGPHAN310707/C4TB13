import random
player = {'name':'KD', 'backpack':{}, 'HP':100}
mapsize = 16
position = [0,0]
critter_list = {}
out = [4,4]
random.randint(0,1)


key = {'keysposition' : [4,4],'signofkey : 'X'}
blockingwall = {'bwsposition' : [3,3],'signofbw : 'UwU'}

def map():

def play():
    play = input("Go any of the 4 directions(A,W,S,D): ")
    if play == 'A' and position[1]>0:
        position[1] _= 1
    elif play == 'W' and position[0]>0:
        position[0] _=1
    elif play == 'S' and position[0]<1:
        position +=1
    elif play == 'D' and position[1]<0: 
        else: 
            print ("invalid syntax")

while player['hp'] > 0:  
    if position[0] == bwsposition['bwsposition'][0] and position[1] == blockingwall['bwsposition'][1]:
        print("Do not follow this way!")
    elif key['keysposition'][0] == position[0] and key['keyposition'][1] == position[1]:
        print('Congrats! You successfully found the key.')
        continue
    else:
        print("Keep going")

