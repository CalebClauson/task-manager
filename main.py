from prompts import * 
from task import view_tasks, add_task, delete_task, edit_task, complete_task

def main():
    welcome()

    while True:
        selection()

        choice = choice_input()

        if choice == 1:
            view_tasks()

        elif choice == 2:
            add_task()
        
        elif choice == 3:
            edit_task()
        
        elif choice == 4:
            complete_task()
        
        elif choice == 5:
            delete_task()
        
        elif choice == 6:
            print("-" * WIDTH)
            print("Goodbye!")
            break
main()