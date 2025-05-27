# read from a file
f = open("data.txt", "r")
content= f.read()
print(content)
f.close()

#read line by line
f = open("data.txt", "r")
line = f.readline()
print(line)
f.close()

#file pointer
f = open("data.txt", "r")
print(f.tell())
f.seek(8)
print(f.read())
f.close()

#exception handling in python
try:
    f = open("Nakshatra.jpg","r")
    content = f.read()
    print(content)
except FileNotFoundError:
     print("file is not found")
finally:
    try:
       f.close()
    except:
       pass

# Write a Python program to create a text file named sample.txt
file = open("sample.txt", "w")
file.write("Hello, this is a file handling practice")
file.close()

#wwrite the code to read the content in sample.txt
f = open("sample.txt", "r")
content = f.read()
print(content)
f.close()

#write a append code
f = open("sample.txt","a")
f.write("\n this is appended")
f.close()

#Write a Python program to count the number of lines, words, and characters in a text file sample.txt.
with open("data.txt","r") as f:
    lines= f.readlines()
num_lines = len(line)
num_words = 0
num_chars = 0
for line in lines:
    num_words += len(line.split())
    num_chars += len(line)
print("number of lines:", num_lines)
print("number of words:", num_words)
print("number of characters:", num_chars)

# write a program code to copy the content of one file to another
f = open("data.txt","r")
f1 = open("sample.txt","w")
for data in f:
    f1.write(data)

#Write a program that reads a file and prints only the lines that contain the word "Python".
with open("sample.txt","r") as file:
    for line in file:
        if line in file:
            print(line.strip())
#Write a program to merge two text files into a third file.
with open("data.txt","r") as file1:
    data1 = file1.read()
with open("sample.txt","r") as file2:
    data2 = file2.read()
with open("my_file.txt","w") as file3:
    file3.write(data1)
    file3.write(data2)
print("the file is merged successfully to the 'my_file.txt'")