#6: Write a python program to count the number of even and odd numbers in a series of numbers

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
def even_odd_GET(n):
    even = 0
    odd = 0
    for number in n:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Number of odd numbers is ", odd, "and number of even numbers is ", even)

even_odd_GET(numbers)