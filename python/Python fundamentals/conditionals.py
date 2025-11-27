# conditionals
age = 22
if age > 56:
  print("Eligable")
elif age >= 22:
  print("Waiting")
else: 
  print("Out")

# ternary conditionals
age = 20
status = 'adult' if age>18 else 'Minor' # must put this in a single line

# `in`, `not in` , in conditions
numbers = ['num1', 'num2', 'num3'] 
if 'num1' in numbers:
  print('num1 found')

nums = {1,2,5,9,7,6,3,8}
even = [n for n in nums if n%2==0]
print(even)

# match-case (switch-case)
status = 200
match status:
  case 200:
    print('success')
  case 404:
    print('Not found')
  case _:
    print('Unknown status')

# | Operator | Meaning                      |
# | -------- | ---------------------------- |
# | `and`    | True if both are true        |
# | `or`     | True if at least one is true |
# | `not`    | Reverses boolean             |

# | Operator | Meaning          | Example |
# | -------- | ---------------- | ------- |
# | `>`      | Greater than     | x > 5   |
# | `<`      | Less than        | x < 10  |
# | `>=`     | Greater or equal | x >= 18 |
# | `<=`     | Less or equal    | x <= 20 |
# | `==`     | Equal            | x == 5  |
# | `!=`     | Not equal        | x != 10 |

# -----Advanced-----
scores = [70,78,90]
if all(score>60 for score in scores):
  print('All > 60')
if any(score>89 for score in scores):
  print("atleast one > 89")

name = ""
message = name or 'no name Provided'
print(message)

age = 15
assert age >= 18, "Age must be 18 or older"  # it will chk our input data is valid or not

# | Technique                 | Purpose                           |
# | ------------------------- | --------------------------------- |
# | Ternary operator          | One-line condition                |
# | `in`, `not in`            | Membership tests                  |
# | List comprehension filter | Fast conditional mapping          |
# | `match-case`              | Replacement for switch            |
# | `all()`, `any()`          | Logical evaluation on collections |
# | `assert`                  | Validation                        |
# | Inline boolean shortcuts  | Cleaner defaults                  |

