#Write a program to input a string and print its length.
name = "nakshatra"
print(len(name))

# Count how many vowels (a, e, i, o, u) are in the input string.
vowels = "aeiouAEIOU"
text = input("Enter a string: ")
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Write a program that reverses a string using slicing.
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)




