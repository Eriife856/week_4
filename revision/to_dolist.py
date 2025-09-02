#create empty list
tasks=[]

#adding tasks
def add_tasks(task):
    tasks.append(task)
    print(f'tasks  "{task}" added')

#removing tasks
def remove_task(task):
    if task in tasks:
       tasks.remove(task)
       print(f'tasks "{task}" removed')
    # else:
    #  print("tasks not found")


#viewing tasks
def view_tasks():
 if not tasks:
       print("no tasks in your list")
 else:
   for index, task in enumerate(tasks,1):
       print(f'{index} {task}')

#run program using while loop
while True:
   print(""" options: 1. Add task  2. remove task  3. view task  4 . exist""")

   choice=input("enter your choice: ")
   if choice == "1":
      task = input("enter your tasks: ")
      add_tasks(task)
   elif choice == "2":
      task = input("enter task to be removed")
      remove_task(task)

   elif choice =="3":
      view_tasks()
   elif choice == "4":
      print("existing program. bye!")
      break
   else:
      print("invalid choice.input a valid option. ")
      
