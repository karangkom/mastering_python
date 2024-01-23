"""
ARGUMENT:
Some information can be pass inside the function by using argument in the function parentheses. We can add many arguments as we want,
just separate them with comma.
"""

"""
Positional Arguments:
The variable (identifier) values of arguments, passed into function based on their position in the function call
"""

# Sample 1 (One argument)
def hello(a):  # (parameter)
    print(f'Hello {a}')


hello('saddam')  # (argument)
hello('rahmat')

# invalid argument:
# hello()

"""
Sample 1 notes:
- Parameter is the variable (identifier) listed inside the parentheses in the function definition.
- Argument is the value that passed into the function when it is called.
- We can put multiple or more than one argument in a function. If the number between argument and parameter not same, the interpreter will throw TypeError exception
"""

print('-' * 100)

# Sample 2 (Multiple arguments)
def hello(time, name):  # (parameters)
    print(f'Good {time}, Mr/Mrs. {name}')


hello('morning', 'saddam')  # (arguments)
hello('day', 'rahmat')
hello('afternoon', 'fuad')
hello('evening', 'fitri')

# Invalid arguments:
# hello()
# hello('morning')
# hello('saddam', 'morning') # incorrect position

"""
Sample 2 notes:
- By default, a function must be called with the correct position and values of arguments.
- The number between argument and parameter should be same
"""

print('-' * 100)

# Sample 3 (Combine with user input and call other function)
def main():
    name = input('Input your name: ')
    viewName(name)


def viewName(A):
    print('*' * 10)
    print(f'Good morning, {A} :)')


main()

print('-' * 100)

# Sample 4 (Passing numeric with user input as argument)
def chickenPrice(kg):
    price = 20000
    totalPrice = kg * price
    print(f'Total chicken meat price for {kg} kilos is, Rp. {totalPrice}')


print("Chicken meat price in a Kg is Rp. 20000")
chickenPrice(int(input('Input kilos: ')))

print('-' * 100)

# Sample 5 (Passing list & tuple as arguments and call other function)
# Type 1
def main(a):
    for i in a:
        print(i)


name = ['saddam', 'rahmat', 'fuad', 'fitri']

main(name)

print('-' * 100)

# Type 2
def myList(a):
    for i in a:
        print(i)


def myTuple(b):
    for j in b:
        print(j)


def main():
    list1 = ['jack', 'mike', 'luis']
    tuple1 = ('sandra', 'michel', 'jojo', 'lisa')

    print('Men:', '-' * 10)
    myList(list1)
    print()

    print('Women:', '-' * 10)
    myTuple(tuple1)


main()

print('-' * 100)

# Type 3
def result(b):
    print('-' * 10, 'Your items:', '-' * 10, )
    for j in b:
        print(j)


def items(a):
    print('Insert items:')
    empty = []

    for i in range(a):
        item = input(f'{i + 1}. ')
        empty.append(item)

    result(empty)


def main():
    list1 = items(int(input('How many item of list that you want?: ')))


main()
