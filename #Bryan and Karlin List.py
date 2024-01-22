#Bryan and Karlin 


list = ["Cherry", "Bananna", "Apple"]



def listmaker():
    action = input("Welcome to your list! You can add something to your list, delete something from your list, view your list, mark a task as completed, or exit your list.")
    if action == "add":
        addtolist = input("What would you like to add to the list?")
        list.append(addtolist)
        print(list)
    if action == "delete":
        deletefromlist = input("What would you like to delete")
        list.remove(deletefromlist)
        print(list)
    if action == "View":
        print("Current to do list:")
        for item in list:
            print(item)
    
    if action == "exit":
        print("Leaving the program.")
    
    if action == "mark as done":
        markdone = (input("Which item would you like marked done?"))
        i = list.index(markdone)
        list[i] = markdone + "☑"
        print(list[i])
    if action == "delete all":
        list.clear()
        print(list)
    if action == "sort":
        list.sort()
        print(list)




        
        

        


listmaker()

        

