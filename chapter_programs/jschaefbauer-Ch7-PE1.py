# This program takes a user's input for daily sales
# and calculates the total sales for the week    

NUM_DAYS = 7  

def main():
  sales = [0] * NUM_DAYS
  total = 0
  for i in range(len(sales)):
    sales[i] = float(input(f'Enter a store\'s sales for  day #{i + 1}: '))
    sales.append(sales)
    total += float(sales[i])
  print(f'You made ${total:,} this week')

main()