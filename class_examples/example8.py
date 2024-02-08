# when list gets passed through function it changes the original list
def square_funtion(arr):
  for index, item in enumerate(arr):
    arr[index] = item ** 2
  return arr

# value of y does not change
# y = 10
# print(square_funtion(y))
# print(y)

example_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_list = square_funtion(example_list)
print(new_list)
print(example_list)
