while True:
    txt = input("Enter your password?")
    print(txt)
    if txt.isalpha() or len(txt)<=8 or txt.isdigit:
        print(txt,"is a name")


        break
    
    else: 
        print("please don't")
