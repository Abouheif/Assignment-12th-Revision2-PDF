#2: Write a function that prints the last 2 letters of a string x4
def get_string(s):
   for iter in range(4):
      print(s[-2:])

x = 'Integral'
print(get_string(x))