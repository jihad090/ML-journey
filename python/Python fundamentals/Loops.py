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
