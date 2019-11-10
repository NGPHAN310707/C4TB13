colorset = ['red', 'blue', 'black','purple', 'white']

while len(colorset) != 0:
    option = input('Enter an item that you prefer to delete: ')
    if option.isdigit():
        print('Pop',option,'(',colorset[int(option)],')')
        colorset.pop(int(option))
    elif option.isalpha():
        isIn = False
        for i in colorset:
            if i == option:
                colorset.remove(i)
                print('Remove',option)
                isIn = True
                break
        if isIn == False:
            print('Cannot found',option)
    else:
        print('WRONG')
    print(colorset)
