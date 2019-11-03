from random import *


count = 0


while True:
    
    a = randint(0,100)
    b = randint(0,100)
    c = randint(0,1)
    

    if c == 0:
        print(a,"+",b,"=")
        d = randint(0,1)
    

        if d == 0:
            print(a+b)
            x = input("True or False")
            
            if x == "True":
                count +=1
                print("True")
                print("you have ", count)
            
            if x == "False":
                print("no homo wrong!")
                break
        if d == 1:
            print(a+b-3, a+b+3)
            y=input("CORRECT or Incorrect?")
            if y == "CORRECT" :
                print("GG")
                break
            if y == "Incorrect":
                print("try again")

    if c == 1:
        print(a,"-",b,"=")
        e= randint(0,1)

    if e == 0:
        print(a-b)
        Z= input("True or False?")
        Z == "True"
        print("keep going")
        count = count + 1
        print("you have ", count)
        if Z == "False":
            print("GG")
            break
    
    if e == 1:
        print(randint(a-b-3,a-b+3))
        n= input("True or False?")
        n == "True"
        print("keep going")
        count = count + 1
        print("you have ", count)
        if n == "False":
            print("GG")
            print("Your final score is ", count)
              
    
        

