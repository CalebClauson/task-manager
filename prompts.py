WIDTH = 30

def welcome():
    print("Welcome to the task Manager.".center(WIDTH))

def selection():
    print(
    f"{'-' * WIDTH}\n"
    f"Select what you would like to do?\n"
    f"{'-' * WIDTH}\n"
    "1. View Tasks\n"
    "2. Add Tasks\n"
    "3. Edit Task\n"
    "4. Complete Task\n"
    "5. Delete Task\n"
    "6. Quit"
)


def choice_input():
    while True:
        try:
            choice = int(input("").strip())
            if choice > 6 or choice == 0:
                print("Oops! That wasn't a number in range! Try Again....")
        except  ValueError:
            print("Please Enter a Number.")
        else:
            return choice
        
