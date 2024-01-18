# Tuple is a collection which is ordered and unchangeable. Once a tuple is created, we cannot change its values. In Python tuples are written with round brackets.

# 1. Create tuple
myTuple1 = (10, 1, 'dua', 200, 4.5, True, 'Hello World')
myTuple2 = 10, 1, 'dua', 200, 4.5, True, 'Hello World' # a tuple that consists of comma-separated values without brackets. We can create a tuple without brackets or parenthesis
myTuple4 = ('tuple',) # to create a tuple with only one item, we have to add a comma after the item, otherwise Python will not recognize it as a tuple.
print(myTuple1)
print(type(myTuple1))
print(myTuple2)
print(type(myTuple2))
print(myTuple4)
print(type(myTuple4))
print()

# 2. Access elements (items) and slicing
myTuple4 = (10, 1, 'dua', 200, 4.5, True, 'Hello World')
"""
             0  1    2     3    4    5          6       etc
            ----------------------------------------------
myTuple4 = (10, 1, 'dua', 200, 4.5, True, 'Hello World')
            ----------------------------------------------
        etc -7  -6    -5   -4   -3    -2       -1
"""

# We can access tuple items by referring to the index number, inside square brackets
print(myTuple4[0])  # using index to access the tuple items. the index is start from 0
print(myTuple4[0:5])  # by a colon, get the characters start from position 0 to position 5 (position 5 not included)
print(myTuple4[1:6])  # get the characters start from position 1 to position 6 (position 6 not included)
print(myTuple4[-4])  # negative indexes is start from -1
print(myTuple4[-5:-3])  # get the characters start from position -5 to position -3 (get position -4. position -3 not included)
print(myTuple4[4:])  # get the characters start from position 4 to the last character
print(myTuple4[:4])  # get the characters start from the first character to position 4 (position 4 not included)
print(myTuple4[-1:])  # get the characters start from position -1 to the last character
print(myTuple4[:-1])  # get the characters start from the first character to position -1 (position -1 not included)
print(myTuple4[-5:11])  # get the characters start from position -5 to the position 11 (etc and not included)
print(myTuple4[1:-2])   # get the characters start from position 1 to the position -2 (position -2 not included)
print()

# 3. Removing items
# We can't remove the items. But we can delete the tuple completely
# We also can't remove the items using built-in methods
myTuple5= (10, 1, 'dua', 200, 4.5, True, 'Hello World')
# del myTuple5(3)
# del myTuple5[1:3]
# print(myTuple5)
del myTuple5
# print(myTuple5) # this will cause an error because we have succsesfully deleted "myTuple4"
# myTuple5.remove('dua')
# myTuple5.pop(2)
# print(myTuple5)
print()

# 4. Operator in tuple
# addition
add1 = (10, 'dua', 200, 'Hello World')
add2 = (1, 4.5, True)
addTotal = add1 + add2
print(addTotal)

# multiplication
mul = (1, 4.5, True) * 3
print(mul)

# in, not in
membership = (10, 'dua', 200, 'Hello World')
print('Hello World' in membership)
print(10 not in membership)
print()