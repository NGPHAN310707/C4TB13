count = 0
while True:
    components = {
        'FAQ:' : 'Guess my favorite color?',
        'Choices:' : 'Which of the following is the most suitable answer?',
        'A:' : 'Grey',
        'B:' : 'Orange',
        'C:' : 'Blue',
        'D:' : 'White'
    }
    for FAQ,Choices in enumerate(components):
        print(Choices,components[Choices])
    a = input('myansweris: ')
    if a == 'A':
        print('TOTALLY CORRECT')
        count +=1
        print("score percentage: 100%")
    else:    
        print('INCORRECT')
        print("Your score is ", count)
        print("score percentage: 0%")
