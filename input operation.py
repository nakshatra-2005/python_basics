# Ask the user for their name and print a greeting like:
# "Hello, [name]! Wel
name = input('enter your name')
print('hello,', name+ '! welcome!')

# Ask the user to enter two numbers, add them, and print the result.
a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=a+b
print(c)

# Ask the user for their birth year, calculate their age, and display it.
num = int(input('enter your birth year'))
a=2025
b=num
c=eval('2025-num')
print(c)

# Ask the user for a number and check whether it is even or odd.
num = int(input('enter a number'))
if num%2==0:
    print("its a even number")
else:
    print("its a odd number")

# Take the radius as input and calculate the area using the formula:
radius = float(input('enter the radius'))
area = 3.14 * radius * radius
print('the area of the circle is:', area)

# Student Details
name = input('name of the student')
age = int(input('age of the student'))
num = float(input('enter marks of the student'))
subject = input('favorite subject')
print(name, age, num, subject)






