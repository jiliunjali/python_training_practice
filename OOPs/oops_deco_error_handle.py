# task manager to practice concepts of python
import json

class Task:
  def __init__(self, id, description, comp_status = False):
    self.id=id
    self.description=description
    self.comp_status=comp_status

class TaskManager:
  task_counter=0
  def __init__(self):
    self.all_tasks=[]
    # self.add_task(task)
    # Read existing tasks from the file if it exists
    try:
      with open("task_menu.txt", "r") as f:
        self.all_tasks = json.load(f)
    except FileNotFoundError:
      pass

  def add_task(self, task):
    TaskManager.task_counter+=1
    # so all_task is now list of dictionaries like --> [task1, task2, task3...], where each task is like{id:,descp:...}
    self.all_tasks.append({'sno':TaskManager.task_counter,'id': task.id,'description':task.description,'completionstatus': task.comp_status != False })
    with open("task_menu.txt",'w') as f:
      json.dump(self.all_tasks,f,indent=2)


  def mark_task(self,id):
    # for i,item in enumerate(self.all_tasks['id']):
    #   if self.id == item:
    #     self.all_tasks['completionstatus'][i]=True
    # else:
    #   raise ValueError("there is no task with such id, check again")
    # return f" you have successfully completed task {self.id}...... "/congratulations/""
    for task in self.all_tasks:
      if task['id']==id:
        task['completionstatus']=True
        with open("task_menu.txt",'w') as f:
          json.dump(self.all_tasks,f,indent=2)
        return f" you have successfully completed task {id}......congratulations !!!"
    raise ValueError("there is no task with such id, check again")

  def display_task(self):
    if len(self.all_tasks) != 0:
      # print("sno. \t id \t description                 \t status")
      for task in self.all_tasks:
        # print(f"{task['sno']} \t{task['id']} \t {task['description']}        \t {task['completionstatus']}")
        print(task)
      with open("task_menu.txt",'r') as f:
          json.load(f)
    else:
      print("nothing have been entered in task holder yet ")

  def delete_task(self,id):
    if len(self.all_tasks) !=0:
      for task in self.all_tasks:
        if task['id']==id:
          self.all_tasks.remove(task)
          with open("task_menu.txt",'w') as f:
            json.dump(self.all_tasks,f,indent=2)
          self.display_task()
          return f" the task {task['description']}is removed from tas holder now "
      raise ValueError("there is no task with such id ")
    else:
      print("task holder is already empty")

#a decorator to log functions
def logger(func):
  def wrapper(*args):
    print(f"Function under execution is {func.__name__}")
    result = func(*args)
    print("function got successfully executed")
  return wrapper

class TaskCLI:
  def __init__(self, task_manager):
    self.task_manager = task_manager

  def display_menu(self):
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Display Tasks")
    print("4. Delete Task")
    print("0. Exit")

  @logger
  def run(self):
    while True:
      self.display_menu()
      choice = input("Enter your choice (0-4): ")

      if choice == "0":
        print("Exiting Task Manager. Goodbye!")
        break
      elif choice == "1":
        id = int(input("give id to it: "))
        description = input("Enter task description: ")
        status = True if input("Is it completed? (y/n): ").lower() == 'y' else False
        task = Task(id, description, status)
        self.task_manager.add_task(task)
      elif choice == "2":
        task_id = int(input("Enter task ID to mark as completed: "))
        print(self.task_manager.mark_task(task_id))
        print("left tasks are : ")
        self.task_manager.display_task()
      elif choice == "3":
        self.task_manager.display_task()
      elif choice == "4":
        task_id = int(input("Enter task ID to delete: "))
        print(self.task_manager.delete_task(task_id))
        print("left tasks are : ")
        self.task_manager.display_task()
      else:
        print("Invalid choice. Please enter a number between 0 and 4.")


if __name__ == "__main__":
  task_manager = TaskManager()
  task_cli = TaskCLI(task_manager)
  task_cli.run()
