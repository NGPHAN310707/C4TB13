while True:
    Username = input("Your username?")
    codep = input("Your top-secret password?")
    if len(codep) < 8 and codep.isalpha:
        print("must have more than 8 characters")
        continue
    reenterpassword = input("Enter the same thing here?")
    if codep != reenterpassword:
        print("TRY AGAIN")
        continue
    email = input("your email?")
    if '@gmail.com' in email:
        print('Well-done')
        continue
    else:
        print("You failed in this attempt.")
