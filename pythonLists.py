# LISTS

# A list is an ordered set of objects
list1 = [10, 20, 30, 40]
list2 = ["A String", 1]

# A list of lists
my_list_of_lists = [['Hi', 5], ['Hello',2]]

# Zip Function - returns an object that contains a list of pairs
# combines the two lists so element 1 of list 1 is paired with element 1 of list 2
# only pairs items until it reaches the length of the shorter list
myObject = zip(list1,list2)
print(list(myObject))

# Empty List
my_empty_list = []

# Append - adds a new element to the end of a list
my_list = [1, 2]
my_list.append(3)
print(my_list)

# Combining Lists
old_list = [1, 2, 3]
new_list = old_list + [4, 5]
print(new_list)

# Range Function - returns an object with the numbers 0 - (n-1)
my_range = range(5) # 0, 1, 2, 3, 4
my_range2 = range(2, 6) # 2, 3, 4, 5
my_range3 = range(1, 50, 10) # 1, 11, 21, 31, 41

print(list(my_range))

# Length of a List
list_length = len(list1)

# Referencing an element of a list
num = list1[0]

# Referencing the last element of a list
last_num = list1[-1]

# Slicing
new_list = list1[1:3] # 20, 30
new_list2 = list1[:2] # starts at index 0; thus will result in 10, 20
new_list3 = list1[2:] # ends at the end of the list; 30, 40
new_list4 = list1[-3:] # gives the last 3 elements; 20, 30, 40
print(new_list, new_list2, new_list3, new_list4)

# counting matching elements
my_name = ['k', 'y', 'l', 'a', 'y', 'u', 'j', 'i', 'r', 'i']
num_y = my_name.count('y')
num_i = my_name.count('i')

# in place sort
list_to_sort = [10, 5, 6, 2, 3]
list_to_sort.sort() # does not return anything
print(list_to_sort)

# another way to sort
list_to_sort2 = [20, 30, 10, 0] # this list will remain unaffected
sorted_list = sorted(list_to_sort2) # returns the sorted list
print(list_to_sort2, sorted_list)

# pop - takes the last item off a list and returns in
list_to_pop = [1, 2, 3]
last_item = list_to_pop.pop()
print(last_item)

# finding the index
list_to_search = [1, 2, 3, 4, 5]
index_of_3 = list_to_search.index(3)
print(index_of_3)
# if you give a value that is not in the list, there will be an error (NameError)

# list comprehensions - puts items from a list into another list if they meet a condition
# format: new_list = [item_to_add for temp_item_var in some_list if *temp_item_var meets some condition*]
itemList = ["Fruit", "Not Fruit", "Fruit"]
newList = [item for item in itemList if item == "Fruit"]
print(itemList, newList)

numList = [0,10,20,30]
added10 = [num + 10 for num in numList]
print(added10)
