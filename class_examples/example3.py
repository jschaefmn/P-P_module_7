x = ['Erik', 100, True, 100, 100, 100]

# remove a value, if there's multiple of the same value,
# only removes first value
x.remove('Erik')
print(x)

while 100 in x:
  x.remove(100)
  print(x)