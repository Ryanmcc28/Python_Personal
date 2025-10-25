selected_task = input("Please select either t1, t2 ,t3 or t4: ").lower()


def run_task(selected_task):
    if  selected_task == "t1":
      import Task_1
    elif  selected_task == "t2":
      import Task_2
    elif  selected_task == "t3":
      import Task_3
    elif  selected_task == "t4":
       import Task_4
    else:
        selected_task = input("Please enter a valid option: ")
        run_task(selected_task)

run_task(selected_task)