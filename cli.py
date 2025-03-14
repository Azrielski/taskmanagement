from crud import create_user, get_all_users, create_task, get_all_tasks, update_task, delete_task

def task_management_system():
    while True:
        print("\n=== TASK MANAGEMENT SYSTEM ===")
        print("1. Register User")
        print("2. Create Task")
        print("3. List Tasks")
        print("4. Update Task Status")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter your name to register: ")
            create_user(name)

        elif choice == "2":
            users = get_all_users()
            if not users:
                print("No users found. Please register first.")
                continue

            print("Available Users:")
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")

            user_number = int(input("Select a user number: ")) - 1
            if 0 <= user_number < len(users):
                selected_user = users[user_number]
                description = input("Enter task description: ")
                create_task(description, selected_user)
            else:
                print("Invalid user selection.")

        elif choice == "3":
            tasks = get_all_tasks()
            if not tasks:
                print("No tasks available.")
            else:
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")

        elif choice == "4":
            tasks = get_all_tasks()
            if not tasks:
                print("No tasks available.")
                continue

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            task_number = int(input("Select a task number to update: ")) - 1
            if 0 <= task_number < len(tasks):
                new_status = input("Enter new status (Pending, In Progress, Completed): ")
                update_task(task_number + 1, new_status)
            else:
                print("Invalid selection.")

        elif choice == "5":
            tasks = get_all_tasks()
            if not tasks:
                print("No tasks available.")
                continue

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            task_number = int(input("Select a task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                delete_task(task_number + 1)
            else:
                print("Invalid selection.")

        elif choice == "6":
            print("Exiting Task Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    task_management_system()
