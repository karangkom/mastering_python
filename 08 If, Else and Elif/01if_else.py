# Python supports the usual logical conditions from mathematics:

# 1. If
# If Statement is used for decision making
name1 = 'saddam'
name2 = 'rahmat'
others = ['fuad', 'fitri']
name3 = 'fitria'
con1 = True

if name1 == 'saddam':
    print(f'His name is {name1}') # Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.

if name1 != name2:
    print(f'"{name1}" is diffrent between "{name2}"')

if 'a' in name2:
    print(f"There is 'a' in {name2}")

if name3 in others: # sample of false condition. it will not execute:
    print(f'My name is {name3}')
print('My name is Along') # this is not part of if statement

if name3 not in others:
    print(f'There is no {name3} in others')

if name1: # without operator. it's refer to name1 == 'saddam' is True condition
    print('Your name is saddam')
#print(name1 == 'saddam')

if con1:
    print('Go ahead')

if name1 == name2: # sample of false condition. it will not execute:
    print('There are same')

print('-' * 100)

# 2. Else
# The else keyword catches anything which isn't caught by the preceding conditions.
number1 = 10
number2 = 20
if number1 > number2:
    print(f'{number1} is greater than {number2}')
else:
    print(f'{number1} is less than {number2}')

print('-' * 100)

#3. Nesting if
val1 = 75
val2 = 800

if val1 == 75:
    print(f'Your score: {val1}')
    print('Step 1')
    if val2 == 80:
        print(f'Your score: {val2}')
        print('Step 2')
else:
    print('Val1 must True!')

print('-' * 100)

#4. Input in if else
name4 = input('Input your name: ')
db_Name = 'saddam'

if name4 == db_Name:
    print('Your name registered')
else:
    print(f'{name4} is not registered')

print('-' * 100)

#5. Combine conditional statements
# and
age = int(input('Input your age: '))

if age >= 18 and age <= 30:
    print('You can enter')
else:
    print("You can't enter")

# or
dL = input('Do you have driving license? (y/n): ')
cD = input('Can you drive a car? (y/n): ')

if dL == 'y' or cD == 'y':
    print("Let's drive")
else:
    print("You can't drive")

print('-' * 100)

#6. invalid if else
number3 = int(input('Input number: '))

if number3 > 0:
    if number3 % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
else: # something invalid when we input less than number3 and odd numbers, the else statement must relies on indentation
    print('Invalid number')