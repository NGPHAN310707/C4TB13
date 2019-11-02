while True:
    n = input("Enter a number?")
    if n.isalpha():
        print("PLEASE FOLLOW THE INSTRUCTION!!!")
        continue
    elif int(n) < 13:
        print("smaller 13, nice try")
    elif int(n) == 13:
        print("Exactly 13")
    else:
        print("larger than 13")
