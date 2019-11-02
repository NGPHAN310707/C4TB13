while True:
    n = input("?")
    if int(n) < 0:
        print("Any number")
        continue
    elif int(n) % 2 == 0:
        print("you choose an even number")
    else:
        print("you choose an odd number")
