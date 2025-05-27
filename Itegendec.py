#Create an Iterator from a List
num = [1,2,3,4,5]
def __init__(self):
    self.num=1
def __inter__(self):
    return self
def __next__(self):
    if self.num<=5:
        val = self.num
        self.num += 1
        return val
    else:
       raise StopIteration
values = num
for i in values:
    print(i)



#Check if an Object is Iterable or Iterator

from collections.abc import Iterator, Iterable
a = [1,2,3]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
it = iter(a)
print(isinstance(it, Iterator))






