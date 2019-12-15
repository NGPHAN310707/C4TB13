import random
player = {'name':'KD', 'backpack':{}, 'HP':100}
mapsize = 16
position = [0,0]
critter_list = {}
exit = [4,4]
random.randint(0,1)
key = {'keysposition' : [4,4],'signofkey': 'k'}
blockingwall = {'bwsposition' : [3,3],'signofbw' : 'I'}

map =[
        ['-' for i in range(4)],
        ['-' for i in range(4)],
        ['-' for i in range(4)],
        ['-' for i in range(4)]
     ]
def printmap():
    for i in range(4):
        for j in range(4):
            print(map[i][j], end=' ')
        print()
        
import random
def printmap(MOP):
    for x in MOP:
        for y in x:
            print(y, end=' ')
        print()

MOP = [['_', '_', '_', 'E'],
        ['_', '_', '_', '_'],
        ['_', '_', '_', '_'], 
        ['K', '_', '_', '_']]

start = 0
key = [4,1]
player = [0,0]
movechoices = ('W','A','S','D')
while True:
    MOP[player[0]][player[1]] = 'P'
    printmap(MOP)
    movechoices = input("which directions? ")
    movechoices = movechoices.upper()
    
    if movechoices == 'S':
        MOP[player[0]][player[1]] = '_'
        if (player[0] + 1 < len(MOP)):
            player[0] += 1
            if MOP[player[0]][player[1]] == 'K':
                print("key has been found!")
                start += 1
            if MOP[player[0]][player[1]] == 'E':
                if start == 1:
                    print("escaped!")
                    break

    elif movechoices == 'D':
        MOP[player[0]][player[1]] = '_'
        if player[1] + 1 < len(MOP):
            player[1] += 1
            if MOP[player[0]][player[1]] == 'K':
                print("Key has been found!")
                start += 1
            if MOP[player[0]][player[1]] == 'E':
                if start == 1:
                    print("escaped!")
                    break

   

    elif movechoices == 'A':
        MOP[player[0]][player[1]] = '_'
        if player[1] - 1 >= 0:
            player[1] -= 1
            if MOP[player[0]][player[1]] == 'K':
                print("Key has been found!")
                start += 1
            if MOP[player[0]][player[1]] == 'E':
                if start == 1:
                    print("escaped successfully!")
                    break
                
    elif movechoices == 'W':
        MOP[player[0]][player[1]] = '_'
        if player[0] - 1 >= 0:
            player[0] -= 1
            if MOP[player[0]][player[1]] == 'K':
                print("Key has been found!")
                start += 1
            if MOP[player[0]][player[1]] == 'E':
                if start == 1:
                    print("escaped!")
                    break

