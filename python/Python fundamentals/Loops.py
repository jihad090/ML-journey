# For Loop
for i in range(5): # range(0, 5, 1)
  print(i)
else: 
  print('It executes when LOOP ended normally')

for i in range(1,7,2): # range(start, end, step)  !end will execute till end-1
  print(i)

fruits = ['Mango', 'Banana', 'Apple'] # like this it can trevarse though touple and set
for fruit in fruits:
  print(fruit)

# while loop
i = 1
while i <=5:
  print(i)
  i+=1
# | Feature  | for loop                   | while loop          |
# | -------- | -------------------------- | ------------------- |
# | Best for | known number of iterations | unknown repetitions |
# | Uses     | Iterating collection       | logical condition   |
# | Example  | for x in range(10)         | while x < 10        |


# continue skips currnt iteration and break breaks the loop in a certain point
for i in range(10):
  if i%3 == 0:
    continue
  if i>5:
    break
  print(i)  
# | Statement | Purpose                      |
# | --------- | ---------------------------- |
# | break     | stop loop                    |
# | continue  | skip next                    |
# | else      | executes if loop exits clean |

# -----Advance Looping -----
# enumerate() => it not only thaverse but also count index (starts from 0)
for index, fruit in enumerate(fruits):
  print(index, fruit)

# zip() => Looping over multiple sequesce
names = ["Jihad", "Fahad", "Amir"]
scores = [10, 12, 99]
for name, score in zip(names, scores):
  print(name, score)

# List comprehension (short powerful way to create list under some rules)
square = [x*x for x in range(10)]
print(square)

even = [x for x in range(10) if x%2==0]
print(even)

# iterating dictionary key
student = {'name':'Jihad', 'age':'23', 'mobile':'01834373977'}
student.items() # [('name', 'Jihad'), ('age', '23'), ('mobile', '01834373977')] -> this is a dict_item
for key,val in student.items():
  print(key,val)

# looping in reverse
for i in reversed(range(5)):
  print(i)

# | Feature              | Use                       |
# | -------------------- | ------------------------- |
# | enumerate            | tracking epoch index      |
# | zip                  | combine features & labels |
# | list comprehension   | fast preprocessing        |
# | filtering            | cleaning datasets         |
# | nested loops         | scanning image pixels     |
# | dictionary iteration | reading JSON results      |
