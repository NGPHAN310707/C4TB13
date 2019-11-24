while True:
    components = {
        'FAQ:' : 'How many legs does an octopus have?',
        'Choices:' : 'Which of the following is the correct answer?',
        'A:' : '1',
        'B:' : '2',
        'C:' : '4',
        'D:' : '8'
    }
    for FAQ,Choices in enumerate(components):
        print(Choices,components[Choices])
    a = input('myansweris: ')
    if a == 'D':
        print('TOTALLY CORRECT')
    else:    
        print('INCORRECT')
