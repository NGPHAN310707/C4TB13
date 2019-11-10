import random
while True:
    XD = ['memelord','memelord','memelord']
    random.shuffle(XD)
    XD = XD[0]
    k = list(XD)
    random.shuffle(k)
    print(*k)
    h = input('Guess what? ')
    if h == XD:
        print('You are right! Congrats!')
    else:
        print('WRONG')
