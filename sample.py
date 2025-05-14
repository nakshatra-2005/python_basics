x = 2
print(x)
x = x+2
print(x)
x += 2
print(x)
x *= 3
print(x)
x /= 2
print(x)
x -= 3
print(x)
a,b,c=8,1,2
print(a)
print(c)
print(b)
print(a<b)
print(a>=c)
print(b<c)
print(a==b)
print(a and b)
print(b or c)
print(not b)
print(not a)
print(not c)
a=("nakshatra", "chaithanya", "akhinandhan", "sai krishna")
b=("nakshatra", "akhinandan", "chaithanya", "sai krishna",)
c=a
print(a)
print(b)
print(c)
print(a is b)
print (a is not c)
print(a is c)
print(a is not b)
a=("nakshatra", "akhinandhan", "chaithanya", "sai krishna")
b=("nakshatra", "pavani", "sindhuja")
print(a,b)
print("nakshatra" in a,b)
print("pavani" not in a)
print("sindhuja" in b)
print("akhinandhan", "chaithanya", "sai krishna" in a)
print("pavani" in a)
a=18
b=11
print(a)
print(b)
print(a & b)
print(a and b)
a=23
b=12
print(a,b)
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
print(a<<4)
print(a>>3)
print(b<<4)
print(b>>3)
a=2
print(bin(a))
a=28
print(bin(a))
a=0b001
print(oct(a))
a=0x010a
print(oct(a))

a=0b0101
print(oct(a))

# 12-05-2005 sting operations
name = "nakshatra nelaveni"
print(len(name))
print(name[-4])
print(name[4])
a='nakshatra'
b='nelaveni'
c= a + " "+  b
print(c)
name = '   nakshatra nelaveni' #sring method
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
name = 'nakshatra nelaveni' #string center
print(name.center(30, '*'))
#string count
name = "she is nakshatra. she is a good girl. nakshatra loves too read and read"
print(name.count('nakshatra'))
print(len(name))
print(name.find('nakshatra', 20, 58)) #string find
name = 'n\ta\tk\ts\th\ta\tt\tr\ta\t' #string expandtab
print(name)
print(name.expandtabs(3))
name = 'akshay' 'arjun' 'varun' #.join
sep = " "
print(sep.join(name))
name = 'nakshatra' #.rjust
print(name.rjust(12, '$'))

#13-05-2025

#if else statements

a=3
b=3
if a==b:
    print("True")
else:
    print("False")

# Loops in Python
# While loop
a=25
while a>=20:
    print("Yes its true", a)
    a=a-1


a=1
while a<=5:
    print(' great', end="")
    b=1
    while b<=4:
        print("nakshatra", end="")
        b=b+1
    a=a+1
    print()

#For loop
a = ["nakshatra", 25, 88.9]
for b in a:
    print(b)

a = "nakshatra"
for b in a:
    print(b)

for a in ["sindhuja", "pavani", 28, 67.0, "chaithanya", 3+8j]:
    print(a)

for a in range(11, 25, 3):
    print(a)

for a in range(10, 5, -1):
    print(a)

for a in range(20):
    if a%5!=0:
        print(a)

# 14-05-2025
#list comprehension
a = [b for b in range(1, 100,) if b%2==0 ]
print(a)
a = "Nakshatra"
b=[c for c in a]
print(b)

#dictionary comprehension
a={b:b*3 for b in range(9)}
print(a)

# set comprehension
a={b*3 for b in range(8) }
print(a)

# Functions
def greet():
    print('hello', end="")
    print('nakshatra', end="")


def add(x,y):
    c = x + y
    print(c)

add(4,7)

def update(a):
    a = 6
    print(id(a))
    print("a", a)

x = 10
print(id(x))
update(x)
print("x", x)

def update(lst):
    print(id(lst))

    lst[1] = 25
    print(id(lst))
    print("x",lst)

lst = [10, 20, 30]
update(lst)
print("lst", lst)

#Arguments
def sum(*a):
    b=0
    for c in a:
        b = b + c
    print(b)
sum(2, 3, 4, 5,7)

def person(name, **data):
    print(name)
    print(data)

person('Nakshatra', age=20, city="karimnagar", phoneno=9959138221)

def person(name, **data):
    print(name)
    for a,b in data.items():
        print(a,b)
person('Lidvija', age=25, city='hyderabad', mob=9381362876)


a=10
def something():
    a = 88
    print('local',a)
something()
print('global', a)

a=88
def something():
    global a
    a = 45
    print('local fun',a)
something()
print('global fun', a)

a = 9
def something():
    a = 99
    x = globals()['a']
    print('global', a )
something()
print('local', a)

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd
lst = [85, 66, 55, 28, 113, 9, 123, ]
even, odd = count(lst)
print('even {} :, odd {} :'.format(even, odd) )






































