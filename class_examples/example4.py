example_list = [10, 20, 30, 40]
example_tuple = (10, 20, 30, 40)

# change first item
# example_list[0] = 1000
# print(example_list)

# example_tuple[0] = 1000
# print(example_tuple)

# Add items
# example_list.append(50)
# print(example_list)

# example_tuple = (50) + example_tuple
# print(example_tuple)

# create a list of indexes where 20 is
example_list2 = [10, 20, 30, 40, 50, 20, 20, 20]
indexes_of_20 = []

for i in range(len(example_list2)):
  if example_list2[i] == 20:
    indexes_of_20.append(i)

print(indexes_of_20)