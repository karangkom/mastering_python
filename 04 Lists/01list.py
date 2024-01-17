# List is a collection which is ordered and changeable. Allows duplicate members.

# 1. Create list
myList1 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
print(myList1)
print()

# 2. Access elements (items) and slicing
myList2 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
"""
               0  1    2     3    4    5          6       etc
            ----------------------------------------------
   myList2 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
            ----------------------------------------------
        etc   -7  -6    -5   -4   -3    -2       -1

"""
print(myList2[0])  # using index to access the list items. the index is start from 0
print(myList2[0:5])  # by a colon, get the characters start from position 0 to position 5 (position 5 not included)
print(myList2[1:6])  # get the characters start from position 1 to position 6 (position 6 not included)
print(myList2[-4])  # negative indexes is start from -1
print(myList2[-5:-3])  # get the characters start from position -5 to position -3 (get position -4. position -3 not included)
print(myList2[4:])  # get the characters start from position 4 to the last character
print(myList2[:4])  # get the characters start from the first character to position 4 (position 4 not included)
print(myList2[-1:])  # get the characters start from position -1 to the last character
print(myList2[:-1])  # get the characters start from the first character to position -1 (position -1 not included)
print(myList2[-5:11])  # get the characters start from position -5 to the position 11 (etc and not included)
print(myList2[1:-2])   # get the characters start from position 1 to the position -2 (position -2 not included)
print()

# 3. Change items value
myList3 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
myList3[5] = False
print(myList3)
myList3[1:5] = [2, 'tiga', 67, 7.9]
print(myList3)
myList3[4:5] = ['saddam']
print()

# 4. Adding list
# a. Using addition operator
myList4 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
myList5 = ['tiga', 67, 7.9, False]
totalList = myList4 + myList5
print(totalList)

# b. Using index
myList6 = [1, 2, 3]
"""
               0  1  2  etc
            ------------
    myList6 = [1, 2, 3]
            ------------
        etc   -3 -2 -1
"""
# myList6[3] = ['saddam'] # using this to add last item will be error
# myList6[3:] = ['saddam']  # last
# print(myList6)
# myList6[:0] = ['rahmat'] # first
# print(myList6)
myList6[2:2] = ['fuad'] # third
print(myList6)
print()

# 5. Removing items
# a. Using empty list
myList7 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
# myList7[3] = [] # we can't remove the item by using this
myList7[:1] = []
print(myList7)
myList7[1:3] = []
print(myList7)
myList7[2:2] = [] # we can't remove the item by using this
print(myList7)

# b. Using del keyword
# we can also remove items using del keyword
myList8 = [10, 1, 'dua', 200, 4.5, True, 'Hello World']
del myList8[3] # remove index 3 item
print(myList8)
del myList8[1:3]
print(myList8)
# del myList8 # the del keyword can also delete the list completely
# print(myList8) # # this will cause an error because we have succsesfully deleted "myList8".
print()

# 6. Multidimensional list and access items
data1 = [1, 2, 3]
data2 = [4, 5]
x = [data1, data2]
"""
         0         1    <----- rows
    --------------------     
    [[1, 2, 3], [4, 5]]
    --------------------
      0  1  2    0  1   
      ^
      |
      |
     cols 
                    
"""
print(x)
print(x[0])
print(x[0][2])
print(x[1])
print(x[1][0])
print()

# 7. Operator in list
# addition
add1 = [10, 'dua', 200, 'Hello World']
add2 = [1, 4.5, True]
addTotal = add1 + add2
print(addTotal)
add3 = [add1 + add2] # 2 dimensions list
print(add3)

# multiplication
mul = [1, 4.5, True] * 3
print(mul)

# Membership
membership = [10, 'dua', 200, 'Hello World']
print('Hello World' in membership)
print(10 not in membership)
print()

# 8. List reference
data3 = [10, 'dua', 200, 'Hello World']
z = data3 # z will be a reference to data3 (copy by reference)
# z = data3[:]  # with colon mark, z will not be a reference to data3
z[2] = 8 # every change in the 'z' is automatically seen in 'data3' as well
print(data3)
print(z)
print(z == data3) # True
