"""
Default Arguments / Default Parameter Value:
Allow us to provide default value in the function definition parameter. Python will use these default value, 
if we doesn't pass any argument inside the function call.
"""

# Sample 1 (Single argument)
def args(a = 10): # default parameter value
    print(f'This is number {a}')


args()  # If we call the function without any argument, the function will use the default parameter value (e.g. a = 10)
args(2) # output: This is number 2

print('-' * 100)

# Sample 2 (Many arguments)
def args(a, b = 'Morning'):
    print(f'Hello Mr. {a}. Good {b}!')


args('Rahmat')  # a = 'Rahmat'. If the b argument is not set, the default value in parameter will be used (e.g. b = 'Morning')
args('Saddam', 'Evening')
args(b = 'Afternoon', a = 'fuad')  # the argument keyword value have high priority than the default parameter value

# Sample 3 (Invalid default parameter value)
# def args(a = 'saddam', b):
# def args(a = 'saddam', b, c = 'rahmat'):
# def args(a, b = 'saddam', c):
