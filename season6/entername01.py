while True:
    txt = input("Enter a name?")
    print(txt)
    if txt.isdigit():
        continue
    else:
        print("Verified")
        break
    
