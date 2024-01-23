"""
Keyword Arguments:
Keyword arguments are passed by its name instead of their position in the function call. So as a result, 
we don’t have to mind about the position of any argument that we have putted inside the argument parentheses.
"""
def args(a, b):
    print(f'My name is {a}. I am {b} years old')


args(a = 'Rahmat', b = 23)
args(b = 31, a = 'saddam')  # Since we are passing arguments through their names/keywords order, the arguments position doesn’t matter
args('fuad', b = 20)  # We can combine both positional and keyword arguments. But positional arguments should be followed by keyword arguments

# invalid keyword only arguments
# args(50, 'mike')  # the position is incorrect
# args('saddam')  # the number between argument and parameter are not same
# args(b = 18, 'fitri')  # we should not pass the keyword argument first before the positional argument