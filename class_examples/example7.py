example_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# enumerate

# for index, item in enumerate(example_list):
#   print(f'index is {index}, item is {item}')
  
print(f'Example list before loop: {example_list}')
for index, item in enumerate(example_list):
  example_list[index] = item - 1

print(f'Example list after loop: {example_list}')
