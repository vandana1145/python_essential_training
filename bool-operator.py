a = True
b = False
x = ('Mini', 'Mouse', 'Hablo', 'Chiku', 'Teddy', 'Mithhu')
y = ('Mini')


if a and b:
    print('a and b: Expression is True.')
else:
    print('a and b: Expression is False.')

if a or b:
    print('a or b: Expression is True.')
else:
    print('a or b: Expression is False.')

if not b:
    print('not b: Expression is True.')
else:
    print('not b: Expression is False.')

if y in x:
    print('y in x: Expression is True.')
else:
    print('y in x: Expression is False.')

if y not in x:
    print('y not in x: Expression is True.')
else:
    print('y not in x: Expression is False.')

if y is x[0]:
    print('y is x[0]: Expression is True.')
else:
    print('y is x[0]: Expression is False.')

if y is not x[1]:
    print('y is not x[1]: Expression is True.')
else:
    print('y is not x[1]: Expression is False.')