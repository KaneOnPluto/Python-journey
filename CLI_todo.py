tasks = []

while True:
    
    print("*========================*\n")
    print("1. Add task")
    print("2. Delete task")
    print("3. Show tasks")
    print("4. Exit")
    print("\n*========================*")
    
    try:

        choice = int(input("\nEnter your choice: "))
        
        match choice:
    
            case 1:
            
                task = input("\nEnter your task: ")
        
                tasks.append(task)
                
                input("\nPress Enter to exit to menu.")
            
          
            case 2:
            
                if not tasks:
                    print("\nNo tasks!")
                    
                else:
                       
                    try:
                        for index, task in enumerate(tasks, start=1):
                            print(f"{index}: {task}")
                      
                        deleted_task = int(input("Delete task number: "))
                    
                        if 1 <= deleted_task <= len(tasks):
                        
                            del tasks[deleted_task - 1]
                        
                        else:
                            print("Invalid task number")
                    
                        input("\nPress Enter to exit to menu.")
                
                    except ValueError:
                    
                        print("Invalid input! Please enter a valid integer.")
                        
            case 3:
            
                if not tasks:
                    print("\nNo tasks!")
                    
                else:
                       
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}: {task}")
            
                    input("\nPress Enter to exit to menu.")
            
            case 4:
                break
        
            case _:
                print("\nInvalid!")
                
    except ValueError:
        print("Invalid choice!")
