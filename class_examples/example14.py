def menu_function():
  user_wants_to_quit = False
  user_input = ''
  menu = 'What do you want to do?\n'
  menu += '1 - add to list\n'
  menu += '2 - Quit'
  user_list = []
  
  while not user_wants_to_quit:
    print(menu)
    user_input = input('> ')
    if user_input == '2':
      user_wants_to_quit = True
    elif user_input == '1':
      print('Please enter an item for the list')
      new_item = input('> ')
      user_list.append(new_item)
    else:
      print('Invalid Input')
    print(user_list)

menu_function()

user_input = float(input('Please enter a number: '))
print(type(user_input))