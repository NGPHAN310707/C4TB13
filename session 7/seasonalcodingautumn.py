while True:
    thang = int(input('Which month?'))
    if thang == 1 or thang == 3:
        print('Spring has 31 days')    
    elif thang == 2:
        print('Spring 30')
    elif thang == 5:
        print ('SUMMER 31 days')    
    elif thang == 4 or thang == 6:
        print('SUMMER 30 days')     
    elif thang == 7 or thang == 9:
        print('Autumn co 31 ngay')
    elif thang == 8:
        print ('Autumn 30')      
    elif thang == 10 or thang == 12:
        print('Winter 30')
    elif thang == 11:
        print ('Winter 31')  
    else:
        print("GLOBAL WARMING dominated Earth") 
