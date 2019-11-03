import random
a = (random.randint(0,100))
b = (random.randint(0,100))
print(a,"-",b,"=",a-b)
import random
a = (random.randint(0,100))
b = (random.randint(0,100))
print(a,"+",b,"+",a+b)
import random
a = (random.randint(0,100))
b = (random.randint(0,100))
print(a,"*",b,"*",a*b)
import random
a = (random.randint(0,100))
b = (random.randint(0,100))
print(a,"/",b,"/",a/b)


completed = { "addition" : False, "subtraction" : False, "multiplication" : False, "division" : False }
# The main function.
def main():
    print("""Welcome to this math based decision making game!
Instructions
\t*read
\t*think
\t*answer

    # Allow the user to read the welcome message before starting the game.
    input("Press enter to continue...")
    clear_screen()    

    print("Let's get started")
    begin_math_stage()

    print("Congratulations!")

def display_incomplete_stages():
    for stage, status in completed.items():
        if not status:
            print("\t*{}".format(stage)) 

def begin_math_stage():
    display_incomplete_stages()
    stage = input("Please select a stage:\n> ").strip().lower()  

    try:
        if not completed[stage]:
            math_stage(stage)
    except KeyError:
        print("{} is not a valid stage.".format(stage))
        begin_math_stage()

def math_symbol(choice):
    if choice == "addition":
        return "+"
    elif choice == "subtraction":
        return "-"
    elif choice == "multiplication":
        return "*"
    elif choice == "division":
        return "/"

def math_stage(stage):
    print("You have entered the {} room.".format(stage))
    print("You will now be asked a series of questions.")

    input("Press enter to continue...")

    for question in range(1, 6): # 1 - 5
        num1 = random.randint(0, 100) # 5
        num2 = random.randint(0, 100) # 5

        if num1 < num2:
            num1, num2 = num2, num1
    
        while True:
            try:
                # Question number 1: What is 5 * 5
                user_answer = float(input("Question number {}: What is {} {} {}: ".format(question, num1, math_symbol(stage), num2))) # 25
                break
            except TypeError:
                print("You have entered an invalid number! Please try again.\n> ")
        
        if round(math_dict[stage](num1, num2), 1) != user_answer:
            print("You entered the incorrect answer! The correct answer was {}".format(num1 * num2))
            math_stage(stage)
    
    print("{} has been completed!".format(stage))
    completed[stage] = True

    if not stages_complete():
        begin_math_stage()
    else:
        return False
        
            
def stages_complete():
    for status in completed.values():
        if not status:
            return False
            elif: False

clearscreen()

    

