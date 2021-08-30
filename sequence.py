x = [1, 'two', [1,2,3], 4.0]
y = (1, 'two', [1,2,3], 4.0)
z = {'one': 1, 'two': '2', 'three': (1,2,3), 'four':[1,2,3,4]}

print(f'{type(x)} are mutable.')
print(f'{type(y)} are immutable.')
print(f'{type(z)} are mutable.')

for i, j in z.items():
    print(f'Key is {i} for the value pair of {j}')

print(id(x))
print(id(y))
print(id(x[1]))
print(id(y[1]))
print(id(z))


# isinstance  for x
if isinstance(x, list):
    print(f'{x}: Yes, it is a list')
elif isinstance(x, tuple):
    print(f"{x}: Oh no, it's a tuple.")
else:
    print(f"{x}: Look's like it's a dictionary.")
print()


# isinstance  for y
if isinstance(y, list):
    print(f'{y}: Yes, it is a list')
elif isinstance(y, tuple):
    print(f"{y}: Oh no, it's a tuple.")
else:
    print(f"{y}: Look's like it's a dictionary.")
print()


# isinstance  for z
if isinstance(z, list):
    print(f'{z}: Yes, it is a list')
elif isinstance(z, tuple):
    print(f"{z}: Oh no, it's a tuple.")
else:
    print(f"{z}: Look's like it's a dictionary.")
