from datetime import datetime
import json

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()


    def add_task(self, description):  # Add a nem Task
        """Add a new Task more details"""
        task = {  
            'id' : len(self.tasks) + 1,
            'description' : description,
            'completed' : False,
            'created_at' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
        }
        
        self.tasks.append(task)
        print(f"Task '{description}' added successfully!")
    
    def view_task(self):
        """Diplay all task"""
        
        if not self.tasks:
            print("\nNo tasks found!")
            return
        
        print("\nYour To-Do List:")
        print("-" * 50)
    
        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            # 1. [True or Fales] Build todo list app
            # 2. [True or Fales] Read book about python
            print(f"{task['id']}. [{status}] {task['description']}")
        print("-" * 50)
            
        
    def complete_task(self , task_id):
        """Mark a task as completed"""
        # 1. Loop throught task property
        # 2. Chech for task_id
        # 3. mark task['completed'] = true
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_task()   # Add at the end of complete_task method (inside the block)
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")
        
    def delete_task(self , task_id):
        """Delete a task"""
        # 1. Loop throught task property 
        # 2. Check for task_id in tasks property
        # 3. Remove task
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_task() # Add at the end of delete_task method (inside the block)
                print(f"Task {task_id} deleted!")
                return
        print(f"Task with ID {task_id} not found!")
        
    def save_task(self):
        """Save task to file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file , indent=5)
        
    def load_tasks(self):
        """Load task from file if it exists"""
        try:
            with open(self.filename , 'r') as file:
                self.tasks = json.load(file)                  
        except FileNotFoundError:
            self.tasks = []
 
 
def main():
    todo = TodoList()
    
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add task")
        print("2. View task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")    
        
        choice = input("\nEnter your choice (1-5)")  
        
        if choice == '1':
            description = input("Enter task description: ")
            todo.add_task(description=description)
        
        elif choice == '2':
            todo.view_task()
        elif choice == '3':
            todo.view_task()
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                todo.complete_task(task_id=task_id)
            except ValueError:
                print("Please enter a vaild task ID!")
        elif choice == '4':
            todo.view_task()
            try:                          
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id=task_id)
            except ValueError:
                print("Please enter a vaild task ID!")
            
        elif choice == '5':
            print("Thank you for using the To-DO List Application!")
            break
        
        else:
            print("Invelid Choice! Please try again")
        
# Testing Class       
if __name__ == "__main__":
    main()
    # todo = TodoList()
    # print(todo.load_tasks())
    # todo.add_task("Build todo list app")
    # todo.add_task("Read Book about Python")
    # todo.save_task()
    # todo.view_task()
    # # todo.complete_task(task_id=1)
    # # todo.complete_task(task_id=2)
    # todo.view_task()
    # todo.delete_task(2) # Delete every task
    # todo.view_task()    # View Updated tasks
    
    

        