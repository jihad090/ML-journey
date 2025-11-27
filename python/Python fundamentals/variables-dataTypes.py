# a dynamic typed container, decides type automatically based on value
import pandas as pd

name = 'Jihad' #can only hold text

age = 22 #single assignment
a, b, c = 1, 2, 3 #multiple assignment
x = y = z = 3 #provide same value to multiple variable

print(type(age)) #chk var type

# type conversion
x = 5
y = str(x)
print(type(y))

# get data directly from csv file
# df = pd.read_csv("house.csv")
# print(df.dtypes)

# -----list----- is a ordered (item mantains position), changable(mutable-> can add, update, delete) collection that allows duplicate items. Like an array
# important for loading and manipulating dataset

number = [1,2,3,3]
alphabet = ['a','v']

number.append(20) #add item
number.insert(2,-9) #insert at certain index, indexing start from 0
number.remove(20) #it will remove 20 from number, make sure that the value is present in the list else it will produce an error
number.pop() #remove last item
x = number[1] #read the value at index 1 and store it in x

print(number)

# -----Tuple----- is a ordered but immutable collection, that allows duplication
# inportant for storing fixed config (hyperparameters)
coordinates = (22.5, 22)
cities = ('Dhake','Ctg', 'Khulna')
  # why touple? we can do all things with List
  # Ans: It is faster than list, value will not change accidentally, good for fixed value like coordinates, previous record

# -----Set----- is a unordered(no fixed index, index[0] is not possible), mutable container but do not allow duplication.
# removing duplicates, imposing set operations on data

setVar = set(number)

items = {1, 2, 6, 3, -9}
items.add(5) # add a new element to the set, if the item already exists, then it will not add new item
items.remove(2) # remove specific item. If the item is not available it will produce a key error
items.discard(31) # works same as error but do not produce key error of key doesn't exists.
items.clear() # make the set empty
print(items) 

# set operation

A = {1, 2, 3}
B = {1, 3}
print(A.union(B)) # also intersection(), difference()....etc is possible.

# other data types
# | Type       | Example                | Mutable 
# | ---------- | ---------------------- | ------- 
# | complex    | `5+3j`                 | ❌       
# | bytes      | `bytes([1,2])`         | ❌       
# | bytearray  | `bytearray([1,2])`     | ✔       
# | memoryview | `memoryview(bytes(5))` | ✔       
# | frozenset  | `frozenset([1,2,3])`   | ❌       
# | range      | `range(10)`            | ❌       
# | NoneType   | `None`                 | ❌       
