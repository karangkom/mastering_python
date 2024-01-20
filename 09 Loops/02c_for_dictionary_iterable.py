# Dictionary as iterable

# Sample 1 (Key)
idData1 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for i in idData1:
    print(i)

# or
# print(idData1.keys())
# for i in idData1.keys():
#     print(i)

print('-' * 100)

# Sample 2 (Value)
idData2 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for j in idData2:
    print(idData2[j])

# or
# print(idData2.values())
# for j in idData2.values():
#     print(j)

print('-' * 100)

# Sample 3 (Key & Value)
idData3 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for k in idData3:
    print(f'{k} : {idData3[k]}')

print('-' * 100)

# Sample 4 (Combine with function)
idData4 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

key = []
value = []

for m in idData4:
    key.append(m) # Adds an element at the end of the empty list

for n in idData4.values():
    value.append(n)

for o, p in zip(key, value):  # zip() function is mainly used to combining data of two iterable elements together
    print(f'{o} : {p}')

print('-' * 100)

# Sample 4 (Simple way to combine with function)
idData5 = {
    'name': 'saddam',
    'age': 30,
    'country': 'indonesia',
    'score': 99
}

for q, r in idData5.items():
    print(f'{q} : {r}')