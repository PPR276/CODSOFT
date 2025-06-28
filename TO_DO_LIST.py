print("""Hey there !!
Ready to get better...
Enter 1 to add a new task to your list .
Enter 2 to remove your completed task .
Enter 3 to view your task list .
Enter 4 to clear your task list .""")
a = int(input("enter your choice : "))
to_do = []
fn = "tasks.txt"
with open(fn,'r')as file:
        d=file.readlines()
if a==1:
    print("enter your tasks (enter 'q' to exit and complete your list): ")
    b = ""
    while b!="q":
        b=input()
        to_do.append(b)
    to_do.remove("q")
    with open(fn, "w") as file:
        for task in to_do:
            file.write(task + "\n")
    print("You have sucessfully created your list !! ")
elif a==2:
    print("enter the task number you want to delete : ")
    c = int (input())
    d.pop(c-1)
    with open(fn, 'w') as file:
        fn.writelines(d)
    print(f"Well Done !! just {len(d)} more to go..")
elif a==3:
    if len(d)==0:
        print("oops! your task list is empty. Enter 1 to add new tasks")
    else:
        for i in d:
            print (f"Task {d.index(i) +1} : {i}")
elif a==4:
    d.clear()
    print("You are all set to have a fresh start !")
else: 
    print("You have entered a wrong option. please enter a valid option !")