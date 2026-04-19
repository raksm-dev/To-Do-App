import json
from datetime import datetime

class Game:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        
        
    def play(self , click):
        task = {
            'id' : len(self.tasks) + 1,
            'click' : click,
            'created_at' : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed' : False        
        }   
        
        
        self.tasks.append(task)
        print(f"Task '{click}' add successfully! " )
        
        
    def view_task(self):
        
        if not self.tasks:
            print("\nNo Tasks FOund!")
            return
        
        print("\n== Game will Start")
        print("-" * 50)
        
        
        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            print(f"{task['id']}. [{status}] {task['click']}")
        print("-" * 50)
        
def main():
    game = Game()
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
                
                
        choice = input("\nEnter your choice (1-3): ")
            
            
        if choice == '1':
            text = input("Enter task: ")
            game.play(text)
            game.view_task() 
            
            
             
        
        
if __name__ == "__main__":
    # main()
    todo = Game()
    todo.view_task()
