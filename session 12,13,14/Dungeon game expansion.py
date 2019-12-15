#Thêm bàn 2 với 2 chìa khoá, phải nhặt được đủ mới mở được cửa
#Thêm bàn 3 với quái vật xuất hiện ngẫu nhiên dọc đường, người chơi có 3 lựa chọn: Bỏ chạy, Đánh, Phòng thủ
#Mô tả chỉ số của người chơi và chỉ số của quái vật xuất hiện
#Mô tả combat, đánh theo turn, người tấn công quái vật và quái vật tấn công người, sự giảm được tính bằng các chỉ số tấn công trừ đi chỉ số phòng thủ
#Ở mỗi turn người chơi đều có quyền chạy, đánh và phòng thủ. Khả năng bỏ chạy là một xác xuất, nếu bỏ chạy không thành công, nhân vật sẽ phải chịu 1 hit từ quái vật
#Thêm bàn 4 với việc nhặt được item hồi HP, được ẩn giấu trên bản đồ
#Mô tả hòm đồ của nhân vật với các item hồi máu, tăng công, thủ trong 1 lượt đánh
#Thêm bàn 5 với việc nhặt được các item có khả năng mặc được như áo, mũ, giày hoặc cầm được như kiếm, giáo được ẩn giấu trong bản đồ
#Thêm bàn 6 với quái vật sinh ra với các chỉ số ngẫu nhiên, có critical damage khi combat
#Học viên tự nghĩ thêm kịch bản
#

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
import random
def print_board(MOP):
    for m in MOP:
        for n in m:
            print(n, end=' ')
        print()

MOP = [['_', '_', '_', '_'],
        ['_', '_', '_', '_'],
        ['_', '_', '_', 'E'], 
        ['_', 'K', '_', '_']]

key_checker = 0
key = [4,3]
player = [0,0]
movechoices = ('W', 'A', 'S', 'D')
while True:
    MOP[player[0]][player[1]] = 'P'
    print_board(MOP)
    movechoices = input("your move? ")
    movechoices = movechoices.upper()
    if move == 'S':
        MOP[player[0]][player[1]] = '_'
        if (player[0] + 1 < len(MOP)):
            player[0] += 1
            if MOP[player[0]][player[1]] == 'K':
                print("you've found a key!")
                key_checker += 1
            if MOP[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("congrats, you've just escape the dungeon!")
                    break

    elif move == 'D':
        MOP[player[0]][player[1]] = '_'
        if player[1] + 1 < len(MOP):
            player[1] += 1
            if MOP[player[0]][player[1]] == 'K':
                print("you've found a key!")
                key_checker += 1
            if MOP[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("congrats, you've just escape the dungeon!")
                    break

   

    elif move == 'A':
        MOP[player[0]][player[1]] = '_'
        if player[1] - 1 >= 0:
            player[1] -= 1
            if MOP[player[0]][player[1]] == 'K':
                print("you've found a key!")
                key_checker += 1
            if MOP[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("escaped successfully!")
                    break
     elif movechoices == 'W':
        MOP[player[0]][player[1]] = '_'
        if player[0] - 1 >= 0:
            player[0] -= 1
            if MOP[player[0]][player[1]] == 'K':
                print("you've found a key!")
                key_checker += 1
            if MOP[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("escaped!")
                    break

def printmap():
    for i in range(4):
        for j in range(4):
            print(map[i][j], end=' ')
        print()
                
def play():
    play = input("Go any of the 4 directions(A,W,S,D): ")
    if play == 'W' and position[0]>0:
        position[0] -=1
    elif play == 'A' and position[1]>0:
        position[1] -= 1    
    elif play == 'S' and position[0] < mapsize - 1:
        position[0] +=1
    elif play == 'D' and position[1] < mapsize - 1:
        position[1] += 1
    else:
            print ("invalid syntax")

printmap ()

while player['HP'] == 1:
    map()
    play()
    if position[0] == blockingwall['bwsposition'][0] and position[1] == blockingwall['bwsposition'][1]:
        print("Do not follow this way!")
    if a == 1:
        [position]['bwsposition'] - 1
    elif key['keysposition'][0] == position[0] and key['keyposition'][1] == position[1]:
        print('Congrats! You successfully found the key.')
        break
    else:
        print("Keep going")
 



skills = {'attack', 'defend', 'flee'
          }
if input = attack
['HP'] + 1
if position[1] == mongster['bwsposition'] and key['keyposition'][1] :
    play = input("Go any of the 4 direction(A,W,S,D):")
    

