
WIDTH = 30
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
    

def view_tasks():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    print("-" * WIDTH)

    has_tasks = False

    for i, task in enumerate(tasks, start=1):
        if task.startswith("[✓]"):
            print(GREEN + f"{i}. {task.strip()}" + RESET)
            has_tasks = True
        elif task.startswith("[]"):
            print(f"{i}. {task.strip()}")
            has_tasks = True

    if not has_tasks:
        print(RED + "Task List is currently EMPTY." + RESET)

    print("-" * WIDTH)            

def add_task():
    print("-" * WIDTH)
    print("Please enter your task:")
    print(RED + "Type 'r' to reset." + RESET)
    print("-" * WIDTH)

    task = input("").strip()
    task = task[0].upper() + task[1:]
    if task in ["r", "reset", "cancel", "quit"]:
        return
    elif task:
        with open('tasks.txt', 'a') as f:
            f.write("[] " + task + "\n")

def edit_task():
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    while True:
        view_tasks()
        print("-" * WIDTH)
        print("Please enter the line you would like to Edit:")
        print(RED + "Type 'r' to reset." + RESET)
        print("-" * WIDTH)

        task_edit = input("").strip().lower()

        if task_edit in ["r", "reset", "cancel", "quit"]:
            return

        try:
            task_edit = int(task_edit)
        except ValueError:
            print(RED + "Please enter a valid integer." + RESET)
            continue

        if task_edit < 1 or task_edit > len(tasks):
            print(RED + "Ooops that wasn't a valid number..." + RESET)
            continue

        if tasks[task_edit - 1].startswith("[✓]"):
            print(RED + "You can't edit a completed task silly." + RESET)
            continue

        print("-" * WIDTH)
        print("Please enter your updated task:")
        print(RED + "Type 'r' to reset." + RESET)
        print("-" * WIDTH)

        new_task_text = input("").strip()

        if new_task_text.lower() in ["r", "reset", "cancel", "quit"]:
            return

        tasks[task_edit - 1] = new_task_text + "\n"

        with open('tasks.txt', 'w') as f:
            f.writelines(tasks)

        return

def delete_task():

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    while True:
        view_tasks()
        print("-" * WIDTH)
        print("Please enter the line you would like to Delete:")
        print(RED + "Type 'r' to reset." + RESET)
        print("-" * WIDTH)
        try:
            task_edit = input("").strip()
            if task_edit in ["r", "reset", "cancel", "quit"]:
                return
            task_edit = int(task_edit)
            if 1 <= task_edit <= len(tasks):
                #since when we read lines it reads as a list pop works
                tasks.pop(task_edit - 1)
                with open('tasks.txt', 'w') as f:
                    f.writelines(tasks)
                    return
            else:
                print(RED + "Ooops that wasn't a valid number..." + RESET)
        except ValueError:
            print("Please enter a valid integer.")

def complete_task():

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    while True:
        view_tasks()
        print("-" * WIDTH)
        print("Please enter the line you would like to complete:")
        print(RED + "Type 'r' to reset." + RESET)
        print("-" * WIDTH)
        try:
            task_edit = input("").strip()
            if task_edit in ["r", "reset", "cancel", "quit"]:
                return
            task_edit = int(task_edit)
            if task_edit < 1 or task_edit > len(tasks):
                print(RED + "Ooops that wasn't a valid number..." + RESET)
                continue
            else:
                completed = tasks[task_edit - 1].replace("[]", '').strip()

        #check if complete
                if tasks[task_edit - 1].startswith("[✓]"):
                    print(RED + "It's already completed silly." + RESET)
                    continue

        #completion
                else:
                    tasks[task_edit - 1] = "[✓] " + completed + "\n"
                    with open('tasks.txt', 'w') as f:
                        f.writelines(tasks)
                        return
        except ValueError:
            print("Please enter a valid integer.")