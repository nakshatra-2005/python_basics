# FUNCTIONS
#Write a function that takes a number and prints whether it is even or odd.
from Comprehension import square


def even_odd(number):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number}is odd")
even_odd(8)

# lambda functions
# Write a lambda function to square a number.
num = [2, 3, 4, 5, 6, 8]
squares = list(map(lambda n : n*2, num))
print(squares)

# Write a lambda function that returns True if a number is even, False otherwise.
evens = lambda n : n%2==0
print(evens(4))
print(evens(9))

#Create a lambda function that takes two numbers and returns their sum.
sums = lambda a,b : a+b
print(3+5)
print(8+9)
