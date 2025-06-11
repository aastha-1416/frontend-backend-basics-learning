# Empty list
my_list = []
print(my_list)
# List with elements
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Accessing Elements
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[2])
print(my_list[-1])
print(my_list[2:4])

#Appending and Inserting Elements
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)
my_list.insert(0, 0)
print(my_list)

#Removing List Elements
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.remove(3)
print(my_list)

#Copying Lists
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(my_list)
print(new_list)

#Clearing a List  
#my_list.clear()