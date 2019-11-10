Ilike = ['Lacoste','Adidas','Supreme']
Iwant = input('C or U or R or D? ')
if Iwant == 'c' or 'C':
    b = input('Which subset do you prefer to add on?')
    Ilike.append(b)
    print(Ilike)
if Iwant == 'r' or 'R':
    if Ilike == 0:
        print('No subset')
    for abc in enumerate(Ilike):
        print(*abc)
if Iwant == 'u' or 'U':
    a = len(Ilike)
    x = int(input('Which subset do you prefer to change?'))
    if x < a :
        Ilike[x] = input('Change what?')
        print(Ilike)
    elif x > a:
        print('Inappropriate changes')    
if Iwant == 'd' or 'D':
    y = int(input('Which subset do you prefer to change?'))
    a = len(Ilike)
    if y < a:
        Ilike.pop(y)
        print(Ilike)
    elif y > a:
        print('Inappropriate changes')
else:
    print('FOLLOW THE INSTRUCTIONS!!!')

while True:
    repeat()
