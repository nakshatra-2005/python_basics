#Zero Division Practice
a = 18
b = 9
try:
    print("resource open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("hey! you cannot divide a number by zero", e)
except ValueError as e:
    print("Its a Invalid value")
finally:
    print("resource closed")


# Type Error Practice
a = 66
b = "Nakshatra"
try:
    print(a+b)
except TypeError as e:
    print("invalid input")

# Index Error Practice
a=["Nakshatra", 7, "Frintu", 88, "Mintu"]
try:
    print(a[6])
except IndexError as e:
    print("Out of the count")

# Value Error Practice
try:
    a = int(input("Enter your age"))
    print(a)
    print("You are eligible for the content")
except ValueError:
    print(" can you please Enter the value")

# File Handling Practice


# Dictionary Lookup Practice
try:
    a = {"name":"nakshatra", "age":20, "score":300}
    print(a["gender"])
except KeyError:
    print("not in the list")

# Multiple Exceptions in One Block
try:
    a = int(input("Enter a number..."))
    b = int(input("Enter another number..."))
    result = a*b
    print("result:", result)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")

# Custom Error Handling
try:
    a =int(input("enter a number"))
    if a < 0:
        print("Negative numbers are not allowed.")
    else:
        print("Number is non negative.")
except ValueError:
    print("Please enter a valid integer.")

# copied from chatgpt








