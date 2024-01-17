# 2. Operators
print('Arithmetic Operators and maths')
print('Addition:')
add1 = 3
add2 = 3
addTotal = add1 + add2
print(f'{add1} + {add2} = {addTotal}')

print('\nSubtraction:')
flo1 = 3
sub2 = 3
subTotal = flo1 - sub2
print(f'{flo1} - {sub2} = {subTotal}')

print('\nMultiplication:')
mul1 = 3
mul2 = 3
mulTotal = mul1 * mul2
print(f'{mul1} * {mul2} = {mulTotal}')

print('\nDivision:')
div1 = 3
div2 = 3
divTotal = div1 / div2 # the data type of division is float. use casting to convert it
# divTotal = int(sub1 / sub2)
# print(type(divTotal))
print(f'{div1} * {div2} = {divTotal}')

print('\nModulus:')
mod1 = 2
mod2 = 3
modTotal = mod1 % mod2
print(f'{mod1} % {mod2} = {modTotal}')

print('\nExponentiation:')
exp1 = 2
exp2 = 3
expTotal = exp1 ** exp2
print(f'{exp1} ** {exp2} = {expTotal}')

print('\nFloor Division:')
flo1 = 3
flo2 = 2
floTotal = flo1 // flo2
print(f'{flo1} // {flo2} = {floTotal}')

print('\nFloat:')
int1 = 3
float1 = 2.0
intFloat = int1 * float1
# intFloat = int(int1 * float1)
# print(type(intFloat))
print(f'{int1} * {float1} = {intFloat}')

print('\nPriority:')
print(3 + 2 * 4) # 4 * 2 = 8, 8 + 3 = 11
print((3 + 2) * 4) # 3 + 2 = 5, 5 * 4 = 20
print((3 + 2) ** 4)

print('\nComparison Operators')
# Comparison operators are used to compare two values:
print(4 > 5)
print(6 < 10)
print(20 != 20)
print(20 == 20)
print(6.3 >= 6.30001)
print(2.0 <= 2.0002)

print('\nLogical Operators')
# Logical operators are used to combine conditional statements:
# 1. and
# Returns True if both statements are true
print(4 > 5 and 20 != 10) #false and true -> 0 and 1 = 0 (false). & is different between and (operator). and is logical operator. & is bitwise operator.
# 2. or
# Returns True if one of the statements is true
print(3 != 2 or 1 > 2)  #true or false -> 1 or 0 = 1 (true). | is different between or. or is logical operator. | is bitwise operator.

print('\nMembership Operators')
# Used to test if a sequence is presented in an object
# 1. in
Text = 'Hello World'
print('Hello' in Text)
print('Wall' in Text)
# 2. not in
print('Halo' not in Text)
print('World' not in Text)

print('\nBitwise Operators')
# Bitwise operators are used to compare (binary) numbers:
# AND
print(6 & 7) # each operands convert to the binaries
""" Sets each bit to 1 if both bits are 1
6 = 00000110
7 = 00000111 &
    00000110 = 6
"""

# OR
print(5 | 9)
""" Sets each bit to 1 if one of two bits is 1
5 = 00000101
9 = 00001001 |
    00001101 = 13
"""

# XOR
print(4 ^ 7)
""" Sets each bit to 1 if only one of two bits is 1
4 = 00000100
7 = 00000111 ^
  = 00000011 = 3
"""