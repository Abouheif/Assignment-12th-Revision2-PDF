#7: Construct a 1-5-1 * sideways pyramid

x = '*'
n = 5

for iter in range(1, n+1):
    print(x * iter)

for iter in range(n-1, 0, -1):
    print(x * iter)