# Create a list of squares from 1 to 10
square = [b**2 for b in range(1,10)]
print(square)

# Make a list of numbers between 1 and 20 that are divisible by 3
a = [b for b in range(1, 20) if b%3==0 ]
print(a)

# Convert a list of words to lowercase: ["PYTHON", "JAVA", "C++"]
a = ("PYTHON", "JAVA", "C++")
b = [a.lower() for a in a]
print(b)

# From a list nums = [1, 2, 3, 4, 5], create a new list of only the even numbers multiplied by 10
num =[1, 2, 3, 4, 5]
new_num = [num for num in range(5) if num%2==0]
print(new_num)

# Given a list nums = [1, 2, 2, 3, 4, 4, 5], create a set of their squares.
a = [1,2,2,3,4,4,5]
b = [c**2 for c in a]
print(b)

# Create a set of vowels from the string "Hello World" (ignore case).
a = ('hello world')
b = {'a', 'e', 'i', 'o', 'u'}
x = set(char for char in a.lower() if char in b)
print(x)






