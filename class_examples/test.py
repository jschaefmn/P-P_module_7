# list1 = [1,2,3]
# list2 = []
# for element in list1:
#   list2.append(element)
  
# list1 = [4,5,6]

# print(list2)

old_tuple = (100,200,300,400)

to_list = list(i for i in old_tuple: i + 1)
print(to_list)

to_tuple = tuple(i for i in to_list)
print(to_tuple)