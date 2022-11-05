#Intructions
print("---------------------------------------------------------------")
print("Hello User! Your wish is my command >__<")
print("---------------------------------------------------------------")
print("This is your array: [5, 3, 60, 40, 99, 8, 10, 35, 44, 101] ")
print("---------------------------------------------------------------")
print("Menu: \n 1 -> Show how many elements \n 2 -> Add an element \n 3 -> Merge another list \n 4 -> Delete an element \n 5 -> Remove last element \n 6 -> Arrange in ascending order \n 7 -> Arrange in descending order \n 8 -> Reverse the elements \n 9 -> Find the smallest element \n 10 -> Find the largest element \n 11 -> Sum of all elements \n 12 -> Index of an element \n 13 -> Insert an element")
print("---------------------------------------------------------------")
print("Please select in the menu (1-6)")
print("---------------------------------------------------------------")

#start codings
my_list = [5, 3, 68, 40, 99, 8, 10, 35, 44, 101]

user_input = input("What do you want to do: ")
print("---------------------------------------------------------------")

#Show how many elements  
if user_input == "1":
    length = len(my_list)
    print(length)

#Add an element   
if user_input == "2":
    add_ele = input("Enter an element that you want to add:")
    print("---------------------------------------------------------------")
    my_list.append(add_ele)
    print("The element has been added! \n--------------------------------------------------------------- \nThis is the new array:")
    print(my_list)
    
#Merge another list
if user_input == "3":
    list = input("Enter list at least 3 elements: ")
    my_list.extend(list)
    print("The element has been merged! \n--------------------------------------------------------------- \nThis is the new array:")
    print(my_list)

#delete an element
if user_input == "4":
    del_ele = input("Enter an element on the list you want to delete: ")
    my_list.remove(int(del_ele))
    print("The element has been deleted! \n--------------------------------------------------------------- \nThis is the new array:")
    print(my_list)

#pop an element
if user_input == "5":
    my_list.pop()
    print("The element has been deleted! \n--------------------------------------------------------------- \nThis is the new array:")
    print(my_list)

else:
    print("Done")