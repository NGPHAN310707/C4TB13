colours = ['blue', 'green', 'yellow','Dark', 'white']

while len(colours) != 0:
    option = input('ENTER YOUR THING: ')
    if option.isdigit():
        print('Pop ',option,' (',colours[int(option)],')')
        colours.pop(int(option))
    elif option.isalpha():
        isIn = False
        for i in colours:
            if i == option:
                colours.remove(i)
                print('Remove',option)
                isIn = True
                break
        if isIn == False:
            print('Cannot found ',option)
    else:
        print('WRONG')
    print(colours)
