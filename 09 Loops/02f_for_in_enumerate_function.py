# The enumerate() function adds a counter as the key of the enumerate object

idFoods1 = ['bakso', 'nasi padang', 'soto', 'coto makassar']

for index, elm in enumerate(idFoods1): # index start on 0
    print(f'{index + 1}. {elm}')

# same as:
# for i in range(len(idFoods1)):
#     print(f'{i + 1}. {idFoods1[i]}')